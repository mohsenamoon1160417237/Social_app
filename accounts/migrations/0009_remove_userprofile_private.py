# Generated by Django 2.2 on 2020-09-18 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_userprofile_private'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='private',
        ),
    ]
