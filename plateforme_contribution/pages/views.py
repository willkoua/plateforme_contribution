from django.views import generic


class Home(generic.TemplateView):
    template_name = 'pages/home.html'


class Contact(generic.TemplateView):
    template_name = 'pages/contact.html'
