import psycopg2
from psycopg2 import sql

def get_connection():
    """Create and return a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            dbname="ekadeli",
            user="ekadeli",
            password="ekadeli2040",
            host="localhost",     # e.g., "localhost"
            port="5432"      # e.g., "5432"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
