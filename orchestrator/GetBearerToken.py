import json
def handler(context, inputs):
    outputs = inputs
    btoken = context['getToken']()
    outputs['bearerToken'] = btoken
    return outputs
