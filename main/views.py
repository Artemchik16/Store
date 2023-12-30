from django.shortcuts import HttpResponse, render
from django.views.generic import ListView, TemplateView

from goods import models as goods_models


class MainPage(TemplateView):
    template_name = "main/index.html"


class AboutPage(TemplateView):
    template_name = "main/about.html"
