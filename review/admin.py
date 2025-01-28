from django.contrib import admin
from .models import Review, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):

    list_display = ('game_title', 'slug', 'status')
    search_fields = ['game_title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('game_title',)}
    summernote_fields = ('full_review',)


# Register your models here.
admin.site.register(Comment)