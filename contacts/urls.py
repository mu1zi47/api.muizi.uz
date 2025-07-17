from django.urls import path
from . import views

urlpatterns = [
    path('message/create/', views.MessageCreateAPIView.as_view(), name='message-create'),
    path('message/list/', views.MessageListAPIView.as_view(), name='message-list'),  # ✅ новый GET
]