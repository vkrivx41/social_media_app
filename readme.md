----- Social Media App ---------

1. Business Idea Creation

- This project is called "SISO or Simple Social Media App", it's a dynamic website that allows users to update
 trends, news, memories, routines, ideas, moods, plans, moment, work, travel, and feelings with 
 simple text and a single optional image.

** Problems to solve**
	- Lack of a free place to unveil what's going on in our lives.
	- Inadequate ways to view other people stuff and moments 
** Solutions**
	- Provide a free place for people to unveil their lives
	- Provide a place to view other people's stuff and react to them

##############################################################################################################

2. Project Design and Planning

** Functionalities **
    Functional
        User
            - A user needs to be able to create an account and login
            - A user needs to create a content that involves both texts and optional images
            - A user can modify their data and security parameters
            - A user can view their content and other people's
            - A user can delete or update their content and account
        Admin
            - Navigate the admin panel

    Non-Functional
        System
            - Performance: Needs to respond and load quickly
            - Availabilty: All time
            - Usability: The GUI needs to be appealing, light (not dark), and simple
            - Usability: The GUI front-page needs pagination for better navigation
        User
            - Data should be encrypted if necessary (passwords) 
            - Data should be private and only modifiable by the owner


** Version Features **
    Version 1
        - User Data (CRUD)
        - Content (CRUD)
        - Profile Photo
    Version 2
        - Short videos
        - Multiple Images for one post
        - Tags
        - Notifications
        - Video section
        - Emailing
        - Likes
        - Comments
        - Repost (Normal and With Thoughts)
        - Share
    Version 3
        - Chat (Messages, attachments)
        - Groups (Chat, Shares)
        - Status (24 hours)
        - Followers (Following and Unfollowing)
        - Admin Dashboard
        - Run Ads
        - Report (Crime, Violence)
    Version 4
        - Call
        - Live Events
        - Scheduling Tasks
        - Recommendation System


##############################################################################################################


3. Project Structure and Template

** Tech Stack and 3rd part tools **
    Front-end
        - HTML
        - CSS (Pure but very few)
    Back-end
        - Django
    DB
        - SQLite
    Storage
        - Local

** Folder Structure **
    - Django Standard Folder Structure
** UI/UX Template **
    - Paper Work

##############################################################################################################

4. System Design

** ERD **
    Objects
        - User
            - id (PK)
            - first_name
            - last_name
            - username
            - email
            - gender
            - password
            - date_joined
        - Post
            - id (PK)
            - user (FK)
            - description
            - image
        - Profile
            - id (PK)
            - user (FK)
            - image

##############################################################################################################

5. Version Control

** Git Setup **

##############################################################################################################

6. Dependency Management

** Tools for Dependency Management **
    Virtual Environment Library
        - poetry
    Dependency Management Library
        - poetry
** Library Versions Management **
        - the pyproject.toml file

##############################################################################################################

7. Coding and Implementation

** Creating Implementation Roadmaps **
** Writing code and pushing **

##############################################################################################################

8. Testing and Code Review
9. Modularize and Containerize
10. Hosting and CI/CD Pipelining

