import os 
import sys
sys.path.append(os.environ.get("ROOT_PATH"))
from datamart_module.test2 import testing

print(os.environ.get("ROOT_PATH"))
print(testing())
