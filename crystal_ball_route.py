from flask_app import app
import random

@app.route('/cyrstal_ball',['GET','POST'])
def crystal_ball():
    if random.random() > 0.8:
        return "You are a lucky individual"
    elif random.random() < 0.2:
        return "You are quite an unlucky individual"
    else:
        return "You are normal"
