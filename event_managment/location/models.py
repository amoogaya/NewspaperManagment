from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class LocationIndexPage(Page):
    templates = "location/location_index_page.html"

    country_name = models.CharField(max_length=200)

    content_panels = Page.content_panels + [
        FieldPanel("country_name", classname="full"),
    ]

    class Meta:

        verbose_name = "Country"
        verbose_name_plural = "Countries"


class LocationPage(Page):
    templates = "location/location_page.html"

    name = models.CharField(max_length=200)
    brief_description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("name", classname="full"),
        FieldPanel("brief_description", classname="full"),
    ]

    class Meta:

        verbose_name = "Location"
        verbose_name_plural = "Locations"


class EventPage(Page):
    #template = "location/event_page.html"

    location = ParentalKey(LocationPage, on_delete=models.CASCADE, related_name='The_events')
    name = models.CharField(max_length=200)
    date = models.DateField("Event date")
    duration = models.IntegerField()
    description = RichTextField(blank=False)

    content_panels = Page.content_panels + [
        FieldPanel("location"),
        FieldPanel("name"),
        FieldPanel("date"),
        FieldPanel("duration"),
        FieldPanel("description"),
    ]
