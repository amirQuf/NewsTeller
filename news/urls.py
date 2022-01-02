from django.urls import path
from .views import NewsList

app_name = "news"
urlpatterns = [
    path('',NewsList.as_view, name="newsList"),
    
]