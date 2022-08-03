# save this as app.py
import flask
from flask import render_template, request, redirect, url_for
import os
import random

app = flask.Flask(__name__)


def return_img_stream(img_local_path):
    import base64
    with open(img_local_path, 'rb') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream).decode()
    return img_stream


img_list = os.listdir('princess_img')
img_25_list = os.listdir('princess_img_25')
answer = ''

@app.route('/')
def index():
    global answer
    random.shuffle(img_list)
    random.shuffle(img_25_list)
    img_25_path = f'princess_img_25/{img_25_list[0]}'
    answer = img_25_list[0].replace('_25.png', '')
    choose = img_25_list[:4]
    random.shuffle(choose)
    for i, c in enumerate(choose):
        choose[i] = choose[i].replace('_25.png', '')
    
    choose = {
        'num1': choose[0],
        'num2': choose[1],
        'num3': choose[2],
        'num4': choose[3],
    }

    img_stream = return_img_stream(img_25_path)
    return render_template('index.html', img_stream=img_stream, choose=choose)


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    global answer
    guess = request.form['char']
    content = {
        'TF': guess == answer,
        'answer': answer,
    }
    answer_img = return_img_stream(f'princess_img/{answer}.png')
    
    return render_template('result.html', img=answer_img, content=content)
    
    
    
    
    
if __name__ == '__main__':
    app.run()
