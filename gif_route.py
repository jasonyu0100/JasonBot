from flask_app import app
from flask import request, jsonify
import requests
import json

API_KEY = 'g1ubfI32am1y2bDQJxvWzf2xYR30CLMk'
URL = 'https://api.giphy.com/v1/gifs/search'

@app.route('/gif', methods=['POST','GET'])
def gif():
    name = request.values.get('text')
    response = requests.get(URL,params={
        'api_key':API_KEY,
        'q':name,
    })
    
    gif_url = response.json()['data'][0]['images']['original']['url'] #string of url 
    
    return_dict = jsonify({'text':'Here is your GIF!','attatchments':[{"image_url": gif_url}]})
    return return_dict

