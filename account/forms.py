from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db.models import fields

from account.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:

        model = Account
        fields = ['username', 'email']