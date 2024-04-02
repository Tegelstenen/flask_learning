import base64
from sqlalchemy import create_engine, text
from tempfile import NamedTemporaryFile
from dotenv import load_dotenv
import os

load_dotenv()

con_string = os.environ["DB_KEY"]
ca_cert_base64 = os.getenv("CA_CERT_BASE64")
if ca_cert_base64 is None:
    raise ValueError("CA_CERT_BASE64 environment variable is not set.")

ca_cert_decoded = base64.b64decode(ca_cert_base64)
with NamedTemporaryFile(delete=False, mode="wb", suffix=".pem") as temp_ca_file:
    temp_ca_file.write(ca_cert_decoded)
    ca_cert_path = temp_ca_file.name

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


def load_a_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {'val': id})
        row = result.all()
        if len(row) == 0:
            return None
        else:
            return row[0]._asdict()
