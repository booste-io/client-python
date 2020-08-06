import requests

def yolov3(image_path, owner, model_name):
    url = 'http://api.booste.io/inference/yolov3'
    files = {'file': open(image_path, 'rb')}
    payload = {"owner" : owner,
    "model_name" : model_name}
    response = requests.post(url, files=files, data=payload)
    return response