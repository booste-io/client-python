from glob import glob
import requests
import time
import os
import json
from uuid import uuid4

# Constants
# Default config
ENDPOINT = 'https://api.banana.dev/'
VERBOSITY = False

# Globals
# Config
endpoint = ENDPOINT
verbosity = VERBOSITY

# Custom config for development
def custom_config(**config):
    if config.__len__() != 0:
        print('Dev Mode: custom config')

    # Set custom values else revert to default
    global endpoint
    if 'url' not in config: 
        endpoint = ENDPOINT
    else:
        url = config.get('url')
        if url  == 'local':
            endpoint = 'http://localhost/'
        else:
            endpoint = url
    
    global verbosity
    if 'verbosity' not in config: 
        verbosity = VERBOSITY
    else:
        verbosity = config.get('verbosity').lower() == 'true'

    # Print all config if any setting has been customized
    if config.__len__() != 0:
        print(f'url: {endpoint}')
        print(f'verbosity: {verbosity}')
        
    
# THE MAIN FUNCTIONS
# ___________________________________

def run_main(api_key, model_key, model_inputs, strategy, **config):
    custom_config(**config)

    call_id = start_api(api_key, model_key, model_inputs, strategy)
    while True:
        dict_out = check_api(api_key, call_id)
        if dict_out['message'].lower() == "success":
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
    except:
        raise Exception("server error: returned invalid json")

    try:
        if "error" in out['message'].lower():
            raise Exception(out['message'])
        return out
    except Exception as e:
        raise e