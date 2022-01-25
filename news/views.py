from django.shortcuts import render
from .models import News ,Category ,Favcategory
from rest_framework.viewsets import ModelViewSet 
from .serializers import (
    NewsSerializer ,CategorySerializer ,FavcategorySerializer)

class NewsViewSet(ModelViewSet):
    queryset = News.objects.filter(status = 'P')
    serializer_class = NewsSerializer

class FavcategoryViewSet(ModelViewSet):
    queryset = Favcategory.objects.all()
    serializer_class = FavcategorySerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer