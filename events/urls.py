from django.urls import path
from .views import EventListView, NewsListView

urlpatterns = [
    path('events/', EventListView.as_view(), name='event_list'),
    path('news/', NewsListView.as_view(), name='news_list'),
]
