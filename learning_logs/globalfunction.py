import re
from django.http import Http404
from .models import Topic

def check_topic_owner(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404