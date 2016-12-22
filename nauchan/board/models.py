from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Board(models.Model):
    short_name = models.CharField(max_length=4, unique=True, null=False,
                    blank=False, help_text=_('A brief alias of a board name'))
    full_name = models.CharField(max_length=50, unique=True, null=False,
                    blank=False, help_text=_('A board name'))

    def __str__(self):
        return self.short_name


class Thread(models.Model):
    board = models.ForeignKey(Board, verbose_name=_('Is part of a board:'),
                help_text=_('This thread is started as a stated board:'))
    is_open = models.BooleanField(verbose_name=_('Open for posting:'),
                help_text=_('This thread is open for posting:'),
                default=True)
    is_in_bumplimit = models.BooleanField(verbose_name=_('Is in bumplimit:'),
                help_text=_('If true, thread will not be bumped after post:'),
                default=False)

    def __str__(self):
        return str(self.id)


class Post(models.Model):
    thread = models.ForeignKey(Thread, verbose_name=_('Is posted in a thread:'),
                    help_text=_('This post is situated inside a thread:'),
                    related_name='posts')
    body = models.CharField(max_length=400, null=False, blank=False,
                    verbose_name=_('Post body:'),
                    help_text=_('Here stays a post body:'))
    signature = models.CharField(max_length=40, null=True, blank=True,
                    help_text=_('Field where author may state his (nick)name:'),
                    verbose_name=_('Post signature:'))
    topic = models.CharField(max_length=70, null=True, blank=True,
                    help_text=_('Field where author may state post topic:'),
                    verbose_name=_('Post topic:'))
    email = models.EmailField(null=True, blank=True,
                    help_text=_('Email address attached to this post:'),
                    verbose_name=_('Author email:'))
    posted_at = models.DateTimeField(verbose_name=_('posted at:'),
                    auto_now_add=True)

    def __str__(self):
        return str(self.id)
