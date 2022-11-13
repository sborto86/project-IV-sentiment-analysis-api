import sqlalchemy as alch
import os
from dotenv import load_dotenv
from sqlalchemy.exc import OperationalError
load_dotenv()

dbName = "news_sentiment"
password="egassemSQL:12"

connectionData = f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)

# Try to connect to the database if doesn't exist create a new one

try:
    engine.connect()
except OperationalError:
    engine = alch.create_engine( f"mysql+pymysql://root:{password}@localhost")
    with engine.connect() as conn:
        conn.execute("commit")
        conn.execute(f"CREATE DATABASE {dbName}")
    engine = alch.create_engine(connectionData)

# Check if the tables exist if not, create tables

insp = alch.inspect(engine)
if not insp.has_table('country'):
    with engine.connect() as con:
        with open("data/country.sql") as file:
            query = alch.text(file.read())
            con.execute(query)
        with open("data/countries.sql") as file:
            query = alch.text(file.read())
            con.execute(query)
if not insp.has_table('people'):
    with engine.connect() as con:
        with open("data/people.sql") as file:
            query = alch.text(file.read())
            con.execute(query)
if not insp.has_table('news'):
    with engine.connect() as con:
        with open("data/news.sql") as file:
            query = alch.text(file.read())
            con.execute(query)