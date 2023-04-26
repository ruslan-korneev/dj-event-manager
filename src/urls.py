from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from src.apps.events.api.views import EventViewSet, EventDateViewSet

router = SimpleRouter()
router.register("events", EventViewSet)

event_router = NestedSimpleRouter(router, "events", lookup="event")
event_router.register("dates", EventDateViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api/v1/", include(event_router.urls)),
    path("api/v1/token/", include("src.apps.api_auth.urls")),
]
