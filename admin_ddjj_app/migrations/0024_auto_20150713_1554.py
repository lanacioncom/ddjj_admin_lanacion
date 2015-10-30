# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ddjj_app', '0023_auto_20150706_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bien',
            name='persona',
            field=models.ForeignKey(blank=True, to='admin_ddjj_app.Persona', help_text='Es el titular del bien, este puede ser distinto al titular de la DDJJ', null=True, verbose_name='Titular del bien'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bien',
            name='vinculo',
            field=models.CharField(default='Titular', help_text='Indica la relacion con el titular de la DDJJ', max_length=255, verbose_name='v\xednculo con el declarante', choices=[('Conviviente', 'Conviviente'), ('C\xf3nyuge', 'C\xf3nyuge'), ('Hijo/a', 'Hijo/a'), ('Titular', 'Titular'), ('Otro', 'Otro')]),
            preserve_default=True,
        ),
    ]
