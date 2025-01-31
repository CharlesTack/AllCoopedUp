from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Review, Comment
from .forms import CommentForm, ReviewForm

# Create your views here.
class ReviewList(generic.ListView):
    """
    Returns all published posts in :model:`review.Review`
    and displays them in a page of six reviews. 
    **Context**

    ``queryset``
        All published instances of :model:`review.Review`
    ``paginate_by``
        Number of posts per page.
        
    **Template:**

    :template:`review/index.html`
    """
    queryset = Review.objects.filter(status=1).order_by("game_title")
    template_name = "review/index.html"
    paginate_by = 6


def review_detail(request, slug):
    """
    Display an individual :model:`review.Review`.

    **Context**

    ``review``
        An instance of :model:`review.Review`.
    ``comments``
        All approved comments related to the post.
    ``comment_count``
        A count of approved comments related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`

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
            messages.add_message(
                request, messages.SUCCESS, "Thanks for your comment. It will be added once approved."
            )
    
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


def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context**

    ``review``
        An instance of :model:`review.Review`.
    ``comment``
        A single comment related to the review.
    ``comment_form``
        An instance of :form:`review.ReviewForm`
    """
    if request.method == "POST":

        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('review_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``review``
        An instance of :model:`review.Review`.
    ``comment``
        A single comment related to the review.
    """
    queryset = Review.objects.filter(status=1)
    review = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('review_detail', args=[slug]))

@login_required
def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.status = 0 # 0 means the review is draft as default
            review.save()
            messages.success(request, 'Many thanks! Your review has been submitted and is pending approval.')
            return redirect('home')  # this is the page where the user will be redirected to after successfully submitting a review
    else:
        form = ReviewForm()
    return render(request, 'review/submit_review.html', {'form': form})