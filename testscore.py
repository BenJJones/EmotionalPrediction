import json
import re

def jsonParse(badJson):
    badJson = re.sub(r"{u\'", "\{\'", badJson)
    badJson = re.sub(r"u\'",r"\"", badJson)
    badJson =re.sub(r"\'",r"\"", badJson)
    print(badJson)
    return badJson

# import file
with open('exampledata2.json') as json_data:
    print(dir(json_data))
    parsed_emotions = json.loads(jsonParse(json_data.read()))
    
    # create list of threat scores
    threats = []

    for face in parsed_emotions:  
        # get numerical values for emotions
        anger = face['scores']['anger']
        contempt = face['scores']['contempt']
        disgust = face['scores']['disgust']
        fear = face['scores']['fear']
        happiness = face['scores']['happiness']
        neutral = face['scores']['neutral']
        sadness = face['scores']['sadness']
        surprise = face['scores']['surprise']
        print(contempt)

        # face data for cropping
        left = face['faceRectangle']['left']
        top = face['faceRectangle']['top']
        width = face['faceRectangle']['width']
        height = face['faceRectangle']['height']

        # assess threat 
        threat = (anger+contempt*10+disgust*100)*10000 - (happiness+neutral+surprise)*1
        threats.append(threat)
        print(threat)

