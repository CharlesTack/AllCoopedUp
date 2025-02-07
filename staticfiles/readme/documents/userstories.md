# User Stories

All of the user stories can be found on the project board [here](https://github.com/users/CharlesTack/projects/16).

All of the "Must-Have" stories are below:

**User Story 1: Review Text**

As a video game player with access to a large library of games, I want to read reviews so that I can get guidance on which games are good and which aren’t.

_Acceptance Criteria:_
- The site has a detailed reviews for a variety of games to start off with before additional contributors add their own.

_Tasks:_
- Create reviews (possibly with AI assistance) to include content on initial deployment.


**User Story 13: Attractive Design & Images**

As a user who is attracted to visually attractive websites I want to be greeted with a page which has imagery from gaming to make visiting the site more appealing so that I enjoy my visit more and come back more often.

_Acceptance Criteria:_
- The site looks visually appealing.
- Images of the games are on both the index page and detailed review page.

_Tasks:_
- Use Bootstrap and custom CSS to ensure that the layout and aesthetics of the page are attractive.
- Use gaming related imagery throughout the site, including “box art”.


**User Story 14: Inclusivity**

As a visually impaired user I would like all screens to have good contrast and all images to have alt descriptions so that I have a greater opportunity to be included.

_Acceptance Criteria:_
- The site’s colour scheme should pass contrast checking tests to ensure that it’s easy for all viewers to see.
- All images should have alt text for screen readers and for when images fail to load.

_Tasks:_
- Use appropriate tools to decide on a colour scheme and ensure that rigorous contrast checking is done in the testing stage.
- Use CSS variables to be able to quickly change colours to assist in making sure they have good contrast at the testing stage.
- Code the HTML to use something like: alt="Image of the box art for {{ game.title }}" so that the reviewer doesn’t have to stipulate the alt text manually.


**User Story 16: Reviewer Registration/Login**

As a gaming fan and contributor I would like to register and be able to login to my own profile so that I can submit my own reviews and comment on others and therefore feel more engaged with the site.

_Acceptance Criteria:_
- User can register to have their own login.
- User can login and logout.

_Tasks:_
- Code a registration page.
- Code login/logout buttons/links on all pages (in nav bar).


**User Story 17: Add a Review**

As a gaming fan and contributor I would like to be able to submit my own reviews so that I can help others and feel more engaged with the site.

_Acceptance Criteria:_
User can submit their own reviews.

_Tasks:_
- Code an “add review” page.
- Code an add review button which leads to the review page to allow the user to submit their own review.
- Give feedback that the review has been submitted (and is pending approval).


**User Story 18: Add Comments**

As a gaming fan and contributor I would like to be able to comment on other people’s reviews so that I feel more engaged with the site.

_Acceptance Criteria:_
- A logged in user can comment on reviews which have been submitted by other reviewers.
- Feedback is given to the customer to confirm that the comment has been received and is pending approval.

_Tasks:_
- A comments form is coded to take the comments and post them beneath the review on the detailed review page.
- Feedback is coded to confirm that the comment has been received and is pending approval.


**User Story 19: Edit/Delete Reviews & Comments**

As a gaming fan and contributor I would like to be able to edit and delete my reviews and comments so that I feel more in control of my contributions.

_Acceptance Criteria:_
- A logged in user can edit or delete their reviews and comments from within the detailed review page.
- Feedback is given to the user to confirm that the comment has been edited and is pending approval, or that it has been deleted (no approval required).

_Tasks:_
- The review page template is coded to display edit/delete buttons on the review itself if the review creator is logged in.
- The comments form is coded to have edit and delete buttons.
- The edit button results in the existing comment being returned to the comments text field to be edited.
- On submission feedback is coded to confirm that the edited comment has been received and is pending approval.
- The delete button produces a modal window to confirm that deletion is definitely desired. The modal also has yes and no buttons. Code all of this.


**User Story 23: Review/Comment Approval**

As the site administrator I need to be able to only accept reviews and comments onto the site once I have approved them to that I can maintain control of the content on the site.

_Acceptance Criteria:_
- Approval is needed before any review or comment goes live on the site.
- Only the admin/s can approve comments.

_Tasks:_
- Code approval requirement into site.