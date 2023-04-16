from flask import Flask, url_for, render_template

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/company')
def company():
    return render_template('company.html')

@app.route('/negative')
def negative():
    return render_template('negative.html')

@app.route('/reflection')
def reflection():
    return render_template('reflection.html')

@app.route('/effort')
def effort():
    return render_template('effort.html')

@app.route('/talktalk')
def talktalk():
    return render_template('talktalk.html')

# app.run(debug=True)
