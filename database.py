from sqlalchemy import create_engine, text
from dotenv import dotenv_values

secrets = dotenv_values(".env")
con_string = secrets["DB_KEY"]
ca_cert_path = "/Users/filipsjostrand/ca.pem"

engine = create_engine(
    con_string,
    connect_args={"ssl": {"ca": ca_cert_path}},
)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = []
        for row in result.all():
            row_dict = row._asdict()
            jobs.append(row_dict)
    return jobs



