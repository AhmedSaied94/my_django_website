from datetime import date
from unicodedata import name
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    skills = models.ManyToManyField('Skill', related_name='projects')
    main_preview = models.ImageField(
        null=True, blank=True, upload_to='projects/main_preview')
    date = models.DateField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            this = Project.objects.get(id=self.id)
            if this.main_preview:
                this.main_preview.delete()
        except ObjectDoesNotExist:
            pass
        super(Project).save(self, *args, **kwargs)


class Image(models.Model):
    image = models.ImageField(upload_to='projects/images')
    gallery = models.ForeignKey(
        'gallery', related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.image.name


class Gallery(models.Model):
    project = models.OneToOneField(
        'Project', related_name='gallery', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.project.title} gallery'
