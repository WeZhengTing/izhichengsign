# -*- coding: utf8 -*-
import json
from time import strftime,gmtime
import datetime
from  Izhichen import izhichen
from sign import sign
def main_handler(event, context):
    print("Received event: " + json.dumps(event, indent = 2)) 
    print("Received context: " + str(context))
    print("Hello world")
    izhichen('你的学号','你的名字写这')
    sign()
    times=(datetime.datetime.today()+datetime.timedelta(hours=8)).strftime("%Y-%m-%d_%H:%M")
    return(times)
