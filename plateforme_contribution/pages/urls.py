from django.conf.urls import patterns, url
from pages import views

urlpatterns = patterns(
    '',
    url(
        r'^$',
        views.Home.as_view(),
        name='home'
    ),

    url(
        r'^login/$',
        'django.contrib.auth.views.login',
        name='login'
    ),

    url(
        r'^logout$',
        views.LogoutView.as_view(),
        name='logout'
    ),

    url(
        r'^contact/$',
        views.Contact.as_view(),
        name='contact'
    ),

    url(
        r'^calendar/$',
        views.Calendar.as_view(),
        name='calendar'
    ),
)
