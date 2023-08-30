import os
import sys
business_key = os.getenv("business_key")
print("validation starts")
if (business_key is None) : 
    sys.exit('Column is Required')
else :
    print('passed -',business_key)
    