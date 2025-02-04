from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Review, RATING, PEGI

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
            'featured_image', 'full_review',
        ]
        widgets = {
            'full_review': SummernoteWidget(),
            'star_rating': forms.Select(choices=[('', 'Select a rating')] + list(RATING)),
            'pegi_rating': forms.Select(choices=[('', 'Select a PEGI rating')] + list(PEGI)),
        }

class SearchForm(forms.Form):
    PLATFORM_CHOICES = [
        ('xbox', 'Xbox'),
        ('playstation', 'PlayStation'),
        ('nintendo', 'Nintendo'),
        ('pc', 'PC'),
    ]
    query = forms.CharField(max_length=200, required=False, label='Search for a game')
    platform = forms.ChoiceField(choices=[('', 'All Platforms')] + PLATFORM_CHOICES, required=False)
    pegi_rating = forms.ChoiceField(choices=[('', 'All PEGI Ratings')] + list(PEGI), required=False)
    co_op_mode_couch = forms.BooleanField(required=False, label='Co-op Mode Couch')
    co_op_mode_online = forms.BooleanField(required=False, label='Co-op Mode Online')