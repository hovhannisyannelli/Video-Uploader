# Video-Uploader

## Installation

Here are the basic steps to get started. I have dockerized the app, so the setting up shall be easier (You shall have Docker installed). 

### Clone

> Clone this repo to your local machine using `https://github.com/hovhannisyannelli/Video-Uploader.git`

### Setup

- Go to the root directory 
- Open the terminal in the root directory
- run `docker-compose up`
- If your build is successful, open your browser and access the application (in my case http://localhost:8000/)

## Documentation 

The app has a user authorization (Log in and Sign Up). You are able to upload, edit and delete videos. The metadata is kept in a db (SQLite) and the videos are kept in /media directory. The videos are also filtered by the user and their titles are shown in user's account.
