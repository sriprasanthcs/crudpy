from django.db import models

# Create your models here.
class crudmysqldb(models.Model):
    sno = models.IntegerField()
    sname = models.CharField(max_length=20)
    semail = models.CharField(max_length=20)
    
class crudtb2(models.Model):
    snoid = models.IntegerField()
    snameid = models.IntegerField()
    semailid = models.IntegerField()