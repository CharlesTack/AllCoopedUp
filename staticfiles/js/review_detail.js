document.addEventListener("DOMContentLoaded", function() {
    const editButtons = document.getElementsByClassName("btn-edit");
    const commentText = document.getElementById("id_comment");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");

    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");

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

    // Delete comment functionality
    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("data-comment_id");
            console.log(`Deleting comment with ID: ${commentId}`);
            deleteConfirm.href = `delete_comment/${commentId}`;
            deleteModal.show();
        });
    }

    // Delete review functionality
    const deleteReviewButtons = document.querySelectorAll(".btn-danger[data-bs-target='#deleteReviewModal']");
    for (let button of deleteReviewButtons) {
        button.addEventListener("click", (e) => {
            let reviewSlug = e.target.getAttribute("data-review_slug");
            console.log(`Deleting review with slug: ${reviewSlug}`);
            document.getElementById("deleteReviewConfirm").href = `/delete/${reviewSlug}/`;
        });
    }
});