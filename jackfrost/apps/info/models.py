from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title

    @property
    def images(self):
        return ServiceImage.objects.filter(service=self)


class ServiceImage(models.Model):
    image = models.ImageField(upload_to="service_images")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, default=None)

class Carousel(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)   

    @property
    def images(self):
        return CarouselImage.objects.filter(carousel=self)

class CarouselImage(models.Model):
    image = models.ImageField(upload_to="carousel_images")
    carousel = models.ForeignKey(Carousel, on_delete=models.CASCADE, default=None)
    heading = models.TextField()
    subheading = models.TextField()
    small = models.TextField(default=None, blank=True)

class Contact(models.Model):
    name = models.TextField(default=None, blank=True, null=True)
    email = models.TextField(default=None, blank=True, null=True)
    phone = models.TextField(default=None, blank=True, null=True)
    message = models.TextField(default=None, blank=True, null=True)
    address = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    name = models.TextField(default=None, blank=True, null=True)
    stars = models.FloatField(default=0.0, blank=True, null=True)
    date_posted = models.DateTimeField(default=None, blank=True, null=True)
    message = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name


