# Generated by Django 3.2.9 on 2022-11-04 04:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0002_cocoment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cocoment',
            new_name='Cocomment',
        ),
    ]
