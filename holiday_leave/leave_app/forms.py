from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    is_manager = forms.BooleanField(required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'full_name', 'emp_no', 'client_squad', 'role', 'location',
                  'start_date', 'deployed_date', 'full_year_leave_entitlement', 'is_manager')
