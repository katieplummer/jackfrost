from django.shortcuts import render, reverse, redirect
from django.views.generic import View, ListView, DetailView, TemplateView, FormView
from .models import Carousel, CarouselImage, Service, ServiceImage, Contact
from .forms import ContactForm
from django.contrib import messages

from jackfrost.apps.blog.models import blog_preview
from jackfrost.apps.event.models import event_preview

# Create your views here

class AboutView(TemplateView):
    template_name = 'info/about.html'

def index_view(request):
    context = {
        'slides' : Carousel.objects.first().images,
        'articles' : blog_preview(),
        'events' : event_preview()
    }
    return render(request, "index.html", context)

class ServiceListView(ListView):
    model = Service
    template_name = "info/home2.html"
    context_object_name = "services"

class ServiceDetailView(DetailView):
    model = Service
    template_name = "info/service-detail.html"
    context_object_name = "service"

class CreateContactView(FormView):
    form_class = ContactForm
    template_name = 'info/contact.html'

    def form_valid(self, form):
        self.form = form
        return redirect(self.get_success_url())

    def get_success_url(self):
        self.form.save()
        sucess_message = 'Thank you {}. We will contact you ASAP.'.format(self.form.cleaned_data['name'])
        messages.success(self.request, sucess_message)
        return reverse('contact')
