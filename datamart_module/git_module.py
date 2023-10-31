import git
import os
from git.exc import InvalidGitRepositoryError
from utils.yaml_reader import YAMLConfigLoader

#pip install GitPython
class GitConfig:
    def __init__(self):
        self.config_loader = YAMLConfigLoader('../config.yaml')

    def config_getter(self,repositories)->dict:
        self.config_loader.load_config()
        base_config = {
            "username":None,
            "local_path":None,
            "endpoint":None,
            "token":None
        }

        if repositories == 'airflow_dag_repo':
            base_config["username"] = self.config_loader.key('airflow_dag_repo')["username"]
            base_config["local_path"] = self.config_loader.key('path_cfg')["repo_dir"]
            base_config["endpoint"] = self.config_loader.key('airflow_dag_repo')["endpoint"]
            base_config["token"] = os.environ.get('gitlab_local_rama')
        else:
            raise NotImplementedError("Repositories not supported, please check the config")
        return base_config

class GitManager():
    def __init__(self,repositories):
        super(GitManager,self).__init__()
        self.config = GitConfig().config_getter(repositories)
        self.username = self.config.get('username')
        self.local_path = self.config.get('local_path')
        self.end_point = self.config.get('endpoint')
        self.token = self.config.get('token')

    def is_directory_empty(self):
        items = os.listdir(self.local_path)
        return not items

    def clone(self):
        if self.is_directory_empty():
            gitlab_repo_url = f"https://{self.username}:{self.token}@{self.end_point}"
            print(f"cloning from @{self.end_point}")
            return git.Repo.clone_from(gitlab_repo_url, self.local_path)
        else :
            print(f"Clone skipped - could not perform clone because path {self.local_path} is not empty")
            return False

    def pull(self,branch):
        try:
            repo = git.Repo(self.local_path)
            print(f"pulling from @{self.end_point} branch {branch}")
            return repo.remotes.origin.pull(branch)
        except InvalidGitRepositoryError as e:
            print(f"invalid git repositories {e}")
            return False

    def push(self,file_path,branch):
        try:
            new_file = f"{self.local_path}/{file_path}"
            repo = git.Repo(self.local_path)
            repo.git.checkout(branch)
            print(f"checkout branch {branch}")
            repo.index.add([new_file])
            print(f"git add [{new_file}]")
            repo.index.commit("DE Automation")
            print(f"pushing {new_file}")
            return repo.remotes.origin.push(refspec=f"{branch}:{branch}")
        except Exception as e:
            print(f"an error occured - {e}")
            return False