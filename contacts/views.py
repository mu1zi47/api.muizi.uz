from rest_framework import generics, permissions
from rest_framework.throttling import AnonRateThrottle
from .models import Message
from .serializers import MessageSerializer


# Ограничиваем только POST-запросы
class PostThrottle(AnonRateThrottle):
    scope = "post_only"

    def allow_request(self, request, view):
        # Разрешаем все запросы кроме POST
        if request.method != "POST":
            return True
        return super().allow_request(request, view)


class MessageCreateAPIView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.AllowAny]  # любой может отправить
    throttle_classes = [PostThrottle]  # Ограничение только на POST

    def perform_create(self, serializer):
        message = serializer.save()
        # Здесь можешь отправлять уведомление в Telegram/email
        # async_to_sync(send_message_notification)(message)

class MessageListAPIView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAdminUser]  # Только админ может смотреть (можно AllowAny)