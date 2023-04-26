from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework_nested.viewsets import NestedViewSetMixin

from src.apps.events.api.serializers import EventSerializer, EventDateSerializer
from src.apps.events.models import Event, EventDate


# class EventViewSet(ModelViewSet):
#     queryset = Event.objects.all()
#     action_serializers = {
#         "default": EventSerializer,
#     }


class EventViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDateViewSet(
    NestedViewSetMixin,
    ListModelMixin,
    RetrieveModelMixin,
    GenericViewSet,
):
    queryset = EventDate.objects.all()
    parent_lookup_kwargs = {"event_pk": "event"}
    serializer_class = EventDateSerializer
