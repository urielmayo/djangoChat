from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from users.models import Profile
from chats.models import Chat, Message
from apis.serializers import (
    ProfileSerializer,
    ChatSerializer,
    MessageSerializer,
)
from apis.permissions import IsInChatPermission


# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [
        IsAuthenticated,
    ]


class ChatViewSet(viewsets.ModelViewSet):
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated, IsInChatPermission]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Chat.objects.all()
        profile = self.request.user.profile
        return Chat.objects.filter(user_1=profile) | Chat.objects.filter(
            user_2=profile
        )

    @action(detail=True, methods=['POST'])
    def send_message(self, request, pk=None):
        profile = self.request.user.profile
        chat = self.get_object()
        receiver = chat.user_2 if chat.user_2 != profile else chat.user_1
        data = {
            'sender': profile.pk,
            'receiver': receiver.pk,
            'chat': chat.pk,
            'message': request.data['message'],
        }
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    @action(detail=True, methods=['GET'])
    def messages(self, request, pk=None):
        chat = self.get_object()
        serializer = MessageSerializer(chat.messages.all(), many=True)
        return Response(serializer.data)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
