from django.contrib.auth import views as auth_views
from django.views.generic import FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from users.models import Profile

from users.forms import SignUpForm, ProfileForm, UserUpdateForm

# Create your views here.


class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """LogoutView"""


class SignUpView(FormView):
    template_name = 'users/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'users/update.html'
    success_url = reverse_lazy('chats:chats')
    form_class = ProfileForm

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        context['user_form'] = UserUpdateForm(instance=self.request.user)
        return context

    def get_object(self, queryset=None):
        # Get the Profile object for the current user
        return get_object_or_404(Profile, user=self.request.user)

    def form_valid(self, form):
        user_form = UserUpdateForm(
            instance=self.request.user,
            data=self.request.POST,
        )
        if user_form.is_valid():
            user_form.save()
        else:
            return self.form_invalid(form)
        return super().form_valid(form)
