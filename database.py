from sqlalchemy import create_engine


# Replace the placeholders with your actual Aiven database credentials and paths
con_string = "mysql+pymysql://avnadmin:AVNS_kPof7KK93MJNIRlbDaH@sensacareers-sensacareers.a.aivencloud.com:28183/defaultdb?charset=utf8mb4"

# Path to the Aiven CA certificate you downloaded
ca_cert_path = "/Users/filipsjostrand/ca.pem"

engine = create_engine(
    con_string,
    connect_args={"ssl": {"ca": ca_cert_path}},
)



