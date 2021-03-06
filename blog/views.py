from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.
def post_list(request):
    # Shows only 4 recently updated posts.
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:4]
    return render(request   , 'blog/post_list.html', {'posts':posts})
