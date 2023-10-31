import sys
sys.path.append('./')
import yaml

class YAMLConfigLoader:
    def __init__(self,file_path):
        self.file_path = file_path
        self.yaml_data = None

    def load_config(self):
        try:
            with open(self.file_path,'r') as yaml_file:
                self.yaml_data = yaml.safe_load(yaml_file)
        except FileNotFoundError:
            print(f"file '{self.file_path}' not found")
        except Exception as e:
            print(f"An error occurred while loading the YAML file: {e}")

    def key(self, variable_name):
        if self.yaml_data:
            return self.yaml_data.get(variable_name)