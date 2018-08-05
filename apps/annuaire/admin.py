from django.contrib import admin

from .models import Profile
from .models import Member

# Register your models here.
admin.site.register(Profile)
admin.site.register(Member)
