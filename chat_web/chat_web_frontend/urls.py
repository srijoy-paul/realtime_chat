from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup_page'),
    path('home/', views.homepage, name='home_page'),
    path('login/', auth_views.LoginView.as_view(template_name='chat_web_frontend/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('rooms/', views.rooms, name='rooms')
]