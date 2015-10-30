# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ddjj_app', '0014_auto_20150608_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personacargo',
            name='egreso',
            field=models.DateField(help_text='DD/MM/AAAA', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personacargo',
            name='ingreso',
            field=models.DateField(help_text='DD/MM/AAAA', null=True, blank=True),
            preserve_default=True,
        ),
    ]
