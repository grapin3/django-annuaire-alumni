# Generated by Django 2.0.6 on 2018-08-27 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annuaire', '0002_auto_20180820_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeisureTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=25, verbose_name='tag')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='leisure',
            field=models.ManyToManyField(blank=True, to='annuaire.LeisureTag'),
        ),
    ]
