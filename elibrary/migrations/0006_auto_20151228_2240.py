# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elibrary', '0005_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='issuedTo',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='requestedBy',
            field=models.TextField(blank=True),
        ),
    ]
