# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('click/<str:button_type>/', views.record_click, name='record_click'),
    path('contact-whatsapp/<str:button_type>/', views.redirect_to_whatsapp, name='contact_whatsapp'),
     path('initiate-call/<str:button_type>/', views.initiate_call, name='initiate_call'),
]