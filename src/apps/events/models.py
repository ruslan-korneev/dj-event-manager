from django.db import models

from src.apps.events.const import Currencies


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField()
    author = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="events"
    )


class EventDate(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=Currencies.choices)
    event = models.ForeignKey(
        "events.Event", on_delete=models.PROTECT, related_name="dates"
    )
    participants = models.ManyToManyField("users.User")
