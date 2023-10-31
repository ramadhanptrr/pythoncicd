import sys
from datamart_module.git_module import GitManager
from datamart_module.file_handler import FileOperations
from utils.yaml_reader import YAMLConfigLoader
from datamart_module.input_handler import InputHandler

#source and target folder
config = YAMLConfigLoader('../config.yaml')
input_value = InputHandler.InputValue()
config.load_config()
repository_folder = config.key('path_cfg')["repo_dir"]
destination_directory = config.key('path_cfg')["repo_pl_dir"]
master_filename = config.key('path_cfg')["pl_master_filename"]
master_directory = config.key('path_cfg')["dag_master_directory"]
branch = config.key('airflow_dag_repo')["branch"]
table_name = input_value['table_name']
new_filename = f"load_process_to_pl_{table_name}_dag.py"

#check & drop if folder exists
if FileOperations(repository_folder).is_directory_exists() :
   FileOperations(repository_folder).remove_directory()

#create a local directory for cloning
FileOperations(repository_folder).create_directory()

#cloning the git
# GitManager('airflow_dag_repo').clone()
# GitManager('airflow_dag_repo').pull(branch)