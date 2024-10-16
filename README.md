💬 Chatbot Application

Welcome to the Chatbot Application! This project is a simple chatbot interface created using Django, Python, HTML, and CSS. 
The chatbot responds to your queries with predefined answers, providing a fun, interactive chat experience. 😎🤖


✨ Features

- 🗣 Real-time chat interface: Chat live with the bot! Just type your message and get an instant response.
- 💬 Predefined responses: The chatbot provides witty and predefined answers to specific user queries.
- 🎨 Interactive UI: A clean, modern interface designed with HTML and CSS for a smooth chat experience.
- 🕒 Chat history: Easily review your previous conversations in the left-hand sidebar.

🛠 Technologies Used

- ⚙️ Django: Powerful Python framework for backend development.
- 🐍 Python: Core programming language for chatbot logic.
- 🌐 HTML/CSS: Frontend technologies used for designing the chat interface.
- 💻 JavaScript (optional): Enhances real-time interactivity (if implemented).

🚀 Getting Started

1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/chatbot-django.git
cd chatbot-django
```

2️⃣ Set up a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3️⃣ Install the dependencies
```bash
pip install -r requirements.txt
```

4️⃣ Migrate the database
```bash
python manage.py migrate
```

5️⃣ Run the development server
```bash
python manage.py runserver
```

6️⃣ Start chatting 💬
Open your browser and go to `http://127.0.0.1:8000/` to chat with the bot!

📋 Usage

- Chat Interface: Type a message in the input box and click `Send` to chat with the bot.
- Previous Chats: Your previous messages are saved in the "Previous Chats" section for easy access.



✨ Customization

- 🧠 Modify chatbot responses: You can update `views.py` to customize the bot's replies and add more intelligence!
- 🎨 Revamp the UI: Edit the CSS in the `static` folder to personalize the look and feel of the chat interface.
- 💾 Add database support: Integrate chat history storage or any other data management with Django models.

