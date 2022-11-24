from django.urls import path
from .views import scrape, news_list
urlpatterns = [
  path('scrape/', scrape, name="scrape"),
  path('newsviewers/', news_list, name="newsviewers"),
]