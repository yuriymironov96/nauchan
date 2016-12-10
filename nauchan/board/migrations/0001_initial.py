# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 00:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(help_text='A brief alias of a board name', max_length=4, unique=True)),
                ('full_name', models.CharField(help_text='A board name', max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', models.CharField(blank=True, help_text='Field where author may state his (nick)name:', max_length=40, null=True)),
                ('topic', models.CharField(blank=True, help_text='Field where author may state post topic:', max_length=70, null=True)),
                ('email', models.EmailField(blank=True, help_text='Email address attached to this post:', max_length=254, null=True)),
                ('posted_at', models.DateTimeField(auto_now_add=True, verbose_name='posted at:')),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_open', models.BooleanField(default=True, help_text='This thread is open for posting:', verbose_name='Open for posting:')),
                ('is_in_bumplimit', models.BooleanField(default=False, help_text='If true, thread will not be bumped after post:', verbose_name='Is in bumplimit:')),
                ('board', models.ForeignKey(help_text='This thread is started as a stated board:', on_delete=django.db.models.deletion.CASCADE, to='board.Board', verbose_name='Is part of a board:')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(help_text='This post is situated inside a thread:', on_delete=django.db.models.deletion.CASCADE, to='board.Thread', verbose_name='Is posted in a thread:'),
        ),
    ]