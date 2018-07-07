from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from os import path

import logging
logger= logging.getLogger(__name__)

def avatar_directory_path(instance, filename):
    return 'avatar/{0}{1}'.format(instance.user.username,
    path.splitext(filename)[1])

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    member = models.ForeignKey('Member', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.user.username

class Member(models.Model):
    memberid = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=30, )
    lastname = models.CharField(max_length=30, )
    photo = models.ImageField(upload_to=avatar_directory_path,null=True, blank=True)
    bio= models.TextField(max_length=500)
    promo=models.IntegerField(null=True)
    gap_year = models.BooleanField(default=False, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        logger.info("Creating user for %s" % instance.username)
        Profile.objects.create(user=instance)
        logger.info("New profile created for %s" % instance.username)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

