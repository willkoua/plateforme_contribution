from django.conf.urls import patterns, url
from pages import views

urlpatterns = patterns(
    '',
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^contact/$', views.Contact.as_view(), name='contact'),
)
