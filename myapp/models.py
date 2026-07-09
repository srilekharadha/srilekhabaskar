from django.db import models

# Create your models here.
class datas(models.Model):
    pid=models.IntegerField()
    fname=models.CharField(max_length=20)
    files=models.FileField(upload_to='files/',blank=True,null=True)
    pimg=models.ImageField(upload_to='photo/',blank=True,null=True)
    def __str__(self):
        return self.fname
