from django.contrib.auth.models import User
from django.contrib.gis.db import models

class restro(models.Model):
    name=models.CharField(max_length=100)
    mpoint=models.PointField(blank=True,null=True)
    lat=models.DecimalField(max_digits=10,decimal_places=6,blank=True,null=True)
    lon=models.DecimalField(max_digits=10,decimal_places=6, blank=True,null=True)
    user=models.ForeignKey('auth.User', related_name='restro')
    def save(self,*args,**kwargs):
        self.lat=self.mpoint.y
        self.lon=self.mpoint.x
        super(restro,self).save(*args,**kwargs)
    class Meta:
        ordering = ('name',)
