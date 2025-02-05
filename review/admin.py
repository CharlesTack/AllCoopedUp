from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Review, Comment


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):

    list_display = ('game_title', 'slug', 'status', 'approved')
    search_fields = ['game_title']
    list_filter = ('status', 'approved')
    prepopulated_fields = {'slug': ('game_title',)}
    summernote_fields = ('full_review',)


# Register your models here.
admin.site.register(Comment)
