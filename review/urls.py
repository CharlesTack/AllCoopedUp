from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('submit/', views.submit_review, name='submit_review'),
    path('<slug:slug>/', views.review_detail, name='review_detail'),
    path('<slug:slug>/edit/', views.edit_review, name='edit_review'),
    path('<slug:slug>/delete/', views.delete_review, name='delete_review'),
    path('<slug:slug>/edit_comment/<int:comment_id>/',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>/',
         views.comment_delete, name='comment_delete'),
]