import requests, os
from uuid import uuid4
import numpy as np
import json
import base64

endpoint = 'https://booste-corporation-v3-flask.zeet.app'
# Endpoint override for development
if 'BoosteDevMode' in os.environ:
    endpoint = 'http://localhost'

def gpt2(in_string, length = 5, pretrained = True, model_id = None, user_id = None):
    global endpoint
    route = 'inference/pretrained/gpt2'
    url = os.path.join(endpoint, route)
    payload = {
        "string" : in_string,
        "length" : str(length)
    }
    response = requests.post(url, json=payload)
    out = response.content.decode()
    cleaned = str(out[2:len(out)-2])
    print(cleaned)
    offset = 0
    word = ""
    sequence = []
    for i in range(len(cleaned)):
        if i+offset < len(cleaned):
            if cleaned[i+offset] == '\\':
                if i+offset+1 < len(cleaned):
                    if cleaned[i+offset+1] == 'n':
                        if word != "" and word != " ":
                            sequence.append(word)
                            word = ""
                        sequence.append("\n")
                        offset += 1
            elif cleaned[i+offset] == " ":
                if word != "" and word != " ":
                    sequence.append(word)
                    word = ""
            else:
                word += cleaned[i+offset]
    if word != "" and word != " ":
        sequence.append(word)
        word = ""

    return sequence

# def yolov3(image_path, owner, model_name, labels, postprocess = True, obj_thresh = 0.5, nms_thresh = 0.5):
#     global endpoint
#     route = 'inference/yolov3'
#     url = os.path.join(endpoint, route)

#     files = {'file': open(image_path, 'rb')}
#     payload = {"owner" : owner,
#     "model_name" : model_name,
#     "labels" : json.dumps(labels),
#     "postprocess" : postprocess,
#     "obj_thresh" : obj_thresh,
#     "nms_thresh" : nms_thresh,
#     "image_name" : image_path}

#     response = requests.post(url, files=files, data=payload)

#     r = response.json()

#     if postprocess:
#         boxes = r['boxes']
#         img_data = base64.b64decode(r['image'])
#         path_out = image_path[:-4] + '_detected' + image_path[-4:]
#         with open(path_out, "wb") as fh:
#             fh.write(img_data)        
#         return boxes

#     else:
#         out1 = np.reshape(a = r['output1'], newshape = r['output1shape'])
#         out2 = np.reshape(a = r['output2'], newshape = r['output2shape'])
#         out3 = np.reshape(a = r['output3'], newshape = r['output3shape'])
#         return {"output_1":out1,"output_2":out2,"output_3":out3}
