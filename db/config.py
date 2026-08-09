import psycopg2

conn = psycopg2.connect(
    host="postgres",
    port=5432,
    database="cashly_db",
    user="cashly_user",
    password="cashly_password"
)