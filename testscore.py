import json

parsed_emotions = dict()

with open('exampledata.json') as json_data:
    parsed_emotions = json.load(json_data)
    
    # get dict of scores
    scores = parsed_emotions[0]['scores']
    
    # get numerical values for emotions
    anger = scores['anger']
    contempt = scores['contempt']
    disgust = scores['disgust']
    fear = scores['fear']
    happiness = scores['happiness']
    neutral = scores['neutral']
    sadness = scores['sadness']
    surprise = scores['surprise']

    # face data for cropping
    left = parsed_emotions[0]['faceRectangle']['left']
    top = parsed_emotions[0]['faceRectangle']['top']
    width = parsed_emotions[0]['faceRectangle']['width']
    height = parsed_emotions[0]['faceRectangle']['height']

    # assess threat 

    threat = (anger*100+contempt*100+disgust*100) - (happiness+surprise)
    print(threat)




