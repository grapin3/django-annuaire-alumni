# Generated by Django 2.0.6 on 2018-08-28 15:26

import apps.annuaire.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('annuaire', '0003_auto_20180827_1606'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leisuretag',
            options={'verbose_name': 'leisure', 'verbose_name_plural': 'leisures'},
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ('lastname', 'firstname'), 'verbose_name': 'member', 'verbose_name_plural': 'members'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'profile', 'verbose_name_plural': 'profiles'},
        ),
        migrations.AlterField(
            model_name='member',
            name='expiration_date',
            field=models.DateField(default=apps.annuaire.models.one_year_delta, verbose_name='expiration date'),
        ),
        migrations.AlterField(
            model_name='member',
            name='firstname',
            field=models.CharField(max_length=30, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='member',
            name='lastname',
            field=models.CharField(max_length=30, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='member',
            name='registration_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='registration date'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='biography'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gap_year',
            field=models.BooleanField(default=False, verbose_name='gap year'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(0, 'male'), (1, 'female')], null=True, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='miscellaneous',
            field=models.TextField(blank=True, max_length=500, verbose_name='miscellaneous'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=apps.annuaire.models.avatar_directory_path, verbose_name='avatar'),
        ),
    ]