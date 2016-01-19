import os

from flask import Flask,jsonify
from subprocess import call
import requests
import base64
import json
import image
import glob

app = Flask(__name__)

inp = 'D:\\Designer\\vid\\test.avi'

#api
url = 'https://api.projectoxford.ai/emotion/v1.0/recognize'
headers = {'Content-Type': 'application/octet-stream','Ocp-Apim-Subscription-Key': 'edd62e5fd2a0449b890a59bf6cdfb24e'}

result = {}

#Get VLC Path
def setPath(input_path,output_path = 'D:\\Designer'):
	return "vlc "+input_path+" --video-filter=scene --vout=dummy --start-time=3 --stop-time=7 --scene-ratio=10 --scene-path="+output_path+" vlc://quit" 


def generateImages(img_path): 
    resp =  os.popen(setPath(img_path))
    return resp

def renameImageFiles():
	i = 0
	for name in glob.glob('*.png'):
		os.renames(name,str(i)+".png")
		i+=1
def removeImageFiles():
	i = 0
	for name in glob.glob('*.png'):
		os.remove(name)
		i+=1

@app.route('/')
@app.route('/getFeature/<string:img_path>')       
def mic_api(img_path = 'D:\\Designer\\vid\\test.mp4'):
	#print img is None
	removeImageFiles()
	generateImages(img_path)
	renameImageFiles()
	for name in glob.glob('*.png'):
		getScores(name)
	return str(result)

def getScores(filename):
	img = open(filename,'rb').read()
	if img is not None:
		r = requests.post(url, data=img,headers = headers)
		result[filename] =  r.text
	return "WError"


if __name__ == '__main__':
	app.debug = True
	app.secret_key = "kanilamba"
	app.run(host = '0.0.0.0', port = 5000)