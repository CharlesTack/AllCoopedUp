document.addEventListener("DOMContentLoaded", function() {
    const deleteCommentButtons = document.querySelectorAll(".btn-delete[data-bs-target='#deleteCommentModal']");
    for (let button of deleteCommentButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("data-comment_id");
            document.getElementById("deleteCommentConfirm").href = `/delete_comment/${commentId}/`;
        });
    }

    const deleteReviewButtons = document.querySelectorAll(".btn-danger[data-bs-target='#deleteReviewModal']");
    for (let button of deleteReviewButtons) {
        button.addEventListener("click", (e) => {
            let reviewSlug = e.target.getAttribute("data-review_slug");
            document.getElementById("deleteReviewConfirm").href = `/delete_review/${reviewSlug}/`;
        });
    }
});