from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

from mywebsite.models import Gallery, Project


@receiver(post_save, sender=Project)
def create_gallery(sender, instance, created, **kwargs):
    print("from signal ", instance)
    if created:
        Gallery.objects.create(project=instance)
