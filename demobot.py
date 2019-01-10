from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/greet')
def greet():
    name = request.values.get('text')
    return f"Hello {name}!"

@app.route('/weather')
def weather():
    temp = int(request.values.get('text'))
    if temp > 30:
        return f"Ooo that's hot. That's hot"
    else:
        return f"The temperature is {temp}"


if __name__ == '__main__':
    app.run()