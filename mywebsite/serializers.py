from rest_framework import serializers
from mywebsite.models import Project, Skill, Gallery, Image


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = [
            "id",
            "name",
        ]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            "id",
            "image",
            "title",
            "description",
        ]


class GallerySerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = [
            "id",
            "images",
        ]

    def get_images(self, obj):
        images = obj.images.all().order_by("id")
        return ImageSerializer(images, many=True).data


class ProjectSerializer(serializers.ModelSerializer):
    date = serializers.DateField("%m %y")
    skills = SkillSerializer(many=True)
    gallery = GallerySerializer()

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "date",
            "desc",
            "skills",
            "main_preview",
            "gallery",
            "github_back_link",
            "github_front_link",
            "live_link",
        ]
