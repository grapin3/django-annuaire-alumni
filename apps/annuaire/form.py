from django import forms
from django.contrib.auth.models import User

from .models import Profile, Member

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo', 'bio', 'promo', 'gap_year', 'miscellaneous',)

    #  We define here the bootstrap class to use. First we put the default
    #  form-control class for all the widget, and then we modify the
    #  specific fields like file or checkbox
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['photo'].widget.attrs.update({'class':'form-control-file'})
        self.fields['gap_year'].widget.attrs.update({'class': 'form-check mt-2'})

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

    #  See the comment in ProfileForm
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs['readonly'] = True
        

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('firstname', 'lastname',)

class UserRegistrationForm(forms.ModelForm):
    # We will make sure that the created user is inactive in the view
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
    password1 = forms.CharField(label="Password",
        widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation",
        widget=forms.PasswordInput,
        help_text="Enter the same password as above, for verification.")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active=False
        if commit:
            user.save()

        return user

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', )

class MemberRegistrationForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('firstname', 'lastname',)

class ProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo', 'bio', 'promo', 'gap_year', 'miscellaneous',)

