from django.apps import AppConfig


class ReviewConfig(AppConfig):
    """
    Provides primary key type for review app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'review'
