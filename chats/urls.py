from django.urls import path

from chats import views

urlpatterns = [
    path(
        route='',
        view=views.ProfileChatsView.as_view(),
        name='chats',
    ),
    path(
        route='chats/<int:pk>/',
        view=views.ChatDetailView.as_view(),
        name='detail',
    ),
    path(
        route='chats/sendchat/<int:pk>',
        view=views.send_chat,
        name='sendchat',
    ),
    path(
        route='chats/new/',
        view=views.NewChatView.as_view(),
        name='list_profiles',
    ),
    path(
        route='chats/create/<int:pk>',
        view=views.create_chat,
        name='create',
    ),
]
