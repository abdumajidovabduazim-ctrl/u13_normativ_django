from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post


def post_list(request):
    q = request.GET.get('q', '')
    posts = Post.objects.all()

    if q:
        posts = posts.filter(title__icontains=q) | posts.filter(content__icontains=q)

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'posts/list.html', {
        'page_obj': page_obj,
        'q': q,
    })