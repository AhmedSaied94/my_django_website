from mywebsite.models import Project, Gallery
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=Project)
def create_gallery(sender, instance, created, **kwargs):
    if created:
        Gallery.objects.create(project=instance)
