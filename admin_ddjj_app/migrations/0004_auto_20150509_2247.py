# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ddjj_app', '0003_tipobien_clasificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='sexo_id',
            field=models.IntegerField(default=0, verbose_name='sexo', choices=[(0, 'M'), (1, 'F')]),
            preserve_default=False,
        ),
    ]
