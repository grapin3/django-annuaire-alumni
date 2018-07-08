from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

from .models import Member
from .form import *
ProfileRegistrationForm

import logging
logger=logging.getLogger(__name__)

@login_required
def show_profiles(request):
    profile_list=Profile.objects.all()
    return render(request, 'annuaire/profile_list.html',{
        'profile_list': profile_list,
        })

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

@login_required
def show_members(request):
    member_list= Member.objects.all()
    return render(request, 'annuaire/member_list.html',{
        'member_list': member_list,
        })

@login_required
def create_member(request):
        member_form = MemberRegistrationForm(request.POST, request.FILES)

        if member_form.is_valid():
            member_form.save()
            messages.success(request, 'The member was successfully created!')
            return render(request, 'annuaire/member_created.html',{
                'member_form': member_form,
                })
        else :
            return render(request, 'annuaire/create_member.html',{
                'member_form': member_form,
                })

def index(request):
    return render(request,'annuaire/index.html')
