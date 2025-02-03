from django.shortcuts import render
from django.views import generic
from django.conf import settings
from .models import CarouselImage, Staff, Product, DiveSite, Social, Contact
from .forms import ContactForm


class IndexView(generic.TemplateView):
    template_name = "mainapp/index.html"
    carousel_images = CarouselImage.objects.all()
    extra_context={'background_style': 'indexBody',
                   'carousel_images': carousel_images,
                   'viewname': 'index'}

class StaffView(generic.TemplateView):
    template_name = "mainapp/staff.html"
    staff = Staff.objects.all()
    extra_context={'background_style': 'otherBody',
                   'staff_members': staff,
                   'viewname': 'staff'}
    
class DiveSiteView(generic.TemplateView):
    template_name = "mainapp/divesites.html"
    divesites = DiveSite.objects.all()
    extra_context={'background_style': 'otherBody',
                   'divesites': divesites,
                   'viewname': 'divesites'}
    
class SocialsView(generic.TemplateView):
    template_name = "mainapp/socials.html"
    socials = Social.objects.all()
    extra_context={'background_style': 'otherBody',
                   'socials': socials,
                   'viewname': 'socials'}

class ContactFormCreateView(generic.edit.CreateView):
    form_class = ContactForm
    template_name = 'mainapp/contact.html'
    success_url = '/sent/'
    extra_context={'background_style': 'otherBody',
                'viewname': 'contact'}
    
class SentView(generic.TemplateView):
    template_name = "mainapp/message_sent.html"
    sent = Contact.objects.all()
    extra_context={'background_style': 'otherBody',
                   'sent': sent,
                   'viewname': 'sent'}

class ProductsView(generic.TemplateView):
    template_name = "mainapp/products.html"
    products = Product.objects.all()
    extra_context={'background_style': 'otherBody',
                   'products': products,
                   'viewname': 'products'}
