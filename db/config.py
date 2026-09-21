import psycopg2
import os

databaseUrl = os.getenv("DATABASE_URL")

conn = psycopg2.connect(databaseUrl)