# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ddjj_app', '0024_auto_20150713_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ddjj',
            name='obs',
            field=models.TextField(verbose_name='observaciones p\xfablicas', blank=True),
            preserve_default=True,
        ),
    ]
