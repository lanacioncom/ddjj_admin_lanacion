# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ddjj_app', '0007_auto_20150603_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bien',
            name='titulares',
            field=models.ManyToManyField(related_name='bienese', through='admin_ddjj_app.BienPersona', to='admin_ddjj_app.Persona'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bienpersona',
            name='bien',
            field=models.ForeignKey(to='admin_ddjj_app.Bien'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bienpersona',
            name='persona',
            field=models.ForeignKey(to='admin_ddjj_app.Persona'),
            preserve_default=True,
        ),
    ]
