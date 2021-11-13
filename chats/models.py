from django.db import models
from users.models import Profile
from django.utils.timezone import now

# Create your models here.
class Chat(models.Model):
    user_1 = models.ForeignKey(
        'users.Profile',
        on_delete=models.CASCADE,
        related_name='user_1'
    )
    
    user_2 = models.ForeignKey(
        'users.Profile',
        on_delete=models.CASCADE,
        related_name='user_2'
    )

    last_message = models.DateTimeField(blank=True, default=now)

    def __str__(self):
        return f'{self.user_1} | {self.user_2}'



class Message(models.Model):
    sender = models.ForeignKey(
        'users.Profile',
        on_delete=models.CASCADE,
        related_name= 'sender'
    )
    
    receiver = models.ForeignKey(
        'users.Profile',
        on_delete=models.CASCADE,
        related_name= 'receiver'
    )
    
    chat = models.ForeignKey(
        'Chat', 
        on_delete=models.CASCADE,
        related_name='chat'
    )

    message = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'from {self.sender} to {self.receiver}: {self.message}'
