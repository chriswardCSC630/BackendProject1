* Chris Ward and Rachna Lewis
* CSC630 with Dr. Zufelt, Period 5
* Due: Friday, April 5th

**Academic Integrity Note:** Both in and out of class, Rachna and I worked with the
other python backend group, Eric and Katherine.

Link used to create database: https://docs.appery.io/docs/apiexpress-databaseconnection-heroku-postgres

The server runs on Heroku at: https://backend-project1.herokuapp.com/

Code was tested locally on port 8000. To test code locally, you will need to modify
NAME, USER, and PASSWORD in the DATABASES block located in setting.py

# Server Explanation:
  For the most part, Rachna and I followed the user and locations idea outlined
  on the canvas assignment. Here is how you should interact with the server:

  * https://backend-project1.herokuapp.com/: link to this README.md on github
  * https://backend-project1.herokuapp.com/admin/: directly access the database
  * https://backend-project1.herokuapp.com/user_id/poi: GET all of a user's place of interests, or POST a new one
  * https://backend-project1.herokuapp.com/users/: GET all users (name and username displayed) or POST a new one
  * https://backend-project1.herokuapp.com/users/user_id/: PATCH or DELETE a user based on their ID
  * https://backend-project1.herokuapp.com/locations/: return all users' homebase and place of interest (latitude, longitude)
  * https://backend-project1.herokuapp.com/locations/user_id/poi_title/: PATCH or DELETE a place of interest based on their ID and the poi's title

## A few notes:
  1) Do not name two places of interest the same thing. This will cause PATCH and DELETE errors which we did not yet handle.
  2) Do not give two users the same ID. IDs should be unique.
  3) The following links were used to help push to Heroku and link to a database:
    https://docs.appery.io/docs/apiexpress-databaseconnection-heroku-postgres
    To solve the error where heroku created 0 tables, I pushed my tables from my local databases
    using the following link: https://devcenter.heroku.com/articles/heroku-postgresql#heroku-postgres-ssl
