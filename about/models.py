from django.db import models

# Create your models here.


class About(models.Model):
    """
    Stores a single about me text
    """
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    # Commented out below until we get to the image upload part
    # profile_picture = CloudinaryField('image', default="placeholder")

    def __str__(self):
        return self.title

# Commented out below as it's too early for this yet

# class CollaborateRequest(models.Model):
#     """
#     Stores a single collaboration request message
#     """
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#     message = models.TextField()
#     read = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Collaboration request from {self.name}"