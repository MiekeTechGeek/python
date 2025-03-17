from django.shortcuts import render, get_object_or_404

from .models import Topic

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic_detail(request, topic_id):
    Topic = get_object_or_404(Topic, id=topic_id)
    return render(request, 'topics/detail.html', {'topic': Topic})
