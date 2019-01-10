from flask_app import app

@app.route('/', methods=['GET','POST'])
def hello():
    return "Hello!"