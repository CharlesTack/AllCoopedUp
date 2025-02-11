import logging
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from .models import Review, Comment
from .forms import CommentForm, ReviewForm, SearchForm

logger = logging.getLogger(__name__)


# Create your views here.
class ReviewList(generic.ListView):
    """
    View to list all reviews with pagination and search functionality.
    """
    model = Review
    template_name = "review/index.html"
    context_object_name = "review_list"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        """
        Add extra context for search feedback.
        """
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("query", "")
        platform = self.request.GET.get("platform", "")
        pegi_rating = self.request.GET.get("pegi_rating", "")
        co_op_mode_couch = self.request.GET.get("co_op_mode_couch", "")
        co_op_mode_online = self.request.GET.get("co_op_mode_online", "")
        form = SearchForm(self.request.GET)
        results = context["review_list"]

        # Add extra context for search feedback
        context["form"] = form
        context["query"] = query
        context["platform"] = platform
        context["pegi_rating"] = pegi_rating
        context["co_op_mode_couch"] = co_op_mode_couch
        context["co_op_mode_online"] = co_op_mode_online
        context["no_results"] = query and not results

        return context

    def get_queryset(self):
        """
        Filter the queryset based on search parameters.
        """
        queryset = (
            super().get_queryset()
            .filter(status=1)
            .order_by('game_title')
        )
        query = self.request.GET.get("query", None)
        platform = self.request.GET.get("platform", None)
        pegi_rating = self.request.GET.get("pegi_rating", None)
        co_op_mode_couch = self.request.GET.get("co_op_mode_couch", None)
        co_op_mode_online = self.request.GET.get("co_op_mode_online", None)

        if query:
            queryset = queryset.filter(game_title__icontains=query)
        if platform:
            if platform == 'xbox':
                queryset = queryset.filter(platform_availability_xbox=True)
            elif platform == 'playstation':
                queryset = queryset.filter(
                    platform_availability_playstation=True
                )
            elif platform == 'nintendo':
                queryset = queryset.filter(platform_availability_nintendo=True)
            elif platform == 'pc':
                queryset = queryset.filter(platform_availability_pc=True)
        if pegi_rating:
            queryset = queryset.filter(pegi_rating=pegi_rating)
        if co_op_mode_couch:
            queryset = queryset.filter(co_op_mode_couch=True)
        if co_op_mode_online:
            queryset = queryset.filter(co_op_mode_online=True)

        return queryset


def review_detail(request, slug):
    """
    View to display the details of a single review, including comments.
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
                request, messages.SUCCESS,
                "Thanks for your comment. "
                "It will be added once approved."
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


@login_required
def edit_review(request, slug):
    """
    View to edit an existing review.
    """
    review = get_object_or_404(Review, slug=slug, author=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.status = 0  # Set the status to draft (0) pending approval
            review.save()
            messages.success(
                request,
                'Your review has been updated and is pending approval.'
            )
            return redirect('home')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'review/submit_review.html', {'form': form})


@login_required
def delete_review(request, slug):
    """
    View to delete an existing review.
    """
    logger.info(f"Received request to delete review with slug: {slug}")
    review = get_object_or_404(Review, slug=slug, author=request.user)
    review.delete()
    messages.success(request, 'Your review has been deleted.')
    return redirect('home')


@login_required
def submit_review(request):
    """
    View to submit a new review.
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.status = 0  # 0 means the review is draft as default
            review.slug = slugify(review.game_title)
            review.save()
            messages.success(
                request,
                'Many thanks! Your review has been '
                'submitted and is pending approval.'
            )
            return redirect('home')
    else:
        form = ReviewForm()
    return render(request, 'review/submit_review.html', {'form': form})


def comment_edit(request, slug, comment_id):
    """
    View to edit an existing comment on a review.
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
            messages.add_message(
                request, messages.ERROR,
                'Error updating comment!'
            )

    return HttpResponseRedirect(reverse('review_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    View to delete an existing comment on a review.
    """
    logger.info(
        f"Received request to delete comment with ID: {comment_id} "
        f"for review with slug: {slug}"
    )
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('review_detail', args=[slug]))
