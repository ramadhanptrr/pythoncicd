import os
import sys
business_key = os.getenv("business_key")
print("validation starts")
if (len(business_key) != 0) : 
    print('passed')
else :
    print("Required")