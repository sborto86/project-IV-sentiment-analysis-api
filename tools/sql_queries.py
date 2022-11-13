from config.sql_connection import engine
import pandas as pd

def get_everything ():
    query = """SELECT * FROM users;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_everything_from_character (name):
    query = f"""SELECT * 
    FROM users
    WHERE character_name = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_just_dialogue (name):
    query = f"""SELECT dialogue 
    FROM users
    WHERE character_name = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def insert_one_row (scene, character_name, dialogue):
    query = f"""INSERT INTO users
     (scene, character_name, dialogue) 
        VALUES ({scene}, '{character_name}', '{dialogue}');
    """
    engine.execute(query)
    return f"Correctly introduced!"


