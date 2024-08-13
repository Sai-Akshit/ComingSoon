from django.urls import path
from . import views

app_name = 'requestemail'

urlpatterns = [
    path('', views.request_email, name='request_email'),
]