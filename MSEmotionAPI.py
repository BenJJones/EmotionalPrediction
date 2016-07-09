import httplib, urllib, base64  

# Image to analyse (body of the request)

body = '{\'URL\': \'https://cbspittsburgh.files.wordpress.com/2016/07/dallas-ambush-shooting-545477342.jpg?w=946\'}'

# API request for Emotion Detection

headers = {
   'Content-type': 'application/json',
}

params = urllib.urlencode({
   'subscription-key': 'f5fb2f9eb2b54c6c9e09cfb23f8d4a37',
   #'faceRectangles': '',
})

try:
   conn = httplib.HTTPSConnection('api.projectoxford.ai')
   conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body , headers)
   response = conn.getresponse()
   print("Send request")

   data = response.read()
   print(data)
   conn.close()
except Exception as e:
   print("[Errno {0}] {1}".format(e.errno, e.strerror))