# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ddjj_app', '0012_auto_20150608_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bien',
            name='m_mejoras_id',
            field=models.IntegerField(blank=True, null=True, choices=[(0, '$'), (1, 'us$'), (2, 'E'), (3, ' Uruguayos'), (4, '\xa3'), (5, 'A'), (6, 'A$'), (7, '$L')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bien',
            name='m_valor_adq_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Moneda valor adquisici\xf3n', choices=[(0, '$'), (1, 'us$'), (2, 'E'), (3, ' Uruguayos'), (4, '\xa3'), (5, 'A'), (6, 'A$'), (7, '$L')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bien',
            name='m_valor_fiscal_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='moneda valor fiscal', choices=[(0, '$'), (1, 'us$'), (2, 'E'), (3, ' Uruguayos'), (4, '\xa3'), (5, 'A'), (6, 'A$'), (7, '$L')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bien',
            name='vinculo',
            field=models.CharField(default='Titular', choices=[('Conviviente', 'Conviviente'), ('C\xf3nyuge', 'C\xf3nyuge'), ('Hijo/a', 'Hijo/a'), ('Titular', 'Titular'), ('Otro', 'Otro')], max_length=255, blank=True, help_text='Indica la relacion con el titular de la DDJJ', verbose_name='v\xednculo con el declarante'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bienpersona',
            name='vinculo',
            field=models.CharField(default='Titular', choices=[('Conviviente', 'Conviviente'), ('C\xf3nyuge', 'C\xf3nyuge'), ('Hijo/a', 'Hijo/a'), ('Titular', 'Titular'), ('Otro', 'Otro')], max_length=255, blank=True, help_text='Indica la relacion con el titular de la DDJJ', verbose_name='v\xednculo con el declarante'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ddjjfamiliar',
            name='vinculo',
            field=models.CharField(blank=True, help_text='Indica la relacion con el titular de la DDJJ', max_length=255, verbose_name='v\xednculo con el declarante', choices=[('Conviviente', 'Conviviente'), ('C\xf3nyuge', 'C\xf3nyuge'), ('Hijo/a', 'Hijo/a'), ('Otro', 'Otro')]),
            preserve_default=True,
        ),
    ]
