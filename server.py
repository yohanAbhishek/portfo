import email
from email import message
from re import sub
from this import d
from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/thankyou.html')
    else:
        return 'oops'


def write_to_file(data):
    with open("database.txt", "a") as f:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = f.write(f'\n{email}, {subject}, {message}')
        
