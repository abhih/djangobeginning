from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView


# Create your views here.

#def home_page_view(TemplateView):
#class homePageView(TemplateView):
from .models import Post


class homePageView(ListView):
    model = Post
    template_name = 'home.html'
    # return HttpResponse('Hello world part1!')
#class aboutPageView(TemplateView):
class aboutPageView(ListView):
    model = Post
    template_name = 'about.html'
#class adminPageView(TemplateView):
class adminPageView(ListView):
    model = Post
    template_name = 'adminPage.html'