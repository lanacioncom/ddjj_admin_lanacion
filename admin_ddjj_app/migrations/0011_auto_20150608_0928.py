# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ddjj_app', '0010_auto_20150608_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ddjj',
            name='poder_id',
            field=models.IntegerField(default=0, verbose_name='poder', choices=[(0, 'Ejecutivo'), (1, 'Legislativo'), (2, 'Judicial'), (3, 'Otro')]),
            preserve_default=True,
        ),
    ]
