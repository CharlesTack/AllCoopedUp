from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

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
    featured_image = CloudinaryField('image', default='missingboxart')
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
    approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=None)

    class Meta:
        ordering = ["-game_title"]

    def __str__(self):
        return f"{self.game_title} | written by {self.author}"


class Comment(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    comment = models.TextField()
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-review"]

    def __str__(self):
        return f"Comment: {self.comment} by {self.author} on {self.review}"
