from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
)
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


attrs = {
    'class': 'form-control'
}


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = _('User Name')
        self.fields['password'].label = _('Password')

        self.fields['username'].widget.attrs.update(attrs)
        self.fields['password'].widget.attrs.update(attrs)


class CreateUserForm(UserCreationForm):

    first_name = forms.CharField(
        label=_('First Name'),
        widget=forms.TextInput(attrs=attrs)
    )

    last_name = forms.CharField(
        label=_('Last Name'),
        widget=forms.TextInput(attrs=attrs)
    )

    username = forms.CharField(
        label=_('User Name'),
        widget=forms.TextInput(attrs=attrs)
    )

    email = forms.EmailField(
        label=_('Email'),
        widget=forms.EmailInput(attrs=attrs)
    )

    password1 = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs=attrs)
    )

    password2 = forms.CharField(
        label=_('Password Confirmation'),
        strip=False,
        widget=forms.PasswordInput(attrs=attrs)
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
        )


class ProfileForm(UserChangeForm):

    password = None

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'email',
        ]

        widgets = {
            'first_name': forms.TextInput(attrs=attrs),
            'last_name': forms.TextInput(attrs=attrs),
            'email': forms.EmailInput(attrs=attrs),
        }

        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'email': _('Email'),
        }