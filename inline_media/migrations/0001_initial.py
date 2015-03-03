# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import django.core.files.storage
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('link', models.URLField(unique=True)),
                ('tags', tagging.fields.TagField(default=b'', help_text='i.e: creativecommons, comercial, non-commercial, ...', max_length=255, blank=True)),
            ],
            options={
                'db_table': 'inline_media_licenses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('picture', sorl.thumbnail.fields.ImageField(storage=django.core.files.storage.FileSystemStorage(b'/home/kuba/dev/mvne_platform/src/mvno/mobile_vikings/media/mvvs', b'/media-2015.01.30.7ddf96e/mvvs/'), upload_to='pictures/%Y/%b/%d')),
                ('show_as_link', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True)),
                ('show_description_inline', models.BooleanField(default=True, verbose_name='Show description inline')),
                ('author', models.CharField(help_text="picture's author", max_length=255, blank=True)),
                ('show_author', models.BooleanField(default=False)),
                ('show_license', models.BooleanField(default=False)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('sha1', models.CharField(default='', max_length=40, db_index=True, blank=True)),
                ('tags', tagging.fields.TagField(default=b'', help_text='i.e: logo, photo, country, season, ...', max_length=255, blank=True)),
                ('license', models.ForeignKey(blank=True, to='inline_media.License', null=True)),
            ],
            options={
                'ordering': ('-uploaded',),
                'db_table': 'inline_media_pictures',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PictureSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text="Visible at the top of the gallery slider that shows up when clicking on cover's picture.", max_length=255)),
                ('slug', models.SlugField()),
                ('description', models.TextField(help_text='Only visible in the inline under sizes small, medium, large or full.', blank=True)),
                ('show_description_inline', models.BooleanField(default=True)),
                ('order', models.CommaSeparatedIntegerField(help_text='Establish pictures order by typing the comma separated list of their picture IDs.', max_length=512, blank=True)),
                ('show_counter', models.BooleanField(default=False, help_text='Whether to show how many pictures contains the pictureset.')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('tags', tagging.fields.TagField(default=b'', help_text='i.e: exposition, holidays, party, ...', max_length=255, blank=True)),
                ('pictures', models.ManyToManyField(related_name='picture_sets', to='inline_media.Picture')),
            ],
            options={
                'db_table': 'inline_media_picture_sets',
            },
            bases=(models.Model,),
        ),
    ]
