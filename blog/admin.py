from django.contrib import admin
from blog.models import Article, Category, Tag


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'state', 'category', 'created']
    list_filter = ["state", "category"]
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ("title",)
    list_per_page = 4


admin.site.register(Article, ArticleAdmin)
# Register your models here.
admin.site.register([Category, Tag])
# admin.site.register(Category)
# admin.site.register(Tag)
