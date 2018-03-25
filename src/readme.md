## To run:

###
$ cd gitapi/src

$ export FLASK_APP=api.py

$ flask run

* Running on http://127.0.0.1:5000/
###

## Examples
###
http://127.0.0.1:5000/github_user/bitbucket_user/bitbucket_type
* Bitbucket_type is either "user" or "teams" (defaults to "user")

* Teams example
http://127.0.0.1:5000/mailchimp/mailchimp/teams

* 2 Users
http://127.0.0.1:5000/kennethreitz/sarahbanas

* Team/User
http://127.0.0.1:5000/mailchimp/sarahbanas

* User/Team
http://127.0.0.1:5000/kennethreitz/mailchimp/teams
###



