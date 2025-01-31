document.addEventListener("DOMContentLoaded", function() {
    const editButtons = document.getElementsByClassName("btn-edit");
    const commentText = document.getElementById("id_comment");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");

    const deleteCommentModalElement = document.getElementById("deleteCommentModal");
    const deleteReviewModalElement = document.getElementById("deleteReviewModal");

    if (deleteCommentModalElement) {
        const deleteCommentModal = new bootstrap.Modal(deleteCommentModalElement);
        const deleteCommentButtons = document.querySelectorAll(".btn-delete[data-bs-target='#deleteCommentModal']");
        const deleteConfirm = document.getElementById("deleteCommentConfirm");

        // Delete comment functionality
        for (let button of deleteCommentButtons) {
            button.addEventListener("click", (e) => {
                let commentId = e.target.getAttribute("data-comment_id");
                console.log(`Deleting comment with ID: ${commentId}`);
                if (commentId) {
                    deleteConfirm.href = `delete_comment/${commentId}/`;
                    console.log(`Set delete comment href to: ${deleteConfirm.href}`);
                } else {
                    console.error("Comment ID is null or undefined");
                }
                deleteCommentModal.show();
            });
        }
    } else {
        console.error("Delete comment modal element not found");
    }

    if (deleteReviewModalElement) {
        const deleteReviewModal = new bootstrap.Modal(deleteReviewModalElement);
        const deleteReviewButtons = document.querySelectorAll(".btn-delete[data-bs-target='#deleteReviewModal']");
        for (let button of deleteReviewButtons) {
            button.addEventListener("click", (e) => {
                let reviewSlug = e.target.getAttribute("data-review_slug");
                console.log(`Deleting review with slug: ${reviewSlug}`);
                if (reviewSlug) {
                    const deleteReviewConfirm = document.getElementById("deleteReviewConfirm");
                    deleteReviewConfirm.href = `/${reviewSlug}/delete/`;
                    console.log(`Set delete review href to: ${deleteReviewConfirm.href}`);
                } else {
                    console.error("Review slug is null or undefined");
                }
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
            console.log(`Editing comment with ID: ${commentId}, Content: ${commentContent}`);
            if (commentId) {
                commentText.value = commentContent;
                submitButton.innerText = "Update";
                commentForm.setAttribute("action", `edit_comment/${commentId}/`);
                console.log(`Set form action to: edit_comment/${commentId}/`);
            } else {
                console.error("Comment ID is null or undefined");
            }
        });
    }
});