import os
import shutil

class FileOperations:
    def __init__(self,path):
        self.path = path

    def is_directory_exists(self):
        if os.path.exists(self.path) and os.path.isdir(self.path):
            return True
        return False
    def is_directory_empty(self):
        items = os.listdir(self.path)
        return not items

    def is_file_exists(self,filename):
        return os.path.isfile(f"{self.path}/{filename}")

    def create_directory(self):
        if not self.is_directory_exists():
            print(f"creating directory {self.path}")
            return os.makedirs(self.path)
        else :
            return f"directory [{self.path}] is already exists"

    def remove_directory(self):
        if self.is_directory_exists():
            if self.is_directory_empty():
                os.rmdir(self.path)
            else:
                shutil.rmtree(self.path)
            print(f"removing {self.path}..")
            return True
        else:
            return f"directory [{self.path}] is not exist"

    def join_filename(self,filename):
        return os.path.join(self.path, filename)

    def copy(self,source_path):
        try:
            shutil.copy(source_path, self.path)
            print(f"File copied {source_path}")
        except FileNotFoundError:
            print("Source file not found.")
        except shutil.SameFileError:
            print("Source and destination are the same file.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def rename(self,old_name,new_name):
        try:
            os.rename(f"{self.path}/{old_name}",f"{self.path}/{new_name}")
            print(f"rename from {old_name} to {new_name}")
            return True
        except FileNotFoundError:
            print(f"{self.path}/{old_name} file not found.")
            return False