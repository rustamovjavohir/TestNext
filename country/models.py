from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=250)
    descriptions = models.TextField()
    population = models.IntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

