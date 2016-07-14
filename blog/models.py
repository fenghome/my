# coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):
    userid = models.AutoField(db_column='userId', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=50)  # Field name made lowercase.
    userpassword = models.CharField(db_column='userPassword', max_length=60)  # Field name made lowercase.

    class Meta:
        db_table = 'users'

class Articles(models.Model):
    articleid = models.IntegerField(db_column='articleId', primary_key=True)  # Field name made lowercase.
    articlename = models.CharField(db_column='articleName', max_length=100)  # Field name made lowercase.
    articleauther = models.CharField(db_column='articleAuther', max_length=50, blank=True, null=True)  # Field name made lowercase.
    articlepic = models.CharField(db_column='articlePic', max_length=200, blank=True, null=True)  # Field name made lowercase.
    articlecolumm = models.IntegerField(db_column='articleColumm')  # Field name made lowercase.
    articletime = models.DateField(db_column='articleTime')  # Field name made lowercase.

    class Meta:
        db_table = 'articles'


class Columns(models.Model):
    colid = models.AutoField(db_column='colId', primary_key=True)  # Field name made lowercase.
    colname = models.CharField(db_column='colName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'columns'

