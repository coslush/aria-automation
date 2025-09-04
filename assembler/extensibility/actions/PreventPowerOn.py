#  Name: PreventPowerOn
#
#  Type: Script
# 
#  Interpreter: Python 3.10
#
#  Main function: handler
#
#  Source: 
def handler(context, inputs):
    outputs = inputs
    outputs['initialPowerOn'] = False
    return outputs
