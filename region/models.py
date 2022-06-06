from django.db import models
from country.models import Country
# Create your models here.


class Region(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
