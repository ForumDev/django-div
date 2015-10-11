# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(default=b'', max_length=15)),
                ('url', models.URLField(help_text=b'Link to an external page (will override page link)', null=True, blank=True)),
                ('image', models.ImageField(upload_to=b'images/box/', verbose_name=b'Box image')),
                ('page', cms.models.fields.PageField(blank=True, to='cms.Page', help_text=b'Select an existing page to link to.', null=True, verbose_name=b'page')),
            ],
            options={
                'verbose_name_plural': 'Boxes',
            },
            bases=(models.Model,),
        ),
    ]
