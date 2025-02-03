from django.urls import path
from django.conf import settings

from . import views

appname = "mainapp"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("contact/", views.ContactFormCreateView.as_view(), name="contact"),
    path("sent/", views.SentView.as_view(), name="sent"),
    path("divesites/", views.DiveSiteView.as_view(), name="divesites"),
    path("products/", views.ProductsView.as_view(), name="products"),
    path("socials/", views.SocialsView.as_view(), name="socials"),
    path("staff/", views.StaffView.as_view(), name="staff"),
]