from django.urls import re_path
from jembe import views

urlpatterns = [
    re_path(r'^$', views.home, name="home"),
    re_path(r'^reservation/$', views.NewReservation.as_view(), name="reservation"),
    re_path(r'^contact/$', views.Contact.as_view(), name="contact"),
    re_path(r'^payments/$', views.payment, name="payment"),
]
