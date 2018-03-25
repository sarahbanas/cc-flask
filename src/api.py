import json
import requests

from flask import Flask

app = Flask(__name__)

# bitbucket has type "teams" and type "user", defaulting to "user"
@app.route('/<github_user>/<bitbucket_user>/', defaults={'bitbucket_type': 'user'})
@app.route('/<github_user>/<bitbucket_user>/<bitbucket_type>')
def combine_profile(github_user, bitbucket_user, bitbucket_type):
	git = get_github(github_user)
	git_repo = get_github_repos(github_user)
	bit = get_bitbucket(bitbucket_user, bitbucket_type)
	bit_repo = get_bitbucket_repositories(bitbucket_user)
	bit_followers = get_bitbucket_followers(bitbucket_user, bitbucket_type)

	name = "Name: " + (git['name'] if git['name'] is not None else bit['display_name'])
	
	total_public_repos = git['public_repos'] + bit_repo['size']
	count_forked = 0
	total_follower_count = git['followers'] + bit_followers['size']
	total_watcher_count = 0
	total_stars = 0
	total_open_issues = 0
	total_commits_to_repos = 0
	total_account_size = 0
	count_languages_used = 0
	list_languages_used = ""
	count_repo_topics = 0
	list_repo_topics = ""

	for repo in git_repo:
		count_forked += repo['forks_count']
		total_watcher_count += repo['watchers_count']
		total_stars += repo['stargazers_count']
		total_open_issues += repo['open_issues_count']
		total_account_size += repo['size']

	return name + "<br />" + \
		"Total Public Repos: " + str(total_public_repos) + "<br />"+ \
		"Forked Repos: " + str(count_forked) + "<br /> " + \
		"Total Follower Count: " + str(total_follower_count) + "<br />" + \
		"Total Watcher Count: "  + str(total_watcher_count) + "<br />" + \
		"Total Stars: " + str(total_stars) + "<br />" + \
		"Total Open Issues " + str(total_open_issues) + "<br /> " + \
		"Total Commits To Repos: " + str(total_commits_to_repos) +"<br />" + \
		"Total Account Size: " + str(total_account_size) + "<br />" + \
		"Languages Used: " + str(count_languages_used) + "<br />" + \
		"Count Repo Topics: " + str(count_repo_topics)
	

# would like to test
def get_github(github_user):
	url = "https://api.github.com/users/" + github_user
	return get_data(url)

# would like to test
def get_github_repos(github_user):
	url = "https://api.github.com/users/" + github_user + "/repos"
	return get_data(url)

# would like to test
def get_bitbucket(bitbucket_user, type):
	if(type == "user"):
		url  = "https://api.bitbucket.org/2.0/users/" + bitbucket_user
	else:
		url = "https://api.bitbucket.org/2.0/teams/" + bitbucket_user

	return get_data(url)

# would like to test
def get_bitbucket_followers(bitbucket_user, type):
	if(type == "user"):
		url  = "https://api.bitbucket.org/2.0/users/" + bitbucket_user + "/followers"
	else:
		url = "https://api.bitbucket.org/2.0/teams/" + bitbucket_user + "/followers"

	return get_data(url)

# would like to test
def get_bitbucket_repositories(bitbucket_user):
	url  = "https://api.bitbucket.org/2.0/repositories/" + bitbucket_user

	return get_data(url)

''' returns a json data response '''
def get_data(url):
	response = requests.get(url)
	if response.status_code != 200:
		return 'error {}'.format(response.status_code)
	else:
		data = json.loads(response.text)
		return data