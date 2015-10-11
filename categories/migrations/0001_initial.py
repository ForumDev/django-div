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
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(default=b'', max_length=15)),
                ('short_text', models.TextField(default=b'', max_length=70)),
                ('url', models.URLField(help_text=b'Link to an external page (will override page link)', null=True, blank=True)),
                ('image', models.ImageField(upload_to=b'images/cat/', verbose_name=b'Category image')),
                ('page', cms.models.fields.PageField(blank=True, to='cms.Page', help_text=b'Select an existing page to link to.', null=True, verbose_name=b'page')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CatSel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('cat', models.ForeignKey(to='categories.Category')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SubCat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(default=b'', max_length=15)),
                ('url', models.URLField(help_text=b'Link to an external page (will override page link)', null=True, blank=True)),
                ('image', models.ImageField(upload_to=b'images/scat/', verbose_name=b'SubCat image')),
                ('cat', models.ForeignKey(to='categories.Category')),
                ('page', cms.models.fields.PageField(blank=True, to='cms.Page', help_text=b'Select an existing page to link to.', null=True, verbose_name=b'page')),
            ],
            options={
                'verbose_name_plural': 'SubCategories',
            },
            bases=(models.Model,),
        ),
    ]
