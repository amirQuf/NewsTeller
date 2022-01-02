from django.shortcuts import render
from django.views.generic import ListView
from .models import News

class NewsList(ListView):
    model = News
    context_object_name = 'news'
    template_name='news/index.html'
    
