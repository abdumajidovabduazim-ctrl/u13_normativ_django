from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','is_deleted','created_at')

    def get_queryset(self, request):
        return Post._default_manager.all()