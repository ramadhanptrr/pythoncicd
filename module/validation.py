import os
business_key = os.getenv("business_key")
if (len(business_key) == 0) : 
    print('form required')
    sys.exit(-1)
else :
    print('passed')
