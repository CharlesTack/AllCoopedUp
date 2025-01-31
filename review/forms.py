from django import forms
from .models import Comment, Review

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'game_title', 'review_title', 'platform_reviewed_on', 
            'index_excerpt', 'star_rating',
            'co_op_mode_couch', 'co_op_mode_online', 'pegi_rating',
            'platform_availability_xbox', 'platform_availability_playstation',
            'platform_availability_nintendo', 'platform_availability_pc', 
            'featured_image', 'full_review', 'status',
        ]