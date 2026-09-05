import os
import psycopg2
from dotenv import load_dotenv

# Load variables from a .env file into the process environment.
load_dotenv()

DB_CONFIG = {
    "host": os.environ.get("PGHOST", "localhost"),
    "port": os.environ.get("PGPORT", "5432"),
    "dbname": os.environ.get("PGDATABASE", "postgres"),
    "user": os.environ.get("PGUSER", "postgres"),
    "password": os.environ.get("PGPASSWORD", ""),
}

def get_connection():
    """Open and return a new database connection."""
    return psycopg2.connect(**DB_CONFIG)

def main():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute ("SELECT version();")
            row = cur.fetchone()
            print("Connected to:", row[0])
    finally:
        conn.close()

if __name__ == "__main__":
    main()