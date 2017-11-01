from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET','POST'])
def add_new():
    if request.method == 'POST':
        #parse form
    else:
        return render_template('add_new.html')

def handle_query(query):
    pass
