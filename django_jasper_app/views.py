from django.shortcuts import render
from .models import Topic, Entry

# Create your views here.

def index(request):
    return render(request,'index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)

def entries(request):
    entries = Entry.objects.order_by('id')
    context = {'entries': entries}
    return render(request, 'entries.html', context)