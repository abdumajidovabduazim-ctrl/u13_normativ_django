from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .forms import PostForm
from .models import Post


def post_list(request):

    q = request.GET.get('q', '')

    # 🔥 soft delete ishlatganing uchun is_deleted=False shart
    posts = Post.objects.filter(is_deleted=False)

    if q:
        posts = posts.filter(
            title__icontains=q
        ) | posts.filter(
            content__icontains=q
        )

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'posts/list.html', {
        'page_obj': page_obj,
        'q': q,
    })


def create_post(request):

    if request.method == 'POST':

        form = PostForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()

    else:
        form = PostForm()

    return render(
        request,
        'posts/create.html',
        {'form': form}
    )


def post_detail(request, pk):

    post = get_object_or_404(Post, pk=pk)

    return render(
        request,
        'posts/detail.html',
        {
            'post': post
        }
    )