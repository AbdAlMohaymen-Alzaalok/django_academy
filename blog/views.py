from django.shortcuts import render
from django.views.generic import ListView,DetailView
from . import models

class ListBlogs(ListView):
    model=models.Blog
    template_name = 'blog_list.html'

class Show_Blog(DetailView):
    model = models.Blog
    template_name = 'blog/show_blog.html'