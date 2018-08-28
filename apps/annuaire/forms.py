from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import Profile, Member

class UserEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

class ProfileEditForm(forms.ModelForm):
    # ToDo: add a proper clean function for the location field
    # We use a custom field to merge all the location info in a single field
    # Translators: Used as the field label during the form rendering
    location = forms.CharField(label=_('Residence'), required=False)
    # Here we define a custom leisure field. We have to manage it manually to be
    # able to add new tag "on the fly"
    leisure = forms.CharField(label=_('Loisir'), widget=forms.SelectMultiple, required=False)
    class Meta:
        model = Profile
        fields = ('leisure', 'photo', 'bio', 'promo', 'gender', 'gap_year', 'miscellaneous',)
        help_texts = {
                'promo': _("Graduating year"),
                'gap_year': _("I took a gap year"),
                }

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('firstname', 'lastname',)

class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',)

class MemberRegistrationForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('firstname', 'lastname',)
