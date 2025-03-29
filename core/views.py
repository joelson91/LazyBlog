from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'home/index.html', context=context)

def post(request, slug):
    post_content = Post.objects.get(slug=slug)
    context = {'post': post_content}
    return render(request, 'home/post.html', context=context)