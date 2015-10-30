# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ddjj_app', '0009_auto_20150603_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bien',
            name='direccion',
            field=models.CharField(max_length=255, verbose_name='Direcci\xf3n', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bien',
            name='m_valor_adq_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Moneda valor adquisici\xf3n', choices=[(0, '$'), (1, 'us$'), (2, 'E'), (3, '$ Uruguayos'), (4, '\xa3'), (5, 'A'), (6, 'A$'), (7, '$L')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bien',
            name='pais',
            field=models.CharField(max_length=255, verbose_name='Pa\xeds', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bien',
            name='unidad_medida_id',
            field=models.IntegerField(blank=True, help_text='Unidad de medida usada para la superficie', null=True, verbose_name='Unidad de medida', choices=[(0, 'm2'), (1, 'ha')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cargo',
            name='poder_id',
            field=models.IntegerField(null=True, verbose_name='poder', choices=[(0, 'Ejecutivo'), (1, 'Legislativo'), (2, 'Judicial'), (3, 'Otro')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ddjj',
            name='flag_presenta',
            field=models.IntegerField(default=1, help_text="<strong style='color:blue'>'Solo el PDF'</strong> Present\xf3 carta o documento distinto al formulario de DDJJ del Poder", verbose_name='carta de DDJJ', choices=[(0, 'Si'), (1, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ddjj',
            name='poder_id',
            field=models.IntegerField(verbose_name='poder', choices=[(0, 'Ejecutivo'), (1, 'Legislativo'), (2, 'Judicial'), (3, 'Otro')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jurisdiccion',
            name='poder_id',
            field=models.IntegerField(null=True, verbose_name='poder', choices=[(0, 'Ejecutivo'), (1, 'Legislativo'), (2, 'Judicial'), (3, 'Otro')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='persona',
            name='estado_civil_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Estado civil', choices=[(0, 'Casado/a'), (2, 'Divorciado/a'), (3, 'Separado'), (4, 'Soltero/a'), (5, 'U. Hecho'), (6, 'Viudo/a')]),
            preserve_default=True,
        ),
    ]
