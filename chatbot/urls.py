from django.urls import path
from django.contrib import admin
from chat.views import chatbot_view, process_message, get_chat_messages, create_new_chat

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', chatbot_view, name='chatbot_view'),  # Optional if this is your homepage
    path('chat/<int:chat_id>/', chatbot_view, name='chatbot_view_with_id'),  # Add this line to accept chat_id
    path('process_message/', process_message, name='process_message'),
    path('get_chat_messages/<int:chat_id>/', get_chat_messages, name='get_chat_messages'),
    path('create_new_chat/', create_new_chat, name='create_new_chat'),
]
