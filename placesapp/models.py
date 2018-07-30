from django.contrib.gis.db import models
from taggit.managers import TaggableManager


class Place(models.Model):
    title = models.CharField(max_length=50)
    location = models.PointField()
    desc = models.TextField()
    address = models.CharField(max_lenght=200)
    phone = models.IntegerField()
    city = models.CharField(max_length=50)
    tags = TaggableManager()
