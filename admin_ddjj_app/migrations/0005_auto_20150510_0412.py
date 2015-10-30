# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ddjj_app', '0004_auto_20150509_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bien',
            name='valor_fiscal',
            field=models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
