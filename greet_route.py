from flask_app import app

@app.route('/greet', methods=['GET','POST'])
def greet():
    name = request.values.get('text')
    return f"Hello {name}!"