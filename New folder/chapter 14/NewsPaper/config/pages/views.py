from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


from django.shortcuts import render

# Create your views here.
