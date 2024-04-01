from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': '1',
        'title': 'Data Analyst',
        'location': 'Remote',
        'salary': '$100,000'
    },
    {
        'id': '2',
        'title': 'Data Scientist',
        'location': 'Stockholm',
        'salary': '$150,000'
    },
    {
        'id': '3',
        'title': 'Marketing Specialist',
        'location': 'Gothenburg'
    },
    {
        'id': '4',
        'title': 'Data Engineer',
        'location': 'Lund',
        'salary': '$120,000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name="Sensa Careers")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

