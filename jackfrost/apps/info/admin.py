from django.contrib import admin
from .models import (Service, 
                    ServiceImage, 
                    Carousel, 
                    CarouselImage, 
                    Contact, 
                    Review
)


# Register your models here.

admin.site.register(Service)
admin.site.register(ServiceImage)
admin.site.register(Carousel)
admin.site.register(CarouselImage)
admin.site.register(Contact)
admin.site.register(Review)