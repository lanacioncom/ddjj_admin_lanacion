# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ddjj_app', '0008_auto_20150603_1611'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bienpersona',
            options={'ordering': ['persona__apellido'], 'verbose_name_plural': 'Titulares extras para este bien'},
        ),
    ]
