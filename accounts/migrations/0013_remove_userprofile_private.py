# Generated by Django 2.2 on 2020-09-18 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200918_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='private',
        ),
    ]