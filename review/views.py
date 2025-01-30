from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Review
from .forms import CommentForm

# Create your views here.
class ReviewList(generic.ListView):
    queryset = Review.objects.filter(status=1).order_by("game_title")
    template_name = "review/index.html"
    paginate_by = 6

def review_detail(request, slug):
    """
    Display an individual :model:`review.Review`.

    **Context**

    ``review``
        An instance of :model:`review.Review`.

    **Template:**

    :template:`review/review_detail.html`
    """
    queryset = Review.objects.filter(status=1)
    review = get_object_or_404(queryset, slug=slug)
    comments = review.comments.all()
    comment_count = review.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.review = review
            comment.save()
    
    comment_form = CommentForm()

    return render(
        request,
        "review/review_detail.html",
        {"review": review,
         "comments": comments,
         "comment_count": comment_count,
         "comment_form": comment_form,
         },
    )