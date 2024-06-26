from django import forms
from mailing_service.forms import FormStyleMixin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User


class UserRegisterForm(FormStyleMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'country', 'phone')


class UserProfileForm(FormStyleMixin, UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'phone', 'country',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
