from django.db import models
from region.models import Region
# Create your models here.


class Shrine(models.Model):
    name = models.CharField(max_length=250)
    descriptions = models.TextField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
