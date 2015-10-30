# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ddjj_app', '0005_auto_20150510_0412'),
    ]

    operations = [
        migrations.CreateModel(
            name='DdjjFamiliar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vinculo', models.CharField(blank=True, help_text='Indica la relacion con el titular de la DDJJ', max_length=255, verbose_name='v\xednculo con el declarante', choices=[('Conviviente', 'Conviviente'), ('C\xf3nyuge', 'C\xf3nyuge'), ('Hijo/a', 'Hijo/a'), ('Titular', 'Titular')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ddjj', models.ForeignKey(to='admin_ddjj_app.Ddjj')),
                ('persona', models.ForeignKey(to='admin_ddjj_app.Persona')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ddjj',
            name='familiares',
            field=models.ManyToManyField(to='admin_ddjj_app.Persona', through='admin_ddjj_app.DdjjFamiliar'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bien',
            name='m_valor_fiscal_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='moneda valor fiscal', choices=[(0, '$'), (1, 'us$'), (2, 'E'), (3, '$ Uruguayos'), (4, '\xa3'), (5, 'A'), (6, 'A$'), (7, '$L')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bien',
            name='nombre_bien',
            field=models.ForeignKey(related_name='bienes', verbose_name='nombre del bien', to='admin_ddjj_app.NombreBien'),
            preserve_default=True,
        ),
        # migrations.DeleteModel(
        #     name='NombreBien',
        # ),
        migrations.CreateModel(
            name='NombreBien',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-nombre'],
                'db_table': 'nombre_biens',
                'managed': False,
                'verbose_name_plural': 'Nombre Bienes',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='bien',
            name='obs',
            field=models.CharField(max_length=255, verbose_name='observaciones', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bien',
            name='persona',
            field=models.ForeignKey(verbose_name='Titular del bien', to='admin_ddjj_app.Persona', help_text='Es el titular del bien, este puede ser distinto al titular de la DDJJ'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bien',
            name='tipo_bien',
            field=models.ForeignKey(related_name='bienes', verbose_name='tipo de bien', to='admin_ddjj_app.TipoBien'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bien',
            name='vinculo',
            field=models.CharField(default='Titular', choices=[('Conviviente', 'Conviviente'), ('C\xf3nyuge', 'C\xf3nyuge'), ('Hijo/a', 'Hijo/a'), ('Titular', 'Titular')], max_length=255, blank=True, help_text='Indica la relacion con el titular de la DDJJ', verbose_name='v\xednculo con el declarante'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cargo',
            name='personas',
            field=models.ManyToManyField(related_name='cargos', through='admin_ddjj_app.PersonaCargo', to='admin_ddjj_app.Persona'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cargo',
            name='poder_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='poder', choices=[(0, 'Ejecutivo'), (1, 'Legislativo'), (2, 'Judicial')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ddjj',
            name='ano',
            field=models.IntegerField(verbose_name='a\xf1o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ddjj',
            name='flag_presenta',
            field=models.IntegerField(default=1, choices=[(0, 'Si'), (1, 'No')], blank=True, help_text="<strong style='color:blue'>'Solo el PDF'</strong> Present\xf3 carta o documento distinto al formulario de DDJJ del Poder", null=True, verbose_name='carta de DDJJ'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ddjj',
            name='obs',
            field=models.TextField(verbose_name='observaciones', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ddjj',
            name='poder_id',
            field=models.IntegerField(verbose_name='poder', choices=[(0, 'Ejecutivo'), (1, 'Legislativo'), (2, 'Judicial')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ddjj',
            name='status',
            field=models.IntegerField(default=0, help_text='Indica si puede ser publicada', verbose_name='publicada?', choices=[(0, 'NO'), (1, 'SI')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ddjj',
            name='tipo_ddjj_id',
            field=models.IntegerField(verbose_name='tipo DDJJ', choices=[(0, 'alta'), (1, 'baja'), (2, 'inicial'), (3, 'anual')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ddjj',
            name='url',
            field=models.CharField(help_text='Url DocumentCloud', max_length=255, verbose_name='link al documento original', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jurisdiccion',
            name='poder_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='poder', choices=[(0, 'Ejecutivo'), (1, 'Legislativo'), (2, 'Judicial')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='persona',
            name='apellido',
            field=models.CharField(max_length=255, verbose_name='apellido/s'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='persona',
            name='documento',
            field=models.IntegerField(null=True, verbose_name='n\xfamero', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='persona',
            name='estado_civil_id',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'Casado/a'), (2, 'Divorciado/a'), (3, 'Separado'), (4, 'Soltero/a'), (5, 'U. Hecho'), (6, 'Viudo/a')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='persona',
            name='nacimento',
            field=models.DateField(null=True, verbose_name='fecha de nacimiento', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(max_length=255, verbose_name='nombre/s'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='persona',
            name='tipo_documento_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='tipo de documento', choices=[(0, 'DNI'), (1, 'LE'), (2, 'LC'), (3, 'PASAPORTE')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personacargo',
            name='jurisdiccion',
            field=models.ForeignKey(verbose_name='organismo', blank=True, to='admin_ddjj_app.Jurisdiccion', null=True),
            preserve_default=True,
        ),
    ]
