# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ddjj_app', '0013_auto_20150608_0940'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bien',
            options={'ordering': ['tipo_bien', 'nombre_bien'], 'verbose_name': 'bien', 'verbose_name_plural': 'bienes'},
        ),
        migrations.AlterField(
            model_name='ddjj',
            name='tipo_ddjj_id',
            field=models.IntegerField(verbose_name='tipo DDJJ', choices=[(0, 'Alta'), (1, 'Baja'), (2, 'Inicial'), (3, 'Anual')]),
            preserve_default=True,
        ),
    ]
