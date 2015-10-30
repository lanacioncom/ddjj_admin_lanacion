# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ddjj_app', '0018_auto_20150622_0901'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jurisdiccion',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Jurisdicciones'},
        ),
    ]
