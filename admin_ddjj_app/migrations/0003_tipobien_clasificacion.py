# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ddjj_app', '0002_auto_20150428_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipobien',
            name='clasificacion',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'Rodados'), (1, 'Bonos, t\xedtulos y acciones'), (2, 'Inmuebles')]),
            preserve_default=True,
        ),
    ]
