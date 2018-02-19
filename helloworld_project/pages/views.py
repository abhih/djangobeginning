from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

#def home_page_view(TemplateView):
class homePageView(TemplateView):
    template_name = 'home.html'
    # return HttpResponse('Hello world part1!')
class aboutPageView(TemplateView):
    template_name = 'about.html'