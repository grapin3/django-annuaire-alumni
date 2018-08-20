from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

from .models import Member
from .forms import *

import logging
logger=logging.getLogger(__name__)

@login_required
def profile_list(request):
    user_list=User.objects.filter(is_active=True)
    return render(request, 'annuaire/profile_list.html',{
        'user_list': user_list,
        })

@login_required
def profile_display(request, username=None):
    if username:
        user = User.objects.get(username=username)
    else:
        user = request.user

    return render(request, 'annuaire/profile_display.html', {
        'user': user,
        })

@login_required
def profile_update(request):
    if request.method == "POST":
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST, request.FILES,
                instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            Profile = profile_form.save(commit=False)
            location = profile_form.cleaned_data['location'].split(", ")
            Profile.city = None
            Profile.region = None
            Profile.country = None
            if len(location)>=1:
                Profile.country = location[-1]
            if len(location)>=2:
                Profile.region = location[-2]
            if len(location)>=3:
                Profile.city = location[-3]
            Profile.save()

            messages.success(request, 'Votre profile a bien été mis à jour \o/')
            return redirect('display_profile')
        else:
            location = ""
            messages.error(request, 'Oups, il semblerait que vous ayez fait \
                    des erreurs. Merci de les corriger.')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile,)
        location = [request.user.profile.city,
                request.user.profile.region, request.user.profile.country]
        location = filter(lambda x: x != None, location)
        location = (", ").join(location)
    return render(request, 'annuaire/profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'location':location,
        })

@login_required
def profile_delete(request):
    if request.user.is_superuser:
        messages.error(request, "Impossible de supprimer le compte d'un \
                superutilisateur")
    else:
        username = request.user.username
        request.user.delete()
        logger.info("User %s has been deleted", username)
        messages.info(request, "Votre compte est désormais supprimé :(")
    return redirect('home')

def profile_register(request):
    form = RegistrationForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        messages.success(request, "Votre compte a bien été crée. Il faut \
                maintenant qu'un modérateur l'active.")
        return redirect('home')
    return render(request, 'annuaire/profile_register.html', {
        'form': form,
        })

@login_required
def member_list(request):
    member_list= Member.objects.all()
    return render(request, 'annuaire/member_list.html',{
        'member_list': member_list,
        })

@login_required
def member_register(request):
    member_form = MemberRegistrationForm(request.POST, request.FILES)

    if member_form.is_valid():
        member_form.save()
        messages.success(request, 'The member was successfully created!')
        return render(request, 'annuaire/member_registered.html',{
            'member_form': member_form,
            })
    else :
        return render(request, 'annuaire/member_register.html',{
            'member_form': member_form,
            })
