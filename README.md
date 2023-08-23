# MeetAyla Chatbot

MeetAyla Chatbot is a web-based application that provides users with a virtual chatbot interface to interact with a women's health chatbot named Ayla. Users can ask questions and receive responses from the chatbot on various health-related topics.

## Features

- Chat with Ayla: Users can enter their questions or concerns and receive responses from the Ayla chatbot.
- Chat History: Users can view their chat history and previous interactions with the chatbot.
- New Chat: Users can start a new chat session, clearing the chat history.
- Settings: Users can access settings to manage their chatbot interactions.

## Technologies Used

- Python (Django framework)
- HTML/CSS
- JavaScript
- Tailwind CSS for styling
- OpenAI GPT-3.5 Turbo for chatbot responses
- AWS EC2 for hosting

## Setup

1. Clone the repository:
  ```
  git clone https://github.com/AugustHottie/meetayla-chatbot.git
  ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate
   ```
   
3. Install the required dependencies:
  ```
  pip install -r requirements.txt
  ```

4. Set up environment variables:
- Create a `.env` file in the root directory and add your OpenAI API key:

  ```
  OPENAI_API_KEY=your_api_key_here
  ```
  
5. Run migrations:
   
   ```
   python manage.py migrate
   ```
   
6. Start the development server:
   
    ```
    python manage.py runserver
    ```

7. Access the application in your web browser at `http://localhost:8000`.

## Usage

1. Register an account or log in if you have an existing account.
2. Start chatting with Ayla by entering your questions in the chat input field.
3. View your chat history, start a new chat, or access settings from the navigation menu.

## Credits

- Built by augusthottie
- Frontend implementation by kokocodes
- Fronted design by sam
- Powered by [OpenAI GPT-3.5 Turbo](https://beta.openai.com/)
- Icons from [SVGRepo](https://www.svgrepo.com/)

## License

This project is licensed under the [MIT License](LICENSE).

---

For any questions or support, please feel free to contact me @ chimexjessica@outlook.com.



