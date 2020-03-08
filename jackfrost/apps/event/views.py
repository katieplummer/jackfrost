from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from .models import Event, EventImage

# Create your views here.

class EventListView(ListView):
    model = Event
    template_name = "event/event.html"
    context_object_name = "events"

class EventDetailView(DetailView):
    model = Event
    template_name = "event/event-post.html"
    context_object_name = "event"
