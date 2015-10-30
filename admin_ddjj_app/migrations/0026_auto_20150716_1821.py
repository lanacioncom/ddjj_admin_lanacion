# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ddjj_app', '0025_auto_20150715_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bienpersona',
            name='persona',
            field=models.ForeignKey(blank=True, to='admin_ddjj_app.Persona', null=True),
            preserve_default=True,
        ),
    ]
