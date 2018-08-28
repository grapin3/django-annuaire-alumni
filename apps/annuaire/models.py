from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save, post_init
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta

from django.utils.translation import gettext_lazy as _

from os import path

import logging
logger= logging.getLogger(__name__)

def avatar_directory_path(instance, filename):
    return 'avatar/{0}{1}'.format(instance.user.username,
    path.splitext(filename)[1])

class LeisureTag(models.Model):

    """Docstring for LeisureTag. """
    #ToDo: ensure that the value are actually 25 char max
    tag = models.CharField('tag', max_length=25)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = _("leisure")
        verbose_name_plural = _('leisures')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    GENDER_MALE = 0
    GENDER_FEMALE = 1
    # Translators: Gender choice descripition
    GENDER_CHOICES = [(GENDER_MALE, _('male')), (GENDER_FEMALE, _('female'))]
    # Translators: Gender field label
    gender = models.IntegerField(_("gender"), choices=GENDER_CHOICES, blank=True,
            null=True)

    # Translators: Avatar field label
    photo = models.ImageField(_("avatar"), upload_to=avatar_directory_path,null=True,
            blank=True)
    city = models.CharField(_("city"), max_length=500,blank=True, null=True)
    region = models.CharField(_("region"), max_length=500, blank=True, null=True)
    country = models.CharField(_("country"), max_length=500, blank=True, null=True)
    bio= models.TextField(_("biography"), max_length=500, null=True, blank=True)
    promo=models.IntegerField("promotion", null=True, blank=True)
    gap_year = models.BooleanField(_("gap year"), default=False)
    miscellaneous = models.TextField(_("miscellaneous"), max_length=500, blank=True)
    leisure = models.ManyToManyField(LeisureTag, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        logger.info("User %s has been created", instance.username)
        Profile.objects.create(user=instance)
        logger.info("Profile %s has been created", instance.username)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

def one_year_delta():
    return timezone.now() + timedelta(days=365)

class Member(models.Model):
    memberid = models.AutoField(primary_key=True)
    firstname = models.CharField(_('first name'), max_length=30, )
    lastname = models.CharField(_('last name'), max_length=30, )
    registration_date = models.DateField(_("registration date"),
            default=timezone.now)
    expiration_date = models.DateField(_("expiration date"),
            default=one_year_delta)
    user = models.OneToOneField(User,
            on_delete=models.SET_NULL,null=True, blank = True)
    original_user_id = None

    # properties used to display a tick in the admin zone
    # We define the method
    def up_to_date_with_subscription(self):
        return self.expiration_date > timezone.now().date()
    # Register it as a boolean so that the admin API display it as a tick
    up_to_date_with_subscription.boolean = True
    # We define the name of it
    up_to_date_with_subscription.short_description = _("up to date")

    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')
        ordering = ('lastname', 'firstname')

    def __str__(self):
        return self.firstname+" "+self.lastname

# The next two function are used to create a memory in order to know if the
# user field changed. And if so it triggers a save() on the relevant User to
# activate or desactivate them
@receiver( post_init, sender=Member)
def set_original_user_id_id(sender, instance, **kwargs):
    instance.original_user_id = instance.user_id

@receiver( post_save, sender=Member)
def check_for_new_user(sender, instance, **kwargs):
    if instance.original_user_id != instance.user_id:
        if instance.original_user_id:
            User.objects.get(pk=instance.original_user_id).save()
        if instance.user:
            instance.user.save()
    instance.original_user_id = instance.user_id

@receiver(pre_save, sender=User)
def toggle_active_user(sender, instance, **kwargs):
    """ Activate or desactivate User depending if they have a Member linked

    A superuser is always active, even if he doesn't have a linked Member
    """
    if (instance.is_superuser):
        instance.is_active = True
    else :
        try:
            instance.member
            if not instance.is_active:
                instance.is_active = True
            logger.info("User %s has been activated", instance.username)
        except:
            if instance.is_active:
                instance.is_active = False
            logger.info("User %s has been deactivated", instance.username)
