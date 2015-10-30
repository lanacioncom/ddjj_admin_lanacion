# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ddjj_app', '0017_auto_20150614_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bien',
            name='superficie',
            field=models.DecimalField(help_text="Superficie de la propiedad <br> Si ingresa un n\xfamero decimal use '.' (punto) como delimitador", null=True, max_digits=10, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
