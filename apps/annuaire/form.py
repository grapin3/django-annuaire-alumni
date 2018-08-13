from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile, Member

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo', 'bio', 'promo', 'gap_year', 'miscellaneous',)
        help_texts = {
                'promo': "Année de votre diplome",
                }

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('firstname', 'lastname',)

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name',
        'last_name',)

class MemberRegistrationForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('firstname', 'lastname',)
