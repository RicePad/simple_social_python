# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-10-20 00:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='groupmember',
            unique_together=set([('group', 'user')]),
        ),
    ]