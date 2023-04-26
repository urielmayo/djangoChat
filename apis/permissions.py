from rest_framework import permissions


class IsInChatPermission(permissions.BasePermission):
    message = 'User is not in chat'

    def has_object_permission(self, request, view, obj):
        # Instance must have an attribute named `owner`.
        profile = request.user.profile
        return obj.user_1 == profile or obj.user_2 == profile
