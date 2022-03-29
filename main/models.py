from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


# Create your models here.
class Population(models.Model):
    country = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    human_count = models.PositiveBigIntegerField()

def image_collection_path(instance, file_name):
    return f"image_collection/{file_name}"

class ImageCollection(models.Model):
    image = models.FileField(upload_to=image_collection_path)
    notes = models.TextField()


class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)