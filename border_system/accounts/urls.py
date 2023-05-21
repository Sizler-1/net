from django.urls import path
from .views import login_view, logout_view
from border.views import home

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
