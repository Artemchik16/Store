from django.shortcuts import HttpResponse, render
from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = "main/index.html"


class AboutPage(TemplateView):
    template_name = "main/about.html"
