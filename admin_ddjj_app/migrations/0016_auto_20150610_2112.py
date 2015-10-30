# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ddjj_app', '0015_auto_20150608_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ddjj',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creaci\xf3n'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ddjj',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificaci\xf3n'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='persona',
            name='ficha_d_l',
            field=models.CharField(default=None, max_length=255, null=True, help_text='Url ficha de Directorio Legislativo', blank=True),
            preserve_default=True,
        ),
    ]
