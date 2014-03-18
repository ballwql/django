from django.db import models
from django.contrib.auth.models import User

class Manager(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70)
    def __unicode__(self):
        return self.last_name + self.first_name

class Dba(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70)
    def __unicode__(self):
        return self.last_name + self.first_name

class State(models.Model):
    id = models.AutoField(primary_key=True)
    statename = models.CharField(max_length=20)
    def __unicode__(self):
        return self.statename

class Database(models.Model):
    id = models.AutoField(primary_key=True)
    databasename = models.CharField(max_length=30)
    databaseip = models.CharField(max_length=30)
    def __unicode__(self):
        return self.databasename + ' - ' + self.databaseip

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    creater = models.ForeignKey(User)
    manager = models.ForeignKey(Manager)
    dba = models.ForeignKey(Dba)
    state = models.ForeignKey(State)
    databases = models.ManyToManyField(Database)
    sql = models.CharField(max_length=2000,blank=True,null=True)
    desc = models.CharField(max_length=2000,blank=True, null=True)
    createdtime = models.DateTimeField()
    lastupdatedtime = models.DateTimeField(blank=True,null=True)
    dbacomment = models.CharField(max_length=2000,blank=True,null=True)
    attachment = models.FileField(upload_to='tasks',blank=True,null=True)
    def __unicode__(self):
        return str(self.id)