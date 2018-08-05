from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
        path('', views.index, name='index'),

        #Gestion des profiles utilisateurs
        path( 'profile', views.display_profile, name='profile'),
        path('update', views.update_profile, name='update_profile'),
        path('create', views.create_profile, name='create_profile'),

        #Gestion des membres
        path('create_member', views.create_member, name='create_member'),
        path('members', views.show_members, name='show_members'),

        #Annuaire
        path('users', views.show_profiles, name='show_profiles'),
        ]

        #The function static ensure that it only work when using DEBUG for
        #  production, an other method must be used to serve static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

