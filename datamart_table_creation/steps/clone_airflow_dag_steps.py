import sys
sys.path.append('./')
from datamart_module.git_module import GitManager
from datamart_module.file_handler import FileOperations
from utils.yaml_reader import YAMLConfigLoader
from datamart_module.input_handler import InputHandler

#source and target folder
config = YAMLConfigLoader('./config.yaml')
config.load_config()
repository_folder = config.key('path_cfg')["repo_dir"]
branch = config.key('airflow_dag_repo')["branch"]

#check & drop if folder exists
if FileOperations(repository_folder).is_directory_exists() :
   FileOperations(repository_folder).remove_directory()

#create a local directory for cloning
FileOperations(repository_folder).create_directory()

#cloning the git
GitManager('airflow_dag_repo').clone()
GitManager('airflow_dag_repo').pull(branch)