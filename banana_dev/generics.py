from glob import glob
import requests
import time
import os
import json
from uuid import uuid4
from copy import deepcopy

# Constants
# Default config
ENDPOINT = 'https://api.banana.dev/'
VERBOSITY = False

# Globals
# Config
endpoint = None
verbosity = None
log_time0 = None
log_time_prev = None

# Log util
def log_it(desc:str, body:str=None):
    if not verbosity:
        return 

    # First call    
    global log_time0
    global log_time_prev
    if desc =='start':
        log_time0 = time.time()
        log_time_prev = log_time0
        print('time | duration | split')
    
    # Subsequent calls
    log_time = time.time()
    clock = time.localtime(log_time)
    timer = log_time - log_time0
    split = log_time - log_time_prev
    log_time_prev = log_time
    print(f'{time.strftime("%H:%M:%S", clock)} {time.strftime("%M:%S", time.gmtime(timer))} {split:.2f} - {desc}')
    if body:
        print(body)

# Reset config to defaults
def reset_config():
    global endpoint
    global verbosity
    endpoint = ENDPOINT
    verbosity = VERBOSITY

# Custom config for development
def custom_config(**config):
    reset_config()

    if config.__len__() != 0:
        print('Dev Mode: custom config')
    else:
        return
    
    # Set custom values else revert to default
    global endpoint
    if 'url' in config: 
        url = config.get('url')
        if url  == 'local':
            endpoint = 'http://localhost/'
        else:
            endpoint = url
    
    global verbosity
    if 'verbosity' in config: 
        verbosity = config.get('verbosity').lower() == 'true'    

    print(f'url: {endpoint}')
    print(f'verbosity: {verbosity}')

    if verbosity:
        log_it(desc='start')
    
# THE MAIN FUNCTIONS
# ___________________________________

def run_main(api_key, model_key, model_inputs, strategy, **config):
    custom_config(**config)

    call_id = start_api(api_key, model_key, model_inputs, strategy)
    log_it(f'call_id: {call_id}')

    while True:
        dict_out = check_api(api_key, call_id)
        if dict_out['message'].lower() == "success":
            log_it(f'end')
            return dict_out

def start_main(api_key, model_key, model_inputs, strategy):
    call_id = start_api(api_key, model_key, model_inputs, strategy)
    return call_id

def check_main(api_key, call_id):
    dict_out = check_api(api_key, call_id)
    return dict_out


# THE API CALLING FUNCTIONS
# ________________________

# Takes in start params, returns call ID
def start_api(api_key, model_key, model_inputs, strategy):
    global endpoint
    route_start = "start/v2/"
    url_start = endpoint + route_start

    payload = {
        "id": str(uuid4()),
        "created": time.time(),
        "apiKey" : api_key,
        "modelKey" : model_key,
        "modelInputs" : model_inputs,
        "strategy": strategy,
    }

    response = requests.post(url_start, json=payload)

    if response.status_code != 200:
        raise Exception("server error: status code {}".format(response.status_code))

    try:
        out = response.json()
    except:
        raise Exception("server error: returned invalid json")

    try:
        if "error" in out['message'].lower():
            raise Exception(out['message'])
        call_id = out['callID']
        return call_id
    except:
        raise Exception("server error: Failed to return call_id")

# The bare async checker.
def check_api(api_key, call_id):
    global endpoint
    route_check = "check/v2/"
    url_check = endpoint + route_check
    # Poll server for completed task

    payload = {
        "id": str(uuid4()),
        "created": int(time.time()),
        "longPoll": True,
        "callID": call_id, 
        "apiKey": api_key
    }
    response = requests.post(url_check, json=payload)

    if response.status_code != 200:
        raise Exception("server error: status code {}".format(response.status_code))

    try:
        out = response.json()
        try:
            out_log = deepcopy(out)
            out_log['modelOutputs'][0]['output']='-hidden by log_it-'
            log_it('check_api loop',out_log)
        except:
            log_it('check_api loop',out)

    except:
        raise Exception("server error: returned invalid json")

    try:
        if "error" in out['message'].lower():
            raise Exception(out['message'])
        return out
    except Exception as e:
        raise e