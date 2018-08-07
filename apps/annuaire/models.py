from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from os import path

from address.models import AddressField

import logging
logger= logging.getLogger(__name__)

def avatar_directory_path(instance, filename):
    return 'avatar/{0}{1}'.format(instance.user.username,
    path.splitext(filename)[1])

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #member = models.ForeignKey('Member', on_delete=models.CASCADE, blank=True)
    photo = models.ImageField(upload_to=avatar_directory_path,null=True, blank=True)
    address = AddressField(on_delete=models.CASCADE, blank=True, null=True)
    bio= models.TextField(max_length=500, null=True, blank=True)
    promo=models.IntegerField(null=True, blank=True)
    gap_year = models.BooleanField(default=False)
    miscellaneous = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username

class Member(models.Model):
    memberid = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=30, )
    lastname = models.CharField(max_length=30, )
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE,null=True, blank = True)
    def __str__(self):
        return self.firstname+" "+self.lastname

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        logger.info("Creating user for %s" % instance.username)
        Profile.objects.create(user=instance)
        logger.info("New profile created for %s" % instance.username)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    old_active = instance.is_active
    instance.is_active = False
    if (instance.is_superuser):
        instance.is_active = True
    try:
        instance.profile.member
        instance.is_active = True
    except:
        pass
    instance.profile.save()
    if (old_active != instance.is_active):
        instance.save()

@receiver(post_save, sender=Member)
def save_member_profile(sender, instance, **kwargs):
    try:
        instance.profile
        instance.profile.user.save()
    except:
        pass
