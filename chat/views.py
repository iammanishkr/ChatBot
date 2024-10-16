import json
import nltk
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Chat, Message
from .forms import MessageForm

# Download necessary NLTK data
nltk.download('punkt')
from nltk.tokenize import word_tokenize

# Predefined chatbot responses
DEFAULT_RESPONSE = "I'm sorry, I don't understand that."
responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there! What can I do for you?",
    "how are you": "I'm just a bot, but thanks for asking!",
    "bye": "Goodbye! Have a great day!",
    "what is your name?": "I'm a simple chatbot created to assist you!",
    "what can you do?": "I can answer simple questions and chat with you. Try asking me something!",
    "tell me a joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "help": "Sure! You can ask me about my capabilities or just chat with me.",
    "what time is it?": "I can't check the time, but you can look at your device's clock!",
    "what is the weather like?": "I don't have real-time data, but you can check a weather app for that.",
    "tell me something interesting": "Did you know honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old!",
    "i'm sad": "I'm sorry to hear that. Sometimes talking helps. Want to share what's on your mind?",
    "i'm happy": "That's great to hear! What made your day so good?",
    "what's your favorite color?": "I don't have preferences like humans do, but I think all colors are beautiful!",
    "can you speak other languages?": "I primarily understand English, but you can try asking me in another language!",
    "who created you?": "I was created by developers to assist users in chatting and answering questions.",
    "tell me about yourself": "I'm a simple chatbot here to help you with your questions and engage in conversation!",
    "how can I improve my day?": "Sometimes a small act of kindness can improve your day! How about helping someone out?",
}

def get_current_chat(chat_id):
    if chat_id:
        return get_object_or_404(Chat, id=chat_id)
    return None  # Return None if no chat_id is provided

def get_bot_response(user_message):
    return responses.get(user_message.lower(), DEFAULT_RESPONSE)

def create_message(chat, content, is_user):
    return Message.objects.create(chat=chat, content=content, is_user=is_user)

def chatbot_view(request, chat_id=None):
    # Fetch the chat with chat_id or set current_chat to None for new chat
    current_chat = get_current_chat(chat_id)
    current_chat_messages = current_chat.messages.all().order_by('timestamp') if current_chat else []
    
    # Fetch all previous chats for the sidebar
    chats = Chat.objects.all().order_by('-created_at')
    
    # Initialize the form
    form = MessageForm()

    # Handle form submission for new messages
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['content']
            # Use the current chat if available, otherwise create a new chat
            chat = current_chat if current_chat else Chat.objects.create(title=user_message[:30])
            
            # Save user and bot messages
            create_message(chat, user_message, True)
            bot_response = get_bot_response(user_message)
            create_message(chat, bot_response, False)

            # Redirect back to the chat with new messages loaded
            return redirect('chatbot_view_with_id', chat_id=chat.id)

    # Render the template with all chats, current chat, and form
    context = {
        'chat_history': chats,                # List of previous chats
        'current_chat': current_chat,         # Current selected chat
        'current_chat_messages': current_chat_messages, # Messages for the current chat
        'form': form,                         # Message form
    }
    return render(request, 'index.html', context)


@csrf_exempt
def process_message(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        chat_id = request.POST.get('chat_id')
        chat = get_object_or_404(Chat, id=chat_id) if chat_id else Chat.objects.first()
        
        create_message(chat, user_message, True)
        bot_response = get_bot_response(user_message)
        create_message(chat, bot_response, False)

        return JsonResponse({'status': 'success', 'response': bot_response})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def get_chat_messages(request, chat_id):
    try:
        chat = get_object_or_404(Chat, id=chat_id)
        messages = Message.objects.filter(chat=chat).values('content', 'is_user', 'timestamp')
        messages_list = list(messages)
        return JsonResponse({'status': 'success', 'messages': messages_list})
    except Chat.DoesNotExist:
        return JsonResponse({'status': 'error', 'message ': 'Chat not found'})

def create_new_chat(request):
    if request.method == 'POST':
        title = request.POST.get('title', 'New Chat')
        chat = Chat.objects.create(title=title)
        return redirect('chatbot_view_with_id', chat_id=chat.id)
    else:
        return render(request, 'index.html')
