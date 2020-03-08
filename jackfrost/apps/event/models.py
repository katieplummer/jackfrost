from django.db import models
import time

# Create your models here.
class Event(models.Model):
    title = models.TextField()
    description = models.TextField()
    location = models.TextField()
    date = models.DateTimeField(default=None, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def images(self):
        return EventImage.objects.filter(event=self)

    @property
    def first_image(self):
        return self.images.first()
    
    @property
    def preview(self):
        return self.description[0:250]

    @property
    def created_at(self):
        return self.timestamp.strftime("%B") + ' ' + self.timestamp.strftime("%d") + ", " + self.timestamp.strftime("%Y")

    class Meta:
        ordering = ['-date']

class EventImage(models.Model):
    caption = models.TextField(default=None, null=True, blank=True)
    image = models.ImageField(upload_to="event_images/")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=None)

# get last 3 articles for blog preview on home page

def event_preview():
    return reversed(Event.objects.all()[2:])