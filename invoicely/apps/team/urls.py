from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import Teamviewsets

router = DefaultRouter()
router.register("teams", Teamviewsets, basename="teams")

urlpatterns = [
    path('', include(router.urls)),
]