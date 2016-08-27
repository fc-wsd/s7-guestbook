from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


def toppage(request):
    posts = Post.objects.all().order_by('-created_at')
    ctx = {
        'posts': posts,
    }
    return render(request, 'toppage.html', ctx)

