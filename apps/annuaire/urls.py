from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
        path( 'profile', views.display_profile, name='profile'),
        ]
