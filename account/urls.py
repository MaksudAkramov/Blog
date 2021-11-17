from django.contrib import admin
from django.urls import path

from account.views import log_user_in, log_user_out, register

urlpatterns = [
    path('login/', log_user_in, name='login'),
    path('register/', register, name='register'),
    path('logout/', log_user_out, name='logout')
]
