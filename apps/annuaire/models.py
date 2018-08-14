from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta


from os import path

import logging
logger= logging.getLogger(__name__)

def avatar_directory_path(instance, filename):
    return 'avatar/{0}{1}'.format(instance.user.username,
    path.splitext(filename)[1])

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Homme'), (GENDER_FEMALE, 'Femme')]
    gender = models.IntegerField("sexe", choices=GENDER_CHOICES, blank=True,
            null=True)

    photo = models.ImageField(upload_to=avatar_directory_path,null=True,
            blank=True)
    city = models.CharField("ville", max_length=500,blank=True, null=True)
    region = models.CharField("region", max_length=500, blank=True, null=True)
    country = models.CharField("pays", max_length=500, blank=True, null=True)
    bio= models.TextField("biographie", max_length=500, null=True, blank=True)
    promo=models.IntegerField("promotion", null=True, blank=True)
    gap_year = models.BooleanField("césure", default=False)
    miscellaneous = models.TextField("divers", max_length=500, blank=True)

    def __str__(self):
        return self.user.username

def one_year_delta():
    return timezone.now() + timedelta(days=365)

class Member(models.Model):
    memberid = models.AutoField(primary_key=True)
    firstname = models.CharField("prénom", max_length=30, )
    lastname = models.CharField("nom", max_length=30, )
    registration_date = models.DateField("date d'inscription",
            default=timezone.now)
    expiration_date = models.DateField("date d'expiration",
            default=one_year_delta)
    profile = models.OneToOneField(Profile,
            on_delete=models.SET_NULL,null=True, blank = True)

    # properties used to display a tick in the admin zone
    # We define the method
    def up_to_date_with_subscription(self):
        return self.expiration_date > timezone.now().date()
    # Register it as a boolean so that the admin API display it as a tick
    up_to_date_with_subscription.boolean = True
    # We define the name of it
    up_to_date_with_subscription.short_description = "À jour"

    class Meta:
        verbose_name = "membre"
        ordering = ('lastname', 'firstname')

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
    instance.profile.save()

@receiver(pre_save, sender=User)
def toggle_active_user(sender, instance, **kwargs):
    """ Activate or desactivate User depending if they have a Member linked

    A superuser is always active, even if he doesn't have a linked Member
    """
    if (instance.is_superuser):
        instance.is_active = True
    else :
        try:
            instance.profile.member
            instance.is_active = True
        except:
            instance.is_active = False
            
# ToDo: this needs to be rework with the link made on User not on Profile
@receiver(post_save, sender=Member)
def save_member_profile(sender, instance, **kwargs):
    try:
        instance.profile
        instance.profile.user.save()
    except:
        pass
