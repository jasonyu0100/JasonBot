from flask_app import app
from flask import request
from random import choice

@app.route('/rock_paper_scissors', methods=['GET','POST'])
def rock_paper_scissors():
    play = request.values.get('text')
    values = ['rock','scissors','paper']
    index = values.index(play)
    comp_play = choice(values)
    comp_index = values.index(comp_play)
    if index == comp_index-1 or (index == 2 and comp_index == 0):
        return f"The computer played {comp_play}, you win!"
    elif index == comp_index:
        return f"The computer played {comp_play}, it's a draw!"
    else:
        return f"The computer played {comp_play}, you lose!"