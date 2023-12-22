import os 
import sys
sys.path.append(os.environ.get("ROOT_PATH"))
import test2

print(os.environ.get("ROOT_PATH"))
print(test2.testing())
