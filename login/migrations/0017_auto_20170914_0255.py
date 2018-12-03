# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-14 02:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0016_auto_20170620_0508'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserComplaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=200)),
                ('location', models.CharField(default='Null', max_length=200)),
                ('Mobile_number', models.IntegerField(max_length=10)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
