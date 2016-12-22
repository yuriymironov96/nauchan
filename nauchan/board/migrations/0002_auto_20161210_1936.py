# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.CharField(default='test', help_text='Here stays a post body:', max_length=400, verbose_name='Post body:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.EmailField(blank=True, help_text='Email address attached to this post:', max_length=254, null=True, verbose_name='Author email:'),
        ),
        migrations.AlterField(
            model_name='post',
            name='signature',
            field=models.CharField(blank=True, help_text='Field where author may state his (nick)name:', max_length=40, null=True, verbose_name='Post signature:'),
        ),
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.CharField(blank=True, help_text='Field where author may state post topic:', max_length=70, null=True, verbose_name='Post topic:'),
        ),
    ]
