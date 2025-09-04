# Name: getBearerToken
#
# Module: com.vmware.basic
#
# Runtime Environment: Python 3.10
#
# Type: Script
# 
# Return Type: string
#
import json
def handler(context, inputs):
    return context['getToken']()
