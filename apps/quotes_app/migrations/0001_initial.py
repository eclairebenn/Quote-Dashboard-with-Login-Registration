# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-23 20:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('log_reg_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes_created', to='log_reg_app.User')),
                ('favorited_users', models.ManyToManyField(related_name='favorited_quotes', to='log_reg_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Quoter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='quote',
            name='quoter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes_said', to='quotes_app.Quoter'),
        ),
    ]
