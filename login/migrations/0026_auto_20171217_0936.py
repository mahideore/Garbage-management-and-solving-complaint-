# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-17 09:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0025_auto_20171216_1040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='civilcomplaintdetails',
            old_name='location',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='civilcomplaintdetails',
            old_name='Mobile_number',
            new_name='user_Mobile_number',
        ),
        migrations.RenameField(
            model_name='civilcomplaintdetails',
            old_name='complaint',
            new_name='user_complaint',
        ),
        migrations.RenameField(
            model_name='electriccomplaintdetails',
            old_name='location',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='electriccomplaintdetails',
            old_name='Mobile_number',
            new_name='user_Mobile_number',
        ),
        migrations.RenameField(
            model_name='electriccomplaintdetails',
            old_name='complaint',
            new_name='user_complaint',
        ),
        migrations.RenameField(
            model_name='othercomplaintdetails',
            old_name='location',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='othercomplaintdetails',
            old_name='Mobile_number',
            new_name='user_Mobile_number',
        ),
        migrations.RenameField(
            model_name='othercomplaintdetails',
            old_name='complaint',
            new_name='user_complaint',
        ),
        migrations.RemoveField(
            model_name='civilcomplaintdetails',
            name='WifiComplaintWorker',
        ),
        migrations.RemoveField(
            model_name='electriccomplaintdetails',
            name='WifiComplaintWorker',
        ),
        migrations.RemoveField(
            model_name='othercomplaintdetails',
            name='WifiComplaintWorker',
        ),
        migrations.AddField(
            model_name='civilcomplaintdetails',
            name='CivilComplaintWorker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.CivilComplaintWorker'),
        ),
        migrations.AddField(
            model_name='civilcomplaintdetails',
            name='user_location',
            field=models.CharField(default='Null', max_length=200),
        ),
        migrations.AddField(
            model_name='civilcomplaintdetails',
            name='worker_name',
            field=models.CharField(default='Null', max_length=200),
        ),
        migrations.AddField(
            model_name='electriccomplaintdetails',
            name='ElectricComplaintWorker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.ElectricComplaintWorker'),
        ),
        migrations.AddField(
            model_name='electriccomplaintdetails',
            name='user_location',
            field=models.CharField(default='Null', max_length=200),
        ),
        migrations.AddField(
            model_name='electriccomplaintdetails',
            name='worker_name',
            field=models.CharField(default='Null', max_length=200),
        ),
        migrations.AddField(
            model_name='othercomplaintdetails',
            name='OtherComplaintWorker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.OtherComplaintWorker'),
        ),
        migrations.AddField(
            model_name='othercomplaintdetails',
            name='user_location',
            field=models.CharField(default='Null', max_length=200),
        ),
        migrations.AddField(
            model_name='othercomplaintdetails',
            name='worker_name',
            field=models.CharField(default='Null', max_length=200),
        ),
        migrations.AlterField(
            model_name='civilcomplaintdetails',
            name='first_name',
            field=models.CharField(default='some string', max_length=200),
        ),
        migrations.AlterField(
            model_name='electriccomplaintdetails',
            name='first_name',
            field=models.CharField(default='some string', max_length=200),
        ),
        migrations.AlterField(
            model_name='othercomplaintdetails',
            name='first_name',
            field=models.CharField(default='some string', max_length=200),
        ),
    ]
