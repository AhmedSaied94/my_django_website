from rest_framework import viewsets
from rest_framework import generics

from .serializers import ProjectSerializer
from .models import Project

# Create your views here.


class ProjectView(viewsets.GenericViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Project.objects.filter(active=True).order_by("-date")
    serializer_class = ProjectSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
