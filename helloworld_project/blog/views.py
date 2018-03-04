from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from .models import Blogger
from django.urls import reverse_lazy
# Create your views here.

class BlogListView(ListView):
    model = Blogger
    template_name = 'blog.html'
    fields=['title']

class BlogDetailView(DetailView):
    model = Blogger
    template_name = 'blog_details.html'
    context_object_name ='blog_value'

class BlogCreateView(CreateView):
    model = Blogger
    template_name = 'create_blog.html'
    fields='__all__'

class BlogUpdateView(UpdateView):
    model= Blogger
    template_name='blog_edit.html'
    fields=['title','body']

class BlogDeleteView(DeleteView):
    model = Blogger
    template_name='blog_delete.html'
    success_url = reverse_lazy('blog')
    context_object_name ='blog_value'
