# Harvard CS50 Web Capstone: *CK Blues*
__By Chris Korsak__

## Project Overview

My Harvard CS50 Web capstone is called __*CK Blues*__. This is a web application that helps guitar players improve their guitar playing. This website provides guitar lessons, individual feedback, and backing tracks to jam with. The application consists of a blog with both free and premium content. Users can sign up for an account to access premium content and submit video links of themselves playing guitar for individual feedback.

## Website Sections

### Login/Logout/Register
In order to access 'premium' content, the user has to register and log in to their account. Users will be asked to provide credentials to register and/or log in.
#### Login/Logout/Register Behavior
* When a user navigates to the registration page, they will be asked to provide a first name, last name, username, password (twice), and an email address. The application will verify these inputs and redirect the user to a newly created user dashboard if successful.
* When a user navigates to the login page, they will be asked to provide a username and password. The application will verfiy these inputs and redirect to the user dashboard if successful.
* Clicking the logout link in the navigation will log the user out and redirect the user to the homepage.

### Blog
The main section of this website is a blog that is filled with content (both free and premium) to help improve guitar playing. Blog articles will consist of lessons, exercises, and backing tracks to solo over.
#### Blog Behavior
* When a user navigates to the homepage, the blog will be populated with a number of 'free' posts that do not require the user to log in.
* When a user is logged in, the blog will be populated with both 'free' and 'premium' content.
* Users can filter blog posts by category to more easily find content they are looking for (lessons, exercises, backing tracks).
* Blog posts will display only a title and excerpt on the main blog page.
* When a user clicks on a post title, the user will be taken to the blog post page where the entire post is displayed.
* Users will be able to comment on posts if logged in to the website. Comments will be displayed whether the user is logged in or not.
* Only 10 posts will display on a page, and pagination links to navigate to more articles will be displayed at the bottom of the page.

### Feedback
In this section of the website, users can submit a form which allows them to receive feedback (aka critique) on their guitar playing. Users will be able to submit a link to a youtube video of themselves playing a song, improvising, or using a playing technique they'd like feedback with.
#### Feedback Behavior
* When logged in, a link called *feedback* will be displayed in the navigation section. If a user clicks on this link, they will be directed to the feedback submission page.
* The feedback page will display a form where the user can submit a youtube video link, select the video category from a dropdown menu (cover song, soloing, rhythm, improvisation, technique), and describe any questions or comments about their video submission.
* Successfully submitting a feedback form will notify the user that their form has been received and is in the queue for review.

### User Dashboard
Users who are logged in will have a 'dashboard' which allows them to see their account details and their feedback submissions.
#### User Dashboard Behavior
* The dashboard will display a list of all feedbacks that have been submitted. Clicking on a feedback link will direct the user to a feedback page that displays a video screencast and any comments from the site administrator.
* Users can update their email or password credentials via dashboard settings.

### Admin
This utilizes the Django admin app in order to take care of site administration. Site administrators can create and publish blog posts, respond to user feedback submissions, and monitor comments.
### Admin Behavior
* Django models displayed in the Django admin app: (User, Post, PostComment, Feedback, FeedbackComment).

## Project Complexity
I believe this project satisfies the complexity requirements and is disinct from the previous class projects for the following reasons:

* This project is modeled as a blog, which is a website structure we have not attempted in the class.
* This project uses five Django models, which is more than any project I've created in this class.
* Because blog post content can be diverse, a user-friendly way to create this content is needed. I have implimented using a pre-made rich text editor called *ckeditor* to achieve this. (rich text editor: https://www.youtube.com/watch?v=mF5jzSXb1dc)

## File Contents

TODO (list contents of files I created)

## Technologies Used
* Django (Python)
* HTML
* CSS
* Javascript

## How To Run This Application

TODO
<!-- If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to a requirements.txt file! -->
using django cdeditor (rich text editor)
* run pip install django-ckeditor in terminal

<!-- * Administrators can flag posts as published, unpublished, free, or premium. -->

