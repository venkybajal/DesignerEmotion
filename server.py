import os

from flask import Flask
from subprocess import call
import requests
import base64
import json
import image

app = Flask(__name__)

inp = 'D:\\Designer\\vid\\test.avi'

url = 'https://api.projectoxford.ai/emotion/v1.0/recognize'
img = open('test.png','rb').read()

def setPath(input_path,output_path = 'D:\\Designer\\vid'):
	return "vlc "+input_path+" --video-filter=scene --vout=dummy --start-time=3 --stop-time=15 --scene-ratio=10 --scene-path="+output_path+" vlc://quit" 

headers = {'Content-Type': 'application/octet-stream','Ocp-Apim-Subscription-Key': 'edd62e5fd2a0449b890a59bf6cdfb24e'}
@app.route('/getFeature/<sting:img_path>')   
def hello(img_path):
   
    resp =  os.popen(setPath(img_path))
    return "Done"

#@app.route('/')    
def mic_api():
	#print img is None
	r = requests.post(url, data=img,headers = headers)
	return str(r.json())


if __name__ == '__main__':
	app.debug = True
	app.secret_key = "kanilamba"
	app.run(host = '0.0.0.0', port = 5000)