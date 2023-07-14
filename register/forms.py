from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
User = get_user_model()

class UserCreationForm_1(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")

    phone_user = forms.CharField(validators = [phoneNumberRegex], max_length = 11)
    class Meta(UserCreationForm.Meta):
        model= User
        fields = ("username", 'phone_user')