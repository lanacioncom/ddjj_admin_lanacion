# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ddjj_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='facebook',
            field=models.CharField(help_text='Facebook', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='persona',
            name='sitio_oficial',
            field=models.CharField(help_text='Sitio Oficial', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='persona',
            name='twitter',
            field=models.CharField(help_text='Twitter', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
