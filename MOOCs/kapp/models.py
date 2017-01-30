# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Coursera(models.Model):
    title = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    inst = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coursera'


class Infy(models.Model):
    title = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    prof = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infy'


class Lynda(models.Model):
    title = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lynda'


class Nptel(models.Model):
    title = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    prof = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nptel'


class Udacity(models.Model):
    title = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    prof = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'udacity'
