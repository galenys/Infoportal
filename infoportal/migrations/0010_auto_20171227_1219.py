# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-27 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoportal', '0009_auto_20171208_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(),
        ),
    ]
