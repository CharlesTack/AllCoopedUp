from django.db import models
from django.contrib.auth.models import User

PLATFORM = ((1, "Xbox"), (2, "PlayStation"), (3, "Nintendo"), (4, "PC"))
RATING = ((1, "1⭐"), (2, "2⭐"), (3, "3⭐"), (4, "4⭐"), (5, "5⭐"))
PEGI = ((1, "3"), (2, "7"), (3, "12"), (4, "16"), (5, "18"))
STATUS = ((0, "Draft"), (1, "Published"))


class Review(models.Model):
    game_title = models.CharField(max_length=100, unique=True)
    review_title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="reviewer"
)
    # related_name above (and the three below) may need to be changed!
    platform_reviewed_on = models.IntegerField(choices=PLATFORM, default=None)
    index_excerpt = models.TextField()
    full_review = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    star_rating = models.IntegerField(choices=RATING, default=None)
    co_op_mode_couch = models.BooleanField(default=False)
    co_op_mode_online = models.BooleanField(default=False)
    pegi_rating = models.IntegerField(choices=PEGI, default=None)
    platform_availability_xbox = models.BooleanField(default=False)
    platform_availability_playstation = models.BooleanField(default=False)
    platform_availability_nintendo = models.BooleanField(default=False)
    platform_availability_pc = models.BooleanField(default=False)
    # image_upload = models.ImageField(upload_to='images/', blank=True, null=True)
    # commented out for now as this will need to be changed when we get to the image upload part
    approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=None)

class Comment(models.Model):
    review = models.ForeignKey(
    Review, on_delete=models.CASCADE, related_name="comments"
)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="commenter"
)
    game_title = models.ForeignKey(
    Review, on_delete=models.CASCADE, related_name="relatedgame"
)
    comment = models.TextField()
    approved = models.BooleanField(default=False)