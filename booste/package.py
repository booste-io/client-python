import requests

def yolov3(image_path, owner, model_name):
    url = 'booste-corporation-v3-flask.zeet.app'
    files = {'file': open(image_path, 'rb')}
    payload = {"owner" : owner,
    "model_name" : model_name}
    response = requests.post(url, files=files, data=payload)
    return response