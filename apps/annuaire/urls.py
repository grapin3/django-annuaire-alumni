from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
        #Gestion des profiles utilisateurs
        path('accounts/myprofile', views.profile_display, name='display_profile'),
        path('accounts/update', views.profile_update, name='update_profile'),
        path('accounts/register', views.profile_register,
            name='register_profile'),
        path('accounts/delete', views.profile_delete, name="delete_profile"),

        #Gestion des membres
        path('create_member', views.member_register, name='create_member'),
        path('members', views.member_list, name='show_members'),

        #Annuaire
        path('users/list', views.profile_list, name='list_profiles'),
        path('user/<slug:username>', views.profile_display,
            name='display_profile'),
        ]

        #The function static ensure that it only work when using DEBUG for
        #  production, an other method must be used to serve static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

