A Simple REST API project with Python Flask

The methods allowed for the following endpoints are as follows

Endpoint 
- /api/v1/users
get - gets all the available users from the DB
post - creates a new user from the DB - requires name and unique email passed in request body


- /api/v1/users/{{id}}
requires id of the users stored in the db as a request parameter

get - gets the specific user from the db
patch - modifies the name/ email of the user from the db and returns the edited entry - requires name and email to be passed in the request body
delete - deletes the user entry in the db and returns the deleted entry
