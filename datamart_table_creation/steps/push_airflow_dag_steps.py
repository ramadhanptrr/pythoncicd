import sys
sys.path.append('./')
from datamart_module.git_module import GitManager
from datamart_module.file_handler import FileOperations
from utils.yaml_reader import YAMLConfigLoader
from datamart_module.input_handler import InputHandler

config = YAMLConfigLoader('./config.yaml')
config.load_config()
input_value = InputHandler.InputValue()
repository_folder = config.key('path_cfg')["repo_dir"]
destination_directory = config.key('path_cfg')["repo_pl_dir"]
master_directory = config.key('path_cfg')["dag_master_directory"]
master_filename = config.key('path_cfg')["pl_master_filename"]
branch = config.key('airflow_dag_repo')["branch"]
table_name = table_name = input_value['table_name']
new_filename = f'load_process_to_pl_{table_name}_dag.py'

if not FileOperations(destination_directory).is_file_exists(new_filename):
    FileOperations(destination_directory).copy(f"{master_directory}/{master_filename}")
    FileOperations(destination_directory).rename(master_filename,new_filename)
    GitManager('airflow_dag_repo').push(f"presentations/{new_filename}", branch)
else:
    sys.exit('file already exists')