from django.db import models

class Message(models.Model):
    name = models.CharField('Name', max_length=50)
    telegramUser = models.CharField('Telegram username', max_length=50)
    message = models.TextField('Message', max_length=500)

    def __str__(self):
        return self.name