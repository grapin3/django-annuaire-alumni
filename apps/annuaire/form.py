from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile, Member

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo', 'bio', 'promo', 'gap_year', 'miscellaneous',)
        help_texts = {
                'promo': "Année de votre diplome",
                }

    #  We define here the bootstrap class to use. First we put the default
    #  form-control class for all the widget, and then we modify the
    #  specific fields like file or checkbox
    #  def __init__(self, *args, **kwargs):
        #  super().__init__(*args, **kwargs)
        #  for field in self.fields:
            #  self.fields[field].widget.attrs.update({'class': 'form-control'})
        #  self.fields['photo'].widget.attrs.update({'class':'form-control-file'})
        #  self.fields['gap_year'].widget.attrs.update({'class': 'form-check mt-2'})

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

    #  See the comment in ProfileForm
    #  def __init__(self, *args, **kwargs):
        #  super().__init__(*args, **kwargs)
        #  for field in self.fields:
            #  self.fields[field].widget.attrs.update({'class': 'form-control'})
        #  self.fields['email'].widget.attrs['readonly'] = True
        

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
