from celery import shared_task
from django.utils import timezone

from .models import Post


@shared_task
def check_old_posts():

    posts = Post.objects.filter(
        created_at__lt=timezone.now()
    )

    print(
        f"Tekshirildi: {posts.count()} ta post"
    )

    return posts.count()