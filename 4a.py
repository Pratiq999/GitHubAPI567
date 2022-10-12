"""
Author : Pratik Kadam

"""
import requests
import json

def fetchRepos(user_id):
    repo_api="https://api.github.com/users/"
    commit_api="https://api.github.com/repos/"
    list_of_repo=[]
    commits=[]
    repo_url=repo_api+f'{user_id}/'+'repos'

    try:
        repo_url=requests.get(url=repo_url)
    except (TypeError, KeyError, IndexError):

        return "Unable to fetch repositories"

    repo_url=json.loads(repo_url.text)

    for repository in repo_url:
        try:
            list_of_repo.append(repository['name'])
        except (TypeError, KeyError, IndexError):

            return "Repository name does not exist"

    for r in list_of_repo:
        commit_url=commit_api+f'{user_id}/{r}/commits'

        try:
            req=requests.get(url=commit_url)
        except(TypeError, KeyError, IndexError):
            return "Unable to fetch commits"

        req_json=json.loads(req.text)
        commits.append(f'Repo:{r} Number of commits:{len(req_json)}')

    return commits

def main():
    """Retrive the user's ID as input"""
    user=input("Enter user's GitHub ID: ")
    for repo in fetchRepos(user):
        print(repo)

if __name__=='__main__':
    main()

