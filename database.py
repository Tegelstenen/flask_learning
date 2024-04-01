from sqlalchemy import create_engine, text

con_string = "mysql+pymysql://avnadmin:AVNS_kPof7KK93MJNIRlbDaH@sensacareers-sensacareers.a.aivencloud.com:28183/defaultdb?charset=utf8mb4"
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



