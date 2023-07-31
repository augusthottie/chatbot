from django.db import models
from django.contrib.auth.models import User

class Chatbot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.message}"

# class User(models.Model):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=128)  
#     def __str__(self):
#         return self.username

# class Conversation(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user} - {self.timestamp}"

# class Message(models.Model):
#     conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
#     content = models.TextField()
#     is_user_message = models.BooleanField(default=False)  # To differentiate user messages from chatbot responses
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.conversation} - {'User' if self.is_user_message else 'Chatbot'} - {self.timestamp}"

