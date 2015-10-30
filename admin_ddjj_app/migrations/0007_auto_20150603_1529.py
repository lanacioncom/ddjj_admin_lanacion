# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ddjj_app', '0006_auto_20150528_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='BienPersona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('porcentaje', models.DecimalField(help_text="<strong>NO</strong> incluir el signo '%'.<br> Si ingresa un n\xfamero decimal use '.' (punto) como delimitador", null=True, max_digits=10, decimal_places=2, blank=True)),
                ('vinculo', models.CharField(default='Titular', choices=[('Conviviente', 'Conviviente'), ('C\xf3nyuge', 'C\xf3nyuge'), ('Hijo/a', 'Hijo/a'), ('Titular', 'Titular')], max_length=255, blank=True, help_text='Indica la relacion con el titular de la DDJJ', verbose_name='v\xednculo con el declarante')),
                ('bien', models.ForeignKey(verbose_name='bien', to='admin_ddjj_app.Bien', help_text=None)),
                ('persona', models.ForeignKey(verbose_name='Titular adicional', to='admin_ddjj_app.Persona', help_text='Titular adicional')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='bien',
            options={'ordering': ['tipo_bien', 'nombre_bien'], 'verbose_name': 'Detalles del bien: ', 'verbose_name_plural': 'bienes'},
        ),
        migrations.AlterModelOptions(
            name='ddjjfamiliar',
            options={'ordering': ['persona__apellido'], 'verbose_name_plural': 'Familiares mencionados en esta ddjj'},
        ),
        migrations.AddField(
            model_name='bien',
            name='titulares',
            field=models.ManyToManyField(related_name='bienes', through='admin_ddjj_app.BienPersona', to='admin_ddjj_app.Persona'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cargo',
            name='poder_id',
            field=models.IntegerField(null=True, verbose_name='poder', choices=[(0, 'Ejecutivo'), (1, 'Legislativo'), (2, 'Judicial'), (3, 'No pertenece a ningun poder')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contenidoddjjs',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ddjj',
            name='familiares',
            field=models.ManyToManyField(to='admin_ddjj_app.Persona', verbose_name='familiares', through='admin_ddjj_app.DdjjFamiliar'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ddjj',
            name='poder_id',
            field=models.IntegerField(verbose_name='poder', choices=[(0, 'Ejecutivo'), (1, 'Legislativo'), (2, 'Judicial'), (3, 'No pertenece a ningun poder')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ddjjfamiliar',
            name='persona',
            field=models.ForeignKey(verbose_name='familiar', to='admin_ddjj_app.Persona'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ddjjfamiliar',
            name='vinculo',
            field=models.CharField(blank=True, help_text='Indica la relacion con el titular de la DDJJ', max_length=255, verbose_name='v\xednculo con el declarante', choices=[('Conviviente', 'Conviviente'), ('C\xf3nyuge', 'C\xf3nyuge'), ('Hijo/a', 'Hijo/a')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jurisdiccion',
            name='poder_id',
            field=models.IntegerField(null=True, verbose_name='poder', choices=[(0, 'Ejecutivo'), (1, 'Legislativo'), (2, 'Judicial'), (3, 'No pertenece a ningun poder')]),
            preserve_default=True,
        ),
    ]
