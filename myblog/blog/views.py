from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import title


from blog.models import Post


def post(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})

def detail(request, post_id):
    posts = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'posts': posts})