# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-21 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0037_auto_20171221_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='userwificomplaint',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
