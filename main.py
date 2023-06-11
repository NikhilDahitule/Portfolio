from flask import Flask, render_template, request, send_file
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.4vw4y5c.mongodb.net/")
db = client['Portfolio']
collection = db['Portfolio']


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/download_resume')
def download_resume():
    try:
        return send_file('static/resume.txt', as_attachment=True)
    except FileNotFoundError:
        return "File not found"


@app.route('/contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    mobile_no = request.form.get('mobile')
    message = request.form.get('message')

    # Store the form data in MongoDB
    try:
        store_data_in_mongodb(name, email, mobile_no, message)
        return render_template('application_submitted.html', name=name)
    except Exception as e:
        error_message = f"An error occurred while storing data in MongoDB: {str(e)}"
        return render_template('error.html', error_message=error_message)


def store_data_in_mongodb(name, email, mobile_no, message):
    data = {
        'name': name,
        'email': email,
        'mobile_no': mobile_no,
        'message': message
    }
    collection.insert_one(data)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
