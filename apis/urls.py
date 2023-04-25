from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet, basename="profile")
router.register(r'chats', views.ChatViewSet, basename="chat")
router.register(r'messages', views.MessageViewSet, basename="mesage")


urlpatterns = [
    path('', include(router.urls)),
]
