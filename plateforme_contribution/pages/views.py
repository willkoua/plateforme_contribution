# coding: utf-8

from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages


class Home(generic.TemplateView):
    template_name = 'pages/home.html'


class Contact(generic.TemplateView):
    template_name = 'pages/contact.html'


class Calendar(generic.TemplateView):
    template_name = 'pages/calendar.html'


class Settlement(generic.TemplateView):
    template_name = 'pages/settlement.html'


class LogoutView(generic.RedirectView):

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(
            request,
            messages.WARNING,
            'Vous avez été déconnecté!'
        )

        return redirect(self.get_redirect_url(*args, **kwargs))

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy(
            "pages:home"
        )
