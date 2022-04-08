from django.contrib import admin

from blog.models import CategoryModel, PostModel, CommentModel


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')

@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'username', 'created_date', 'is_active', 'is_updated', 'category_list',)
    readonly_fields = ('is_updated',)
    list_filter = ("categories__title", )
    search_fields = ("content__icontains", )

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'created_date', 'modified_date')
