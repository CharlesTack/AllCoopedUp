from django.contrib import admin
from .models import Review
# NB - above when we add additional models we can just add them seperated by a comma


# Register your models here.
admin.site.register(Review)