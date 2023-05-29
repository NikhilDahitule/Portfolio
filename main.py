from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/download_resume')
def download_resume():
    try:
        return send_file('static/resume.txt', as_attachment=True)
    except FileNotFoundError:
        return "File not found"
# @app.route('/contact',methods=['POST'])


# def SubmitContact():
#   data = request.form
#   add_application(id, data)
#   return render_template('application_submitted.html', apply=data, job=job)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
