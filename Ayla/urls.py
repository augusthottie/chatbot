from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('chatbot/', views.chatbot_view, name='chatbot'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('history/', views.history_view, name='history'),
    path('settings/', views.settings_view, name='settings'),
]