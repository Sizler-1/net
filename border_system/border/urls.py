from django.urls import path, include
from . import views
from authentication.views import home
from .views import home
from django.views.generic import TemplateView


urlpatterns =[
    path('', home, name='home'),    
    path('add_border_crossing/', views.add_border_crossing, name='add_border_crossing'),
    path('view_vaccines/<int:crossing_id>/', views.view_vaccines, name='view_vaccines'),
    path('add_vaccine/<int:crossing_id>/', views.add_vaccine, name='add_vaccine'),
    path('login/', views.login, name='login'),
    path('login',TemplateView.as_view(template_name = 'login.html')),
    path('records/', views.vaccination_records, name='vaccination_records'),
    path('about/', views.about, name='about'),
]
