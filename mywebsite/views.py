from rest_framework import viewsets

from .models import Project
from .serializers import ProjectSerializer

# Create your views here.


class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by("-date")
    serializer_class = ProjectSerializer
