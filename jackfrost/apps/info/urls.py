from django.urls import path
from .views import ServiceListView, ServiceDetailView, AboutView, CreateContactView

urlpatterns = [
    path('', ServiceListView.as_view(), name="service"),
    path('<int:pk>/', ServiceDetailView.as_view(), name="service-detail"),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', CreateContactView.as_view(), name='contact')
]