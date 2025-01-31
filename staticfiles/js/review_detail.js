document.addEventListener("DOMContentLoaded", function() {
    const editButtons = document.getElementsByClassName("btn-edit");
    const commentText = document.getElementById("id_comment");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");

    const deleteCommentModalElement = document.getElementById("deleteCommentModal");
    const deleteReviewModalElement = document.getElementById("deleteReviewModal");

    if (deleteCommentModalElement) {
        const deleteCommentModal = new bootstrap.Modal(deleteCommentModalElement);
        const deleteButtons = document.getElementsByClassName("btn-delete");
        const deleteConfirm = document.getElementById("deleteCommentConfirm");

        // Delete comment functionality
        for (let button of deleteButtons) {
            button.addEventListener("click", (e) => {
                let commentId = e.target.getAttribute("data-comment_id");
                console.log(`Deleting comment with ID: ${commentId}`);
                deleteConfirm.href = `delete_comment/${commentId}`;
                deleteCommentModal.show();
            });
        }
    } else {
        console.error("Delete comment modal element not found");
    }

    if (deleteReviewModalElement) {
        const deleteReviewModal = new bootstrap.Modal(deleteReviewModalElement);
        const deleteReviewButtons = document.querySelectorAll(".btn-danger[data-bs-target='#deleteReviewModal']");
        for (let button of deleteReviewButtons) {
            button.addEventListener("click", (e) => {
                let reviewSlug = e.target.getAttribute("data-review_slug");
                console.log(`Deleting review with slug: ${reviewSlug}`);
                document.getElementById("deleteReviewConfirm").href = `/delete/${reviewSlug}/`;
                deleteReviewModal.show();
            });
        }
    } else {
        console.error("Delete review modal element not found");
    }

    // Edit comment functionality
    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("data-comment_id");
            let commentContent = document.getElementById(`comment${commentId}`).innerText;
            commentText.value = commentContent;
            submitButton.innerText = "Update";
            commentForm.setAttribute("action", `edit_comment/${commentId}`);
        });
    }
});