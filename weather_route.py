from flask_app import app

@app.route('/weather', methods=['GET','POST'])
def weather():
    temp = int(request.values.get('text'))
    if temp > 30:
        return f"Ooo that's hot. That's hot"
    else:
        return f"The temperature is {temp}"