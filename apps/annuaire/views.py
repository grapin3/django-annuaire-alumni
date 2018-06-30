from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

from .form import UserForm, ProfileForm, UserRegistrationForm,\
ProfileRegistrationForm

import logging
logger=logging.getLogger(__name__)

@login_required
def display_profile(request, user_id=None):
    if user_id:
        user = User.objects.get(pk=user_id)
    else:
        user = request.user

    return render(request, 'annuaire/profile.html', {
        'user': user,
        })

@login_required
def update_profile(request):
    user_form = UserForm(request.POST or None, instance=request.user)
    profile_form = ProfileForm(request.POST or None, request.FILES, instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        messages.success(request, 'Your profile was successfully updated!')
        return redirect('profile')
    else:
        messages.error(request, 'Please correct the error below.')
    return render(request, 'annuaire/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def create_profile(request):
    user_form = UserRegistrationForm(request.POST or None,
            initial={'is_active':False}, )
    profile_form = ProfileRegistrationForm(request.POST or None, request.FILES)

    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        #profile_form.save()
    logger.info("Rendering Create Profile page")
    return render(request, 'annuaire/create_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        })

def index(request):
    return render(request,'annuaire/index.html')
