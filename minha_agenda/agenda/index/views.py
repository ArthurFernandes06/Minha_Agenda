from django.shortcuts import render, get_object_or_404
from .forms import TopicForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Topic

def index_views(request):
    """Adiciona uma nova tarefa"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False) 
            new_topic.owner = request.user       
            new_topic.save()                    
            return HttpResponseRedirect(reverse('index'))
    topics = Topic.objects.filter(owner = request.user).order_by('date_added')

    context = {
        'form': form,
        'topics': topics,
    }
    return render(request,'index/index.html',context)

def topic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    context = {'topic': topic}

    if topic.owner != request.user:
        raise Http404

    return render(request, 'index/index.html',context)

def edit_topic(request, id):
    topic = get_object_or_404(Topic, id=id)  

    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('index'))

    else:
        form = TopicForm(instance=topic)  

    context = {'form': form, 'topic': topic}
    return render(request, 'index/edit_topic.html', context)


def delete_topic(request, id):
    topic = get_object_or_404(Topic, id=id)

    
    if topic.owner != request.user:
        return HttpResponseRedirect(reverse('index'))

    topic.delete()
    return HttpResponseRedirect(reverse('index'))