# Generated by Django 2.2 on 2020-09-18 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_userprofile_private'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='user_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rel_from_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
