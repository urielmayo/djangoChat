from django.contrib import admin

from chats.models import Chat, Message
# Register your models here.
@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'user_1',
        'user_2',
        'last_message'
    ]

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    
    list_display = [
        'sender',
        'receiver',
        'sent_date',
    ]

    list_filter = [
        'sender',
        'receiver'
    ]

    list_display_links = list_display