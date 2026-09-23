import os
from psycopg2.pool import ThreadedConnectionPool

databaseUrl = os.getenv("DATABASE_URL")
pool = ThreadedConnectionPool(minconn=1, maxconn=10, dsn=databaseUrl)

def getConn():
    return pool.getconn()

def putConn(conn):
    pool.putconn(conn)