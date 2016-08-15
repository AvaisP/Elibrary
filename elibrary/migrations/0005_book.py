# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elibrary', '0004_auto_20151228_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookName', models.CharField(max_length=400)),
                ('author', models.CharField(max_length=200)),
                ('copies', models.IntegerField(default=1)),
                ('issuedTo', models.TextField()),
                ('requestedBy', models.TextField()),
            ],
        ),
    ]
