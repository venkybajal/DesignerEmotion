import os

from flask import Flask
from subprocess import call
import requests
import base64
import json
import image

app = Flask(__name__)

VLC_PATH = "vlc D:\\Designer\\vid\\test.avi --video-filter=scene --vout=dummy --start-time=3 --stop-time=15 --scene-ratio=10 --scene-path=D:\\Designer\\vid vlc://quit"


url = 'https://api.projectoxford.ai/emotion/v1.0/recognize'
img = open('test.png','rb').read()


headers = {'Content-Type': 'application/octet-stream','Ocp-Apim-Subscription-Key': 'edd62e5fd2a0449b890a59bf6cdfb24e'}

def hello():
    resp =  os.popen(VLC_PATH)
    return "Done"

@app.route('/')    
def mic_api():
	#print img is None
	r = requests.post(url, data=img, headers = headers)
	return str(r.json())


if __name__ == '__main__':
	app.debug = True
	app.secret_key = "kanilamba"
	app.run(host = '0.0.0.0', port = 5000)