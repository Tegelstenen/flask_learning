import os
from sqlalchemy import create_engine, text

# Assuming you've set DB_KEY in Render's environment settings
con_string = os.environ["DB_KEY"]

engine = create_engine(
    con_string,
    connect_args={"ssl": {"ca": "ca.pem"}},
)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = []
        for row in result.all():
            row_dict = row._asdict()
            jobs.append(row_dict)
    return jobs