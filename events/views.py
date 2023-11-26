from django.shortcuts import render
from django.views.generic import ListView
from .models import Event, News


class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    paginate_by = 9
    ordering = ['-date']
    

class NewsListView(ListView):
    model = News
    template_name = 'events/news_list.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 9
    

