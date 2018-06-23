from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def display_profile(request, user_id=None):
    if user_id:
        user = User.objects.get(pk=user_id)
    else:
        user = request.user

    return render(request, 'annuaire/profile.html', {
        'user': user,
        })
