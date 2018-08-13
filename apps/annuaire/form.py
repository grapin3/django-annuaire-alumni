from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile, Member

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo', 'bio', 'promo', 'city', 'region', 'country',
                'gender', 'gap_year', 'miscellaneous',)
        help_texts = {
                'promo': "Année de votre diplome",
                }

    def clean(self):
        cleaned_data = super(ProfileEditForm, self).clean()
        city = cleaned_data.get('city')
        region = cleaned_data.get('region')
        country = cleaned_data.get('country')

        if city:
            city = city.split(", ")
            cleaned_data["country"] = None
            cleaned_data["region"] = None
            if len(city)>=1:
                cleaned_data["country"] = city[-1]
            if len(city)>=2:
                cleaned_data["region"] = city[-2]
            if len(city)>=3:
                cleaned_data["city"] = city[-3]
            else:
                cleaned_data["city"] = None
            
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
