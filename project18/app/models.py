from django.db import models
class Capital(models.Model):
    capid=models.IntegerField()
    capname=models.CharField(max_length=100,primary_key=True)


class Country(models.Model):
    cid=models.IntegerField()
    cname=models.CharField(max_length=100)
    capname=models.OneToOneField(Capital,on_delete=models.CASCADE)