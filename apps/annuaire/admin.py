from django.contrib import admin

from .models import Profile
from .models import Member

admin.site.register(Profile)

# Register your models here.
admin.site.register(Member)
