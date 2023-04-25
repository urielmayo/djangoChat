from rest_framework import viewsets

from users.models import Profile
from chats.models import Chat, Message
from apis.serializers import (
    ProfileSerializer,
    ChatSerializer,
    MessageSerializer,
)


# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
