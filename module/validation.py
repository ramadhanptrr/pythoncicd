import os
business_key = os.getenv("business_key")
if (business_key == '') : 
    print('form required')
    sys.exit(-1)
else :
    print('passed')
