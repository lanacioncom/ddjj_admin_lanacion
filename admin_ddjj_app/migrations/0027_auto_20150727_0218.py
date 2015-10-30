# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ddjj_app', '0026_auto_20150716_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ddjjfamiliar',
            name='persona',
            field=models.ForeignKey(verbose_name='familiar', blank=True, to='admin_ddjj_app.Persona', null=True),
            preserve_default=True,
        ),
    ]
