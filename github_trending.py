import requests
import sys
from datetime import date, timedelta


def get_trending_repositories(top_size):
    search_date = (date.today() - timedelta(weeks=1)).strftime('%Y-%m-%d')
    payload = {"q": "created:>{}".format(search_date), "sort": "stars"}
    url = "https://api.github.com/search/repositories"
    trending_top = requests.get(url, params = payload).json()["items"]
    del trending_top[top_size:]
    return trending_top


def get_open_issues_amount(repo_owner, repo_name):
    url = "https://api.github.com/repos/{}/{}/issues".format(repo_owner, repo_name)
    return len(requests.get(url).json())


if __name__ == '__main__':
    top_size = 20
    for idx, repo in enumerate(get_trending_repositories(top_size), 1):
        repo_name = repo["name"]
        repo_owner = repo["owner"]["login"]
        opened_issues = get_open_issues_amount(repo_owner, repo_name)
        print("{}) Author: {}".format(idx, repo_owner))
        print("Repo name: {}".format(repo_name))
        print("Link: {}".format(repo["html_url"]))
        print("Stargazers count: {}".format(repo["stargazers_count"]))
        print("Opened issues: {}\n".format(opened_issues))
    sys.exit()
