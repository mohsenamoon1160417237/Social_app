# Generated by Django 2.2 on 2020-09-12 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20200912_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='image',
            unique_together=set(),
        ),
    ]
