# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ddjj_app', '0016_auto_20150610_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bien',
            name='m_mejoras_id',
            field=models.IntegerField(blank=True, null=True, choices=[(0, '$'), (1, 'us$'), (2, 'E'), (3, ' Uruguayos'), (4, '\xa3'), (5, 'A'), (6, 'A$'), (7, '$L'), (8, 'No especifica')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bien',
            name='m_valor_adq_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Moneda valor adquisici\xf3n', choices=[(0, '$'), (1, 'us$'), (2, 'E'), (3, ' Uruguayos'), (4, '\xa3'), (5, 'A'), (6, 'A$'), (7, '$L'), (8, 'No especifica')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bien',
            name='m_valor_fiscal_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Moneda Mejoras', choices=[(0, '$'), (1, 'us$'), (2, 'E'), (3, ' Uruguayos'), (4, '\xa3'), (5, 'A'), (6, 'A$'), (7, '$L'), (8, 'No especifica')]),
            preserve_default=True,
        ),
    ]
