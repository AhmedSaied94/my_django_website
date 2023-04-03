from rest_framework.routers import DefaultRouter
from .views import ProjectView


router = DefaultRouter()

router.register(r"projects", ProjectView, basename="projects")
