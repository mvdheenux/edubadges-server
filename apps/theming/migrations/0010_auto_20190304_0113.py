# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-04 09:13
from __future__ import unicode_literals

from django.db import migrations

def migrate_them_to_badger_app(apps, schema_editor):
    Theme = apps.get_model('theming', 'Theme')
    BadgrApp = apps.get_model('mainsite', 'BadgrApp')

    for t in Theme.objects.all():
        url = t.site.domain
        if BadgrApp.objects.filter(cors=url).exists():
            badgr_app = BadgrApp.objects.get(cors=url)
            t.badgr_app = badgr_app
            t.save()



class Migration(migrations.Migration):

    dependencies = [
        ('theming', '0009_theme_badgr_app'),
    ]

    operations = [
        migrations.RunPython(migrate_them_to_badger_app, reverse_code=migrations.RunPython.noop)
    ]
