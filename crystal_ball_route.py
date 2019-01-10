from flask_app import app
import random

@app.route('/crystal',['GET','POST'])
def crystal_ball():
    if random.random() > 0.8:
        return "You are a lucky individual"
    elif random.random() < 0.2:
        return "You are quite an unlucky individual"
    else:
        return "You are normal"
