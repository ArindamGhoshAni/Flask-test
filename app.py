from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/', methods=['POST'])
def submit_data():
    name = request.form['name']
    email = request.form['email']
    with open('data.csv', mode='a', newline='') as data_file:
        data_writer = csv.writer(data_file)
        data_writer.writerow([name, email])
    return 'Data submitted successfully!'
