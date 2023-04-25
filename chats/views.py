from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.db.models import Q

from chats.models import Message, Chat
from users.models import Profile
# Create your views here.


class ChatDetailView(LoginRequiredMixin, DetailView):
    template_name = 'detail_chat.html'
    model = Chat

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.filter(chat=context['chat'].pk)
        profile = self.request.user.profile
        if context['chat'].user_1 == profile:
            context['receiver'] = context['chat'].user_2
        else:
            context['receiver'] = context['chat'].user_1
        return context


class ProfileChatsView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'chats.html'
    context_object_name = 'chats'

    def get_queryset(self):
        profile = self.request.user.profile
        queryset = Chat.objects.filter(
            Q(user_1=profile) | Q(user_2=profile)
        ).order_by('-last_message')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProfileChatsView, self).get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
        return context


@login_required
def send_chat(request, pk):
    if request.method == 'POST':
        if request.POST['message-text'] != '':
            chat = get_object_or_404(Chat, pk=pk)
            if chat.user_1.user == request.user:
                receiver = chat.user_2.user
            else:
                receiver = chat.user_1.user
            Message.objects.create(
                sender=request.user.profile,
                receiver=receiver.profile,
                chat=chat,
                message=request.POST['message-text']
            )
            chat.last_message = now()
            chat.save()
            return redirect(reverse('chats:detail', kwargs={'pk': pk}))
        else:
            context = {
                'error': 'mensaje vacio'
            }
            return render(
                request,
                reverse('chats:detail', kwargs={'pk': pk}),
                context=context
            )
    return redirect(reverse('chats:detail', kwargs={'pk': pk}))


class NewChatView(LoginRequiredMixin, ListView):
    template_name = 'list_profiles.html'
    model = Profile
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.exclude(pk=self.request.user.profile.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logged_profile = context['view'].request.user.profile
        added_users = {}

        for chat in logged_profile.user_1.all():
            added_users[chat.user_2] = Chat.objects.get(
                user_1=logged_profile,
                user_2=chat.user_2
            ).pk

        for chat in logged_profile.user_2.all():
            added_users[chat.user_1] = Chat.objects.get(
                user_2=logged_profile,
                user_1=chat.user_1
            ).pk

        context['added_users'] = added_users
        return context


@login_required
def create_chat(request, pk):
    logged_profile = request.user.profile
    user_2 = Profile.objects.get(pk=pk)
    new_chat = Chat.objects.create(user_1=logged_profile, user_2=user_2)
    return redirect(reverse('chats:detail', kwargs={'pk': new_chat.pk}))
