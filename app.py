from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = []
        for row in result.all():
            row_dict = row._asdict()
            jobs.append(row_dict)
    return jobs

@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, company_name="Sensa Careers")

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

