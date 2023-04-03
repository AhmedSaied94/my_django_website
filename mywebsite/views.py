from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ProjectSerializer
from .models import Project

# Create your views here.


class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-date')
    serializer_class = ProjectSerializer
