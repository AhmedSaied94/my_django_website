from rest_framework import serializers
from .models import *


class NewRepresent(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class ProjectSerializer(serializers.ModelSerializer):
    date = serializers.DateField('%m %y')
    skills = NewRepresent()
    gallery = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'date',
            'desc',
            'skills',
            'main_preview',
            'gallery',
        ]

    def get_gallery(self, obj):
        lista = []
        for img in obj.gallery.images.all():
            lista.append(img.image.url)
        return lista
