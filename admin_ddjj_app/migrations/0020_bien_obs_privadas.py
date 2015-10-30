# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ddjj_app', '0019_auto_20150622_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='bien',
            name='obs_privadas',
            field=models.CharField(max_length=255, null=True, verbose_name='observaciones privadas', blank=True),
            preserve_default=True,
        ),
    ]
