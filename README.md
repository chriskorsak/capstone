# Harvard CS50 Web Capstone: CK Blues - By Chris Korsak

## Project Overview

My Harvard CS50 Web capstone is called 'CK Blues.' This is a web application that helps guitar players improve their playing. This website provides guitar lessons, individual feedback, and backing tracks to jam with. The application is primarily a blog with both free and premium content. Users can sign up for an account to access premium lessons, content, and be able to submit a video link for individual feedback of their guitar playing.

## Website Sections

### Login/Logout/Register
In order to access 'premium' content, the user has to register and log in to their account. Users will will be asked to provide credentials to register and/or log in.
#### Login/Logout/Register Behavior
* When a user navigates to the registration page, they will be asked to provide a username, password (twice), and an email address. The application will verify these inputs and redirect to a user dashboard if successful.
* When a user navigates to the login page, they will be asked to provide a username and password. The application will verfiy these inputs and redirect to a user dashboard if successful.
* Clicking the logout link in the navigation will log the user out and redirect the user to the homepage.

### Blog
The main section of this website is a blog that is filled with content (both free and premium) on how to improve guitar playing. As a former guitar instructor, I have a catalog of lessons, exercises, and philosophies to share.
#### Blog Behavior
* When a user navigates to the homepage, the blog will be populated with 'free' posts that do not require the user to log in.
* When a user is logged in, the blog will be populated with both 'free' and 'premium' content
* Users can filter blog posts by category to more easily find content they are looking for.
* Blog posts will display only a small portion of their content on the main blog page.
* When a user clicks on a post title, the user will be taken to the blog post page where the entire post is displayed.
* Users will be able to comment on posts if logged in to the website. Comments will be displayed whether logged in or not.
* Only 10 posts will display on a page, and pagination links to navigate to more articles will be displayed.

## Feedback
In this section of the website, users can submit a form which allows them to receive feedback (aka critique) on their guitar playing. Users will need to submit a link to a youtube video of themselves playing a song, improvising, or using a playing technique they'd like help with.
#### Feedback Behavior
* When logged in a link called 'feedback' will be displayed. If a user clicks on this link, they will be directed to the feedback page.
* The feedback page will display a form where the user can submit a youtube video link, select the type of video from a dropdown menu (cover song, improvisation, technique), and describe any questions or comments about the video for guidance.
* Successfully submitting a feedback form will notify the user that their form has been received and is in the queue for review.
* The feedback page will display any feedbacks that are ready to view. Clicking on a feedback title will direct the user to a feedback page that displays a video screencast and any comments.

## Admin
This utilizes the Django admin app in order to take care of site administration. Site administrators can create and publish blog posts, review user comments, and respond to user feedback submissions.

## User Dashboard
Users who are logged in will have a 'dashboard' which allows them to see their account details and feedback submissions.
* The dashboard will list all feedback submissions. Users can click on a submission to see their critique if it's completed.
* Users can update their email or password credentials via dashboard settings.

# Project Complexity
I believe this project satisfies the complexity requirements and is disinct from the previous class projects for the following reasons:

<!-- What’s contained in each file you created. -->

<!-- How to run your application. -->

<!-- If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to a requirements.txt file! -->

 
 <!-- notes -->
 Blog posts could be written in markdown language. Or, use this for rich text editor: https://www.youtube.com/watch?v=mF5jzSXb1dc . Blog posts could be flagged as unpublished, published, free, and premium. Blog page can have categories so you can filter posts.
