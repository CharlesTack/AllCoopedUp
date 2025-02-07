from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Review, RATING, PEGI


class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a review
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Comment
        fields = ('comment',)


class ReviewForm(forms.ModelForm):
    """
    Form class for users to submit a review.
    """
    class Meta:
        """
        Specify the Django model and order of the fields.
        """
        model = Review
        fields = [
            'game_title', 'review_title', 'platform_reviewed_on',
            'index_excerpt', 'star_rating',
            'co_op_mode_couch', 'co_op_mode_online', 'pegi_rating',
            'platform_availability_xbox', 'platform_availability_playstation',
            'platform_availability_nintendo', 'platform_availability_pc',
            'featured_image', 'full_review',
        ]
        labels = {
            'index_excerpt': 'One line teaser for the home page',
            'pegi_rating': 'PEGI rating',
            'featured_image': 'Image (Please see copyright notice below)',
        }
        widgets = {
            'full_review': SummernoteWidget(),
            'star_rating': forms.Select(
                choices=[('', 'Select a rating')] + list(RATING)),
            'pegi_rating': forms.Select(
                choices=[('', 'Select a PEGI rating')] + list(PEGI)),
            'index_excerpt': forms.Textarea(attrs={'class': 'index-excerpt'}),
        }


class SearchForm(forms.Form):
    """
    Form class for users to search for reviews.
    """
    PLATFORM_CHOICES = [
        ('xbox', 'Xbox'),
        ('playstation', 'PlayStation'),
        ('nintendo', 'Nintendo'),
        ('pc', 'PC'),
    ]
    query = forms.CharField(
        max_length=200, required=False, label='Search for a game'
    )
    platform = forms.ChoiceField(
        choices=[('', 'All Platforms')] + PLATFORM_CHOICES, required=False
    )
    pegi_rating = forms.ChoiceField(
        choices=[('', 'All PEGI Ratings')] + list(PEGI), required=False
    )
    co_op_mode_couch = forms.BooleanField(
        required=False, label='Co-op Mode Couch'
    )
    co_op_mode_online = forms.BooleanField(
        required=False, label='Co-op Mode Online'
    )
