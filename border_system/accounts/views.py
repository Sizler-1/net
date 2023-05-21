from django.shortcuts import render

# Create your views here.

from django.contrib.auth.views import LoginView, LogoutView

login_view = LoginView.as_view(template_name='accounts/login.html')
logout_view = LogoutView.as_view()
