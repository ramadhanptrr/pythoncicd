import git
import os

def clone():
    gitlab_token = os.environ.get('gitlab_local_rama')
    gitlab_username = 'ramadhanputraaf'
    gitlab_repo_url = f"https://{gitlab_username}:{gitlab_token}@gitlab.com/ramadhanputraaf/my-stage.git"
    local_path = "/var/jenkins_home/workspace/datamart_automation/repositories"
    repo = git.Repo.clone_from(gitlab_repo_url, local_path)
    return repo

clone()