from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_a_job_from_db

app = Flask(__name__)

@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, company_name="Sensa Careers")

@app.route("/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route("/jobs/<id>")
def show_job(id):
    job = load_a_job_from_db(id)
    if not job:
        return "Not found", 404
    else:
        return render_template('jobpage.html', job=job, company_name="Sensa Careers")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

