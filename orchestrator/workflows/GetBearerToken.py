#    Name: GetBearerToken
#
#    Inputs:
#        None
#
#    Outputs:
#        bearerToken : string
#
#    Note: Moved to the getBearerToken.py action
#
#    Source: 
#       https://cloudblogger.co.in/2024/04/10/simplest-way-to-generate-bearer-token-in-orchestrator-for-aria-automation-cb10135/
#
import json
def handler(context, inputs):
    outputs = inputs
    btoken = context['getToken']()
    outputs['bearerToken'] = btoken
    return outputs
