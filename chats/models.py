from django.db import models
from django.utils.timezone import now

# Create your models here.


class Chat(models.Model):
    user_1 = models.ForeignKey(
        'users.Profile',
        on_delete=models.CASCADE,
        related_name='user_1',
    )
    user_2 = models.ForeignKey(
        'users.Profile',
        on_delete=models.CASCADE,
        related_name='user_2',
    )
    last_message = models.DateTimeField(blank=True, default=now)

    def __str__(self):
        return f'{self.user_1} | {self.user_2}'


class Message(models.Model):
    sender = models.ForeignKey(
        'users.Profile',
        on_delete=models.CASCADE,
        related_name='sent_messages',
    )
    receiver = models.ForeignKey(
        'users.Profile',
        on_delete=models.CASCADE,
        related_name='received_messages',
    )
    chat = models.ForeignKey(
        'Chat',
        on_delete=models.CASCADE,
        related_name='messages',
    )

    message = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}: {self.message}'
