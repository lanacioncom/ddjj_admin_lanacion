# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ddjj_app', '0021_auto_20150622_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ddjj',
            name='obs_privadas',
            field=models.TextField(max_length=255, null=True, verbose_name='observaciones privadas', blank=True),
            preserve_default=True,
        ),
    ]
