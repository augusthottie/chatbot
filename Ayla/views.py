import os

from .forms import RegistrationForm

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

import openai
from openai.error import InvalidRequestError
from .models import  Chatbot
from dotenv import load_dotenv
load_dotenv()

#home view
def home_view(request):
    return render(request, 'home.html')

def get_chatbot_response(user_input):
    try:
        openai.api_key = os.environ.get('OPENAI_API_KEY')
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a women's health chatbot. Your name is Ayla."},
                {"role": "user", "content": user_input},
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except InvalidRequestError as e:
        # Handle invalid request error
        return HttpResponse("Invalid Request: " + str(e))
    except Exception as e:
        # Handle other errors
        return HttpResponse("An error occurred: " + str(e))

#chatbot view
@login_required
def chatbot_view(request):
    # Retrieve the conversation history from the user's session
    conversation_history = request.session.get('conversation_history', [])

    # Initialize chatbot_response with an empty string
    chatbot_response = ''

    if request.method == 'POST':
        # Check if the "Send" button is clicked
        if 'send_button' in request.POST:
            user_input = request.POST.get('user_input', '')
            # Assuming you have properly set up the authentication middleware,
            # you can directly use request.user to get the authenticated user.
            chatbot_response = get_chatbot_response(user_input)

            # Add the username to the chatbot response
            chatbot_response = f"Hi {request.user.username}, {chatbot_response}"

            # Save the user input and chatbot response in the Chatbot model
            chatbot_entry = Chatbot.objects.create(
                user=request.user,
                message=user_input,
                response=chatbot_response,
            )

            # Append the user input and chatbot response to the conversation history
            conversation_history.append({
                'user_input': user_input,
                'chatbot_response': chatbot_response,
            })

            # Store the updated conversation history in the user's session
            request.session['conversation_history'] = conversation_history

            # Redirect to a new URL after processing the form submission
            return redirect('chatbot')

    else:
        # If it's not a POST request, set chatbot_response to an empty string
        chatbot_response = ''

    return render(request, 'chatbot.html', {'conversation_history': conversation_history, 'chatbot_response': chatbot_response})

    
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chatbot')

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('chatbot')
        
        else:
            return redirect('login')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')