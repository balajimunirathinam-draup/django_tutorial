from main.models import ImageCollection
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


@receiver(post_save, sender=ImageCollection)
def watch_image_collection(*args, **kwargs):
    print("image stored")