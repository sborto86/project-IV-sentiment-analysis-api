from config.sql_connection import engine
import pandas as pd
from src.queries import get_guardian_articles
from src.sentiment import add_sentiment

def get_everything ():
    query = """
            SELECT time AS date, title, people.fname AS `name`, country.countryname AS country, people.party_name AS party, polarity, subjectivity, news.neg, neu, pos, compound 
            FROM news
            JOIN people
            ON news.idpeople = people.idpeople
            JOIN country
            ON people.countrycode = country.countrycode;
            """
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_country(name=None):
    query = """
            SELECT * FROM country
            """
    if name:
        query +=f"""WHERE countryname = '{name}';
                """
    else: 
        query +=';'
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_text(name=None):
    query = """
            SELECT people.fname AS `name`, GROUP_CONCAT(title SEPARATOR ' ') AS all_titles 
            FROM news
            JOIN people
            ON news.idpeople = people.idpeople"""
    if name:
        query += f"""
            WHERE people.fname = '{name}'"""
    query += """
            GROUP BY people.idpeople;
            """
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_sentiment (name=None):
    query = """
            SELECT people.fname AS `name`, country.countryname AS country, people.party_name AS party, AVG(polarity) AS polarity, STDDEV(polarity), AVG(subjectivity) AS subjectivity, STDDEV(subjectivity), AVG(news.neg) AS `neg`, STDDEV(`neg`), AVG(neu) AS neu, STDDEV(neu), AVG(pos) AS pos, AVG(compound) AS compound, STDDEV(compound) 
            FROM news
            JOIN people
            ON news.idpeople = people.idpeople
            JOIN country
            ON people.countrycode = country.countrycode"""
            
    if name:
        query += f"""
                    WHERE people.fname = '{name}'"""
    query += """
            GROUP BY people.idpeople;
            """
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_people ():
    query = """
            SELECT fname, countrycode, party_name 
            FROM people;
            """
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def add_people (dic):
    """
    Function to add a known people in the database.
    Arguments:
        dic: dic in the specified format
    Returns:
        str specifing if the request was succesful or not
    """
    ## Validating input:
    if 'name' in dic and type(dic['name']) == str:
        pass
    else:
        return "Bad input you should pass a dictionary with the correct values", 400
    if 'country' in dic and type(dic['country']) == str and len(dic['country']) == 3:
        pass
    else:
        return "Bad input country should be specified in 3 letter ISO code", 400
    if 'party' in dic and type(dic['party']) == str:
        pass
    else:
        dic['party']==None

    ## Adding request to SQL database people table

    try: 
        query = f"""
            INSERT INTO people (fname, countrycode, party_name) 
            VALUES 
            ('{dic['name']}', '{dic['country']}', '{dic['party']}') 
            ON DUPLICATE KEY UPDATE countrycode='{dic['country']}', party_name='{dic['party']}';
        """
        engine.execute(query)
        print(f"{dic['name']} correctly introduced in the database")
    except Exception as e:
        return f"There was a problem adding {dic['name']} in the database --> {type(e)} : {e}", 503
    id = engine.execute(f"SELECT idpeople FROM people WHERE fname='{dic['name']}';").first()[0]
    
    ## Feching the information from the Guardian API to add to the news table
    
    try:
        df = get_guardian_articles(dic['name'], id)
        print(f"{dic['name']} news correctly fetched from The Guardian API")
    except Exception as e:
        return f"There was a problem geeting the news for {dic['name']} in The Guardian API --> {type(e)} : {e}", 503
    if not df:
        return f"There was a problem geeting news for {dic['name']} in The Guardian API", 503
    
    df = pd.DataFrame(df)

    ## Formating time column

    df['time'] = df['time'].apply(pd.to_datetime)

    ## Adding sentiment columns
    try:
        df = add_sentiment(df)
        print('sentiment calculation succefully added')
    except Exception as e:
        return f"There was a problem adding sentiment columns in the dataframe --> {type(e)} : {e}", 503
    
    ## Adding to SQL database
    try:
        df.to_sql('news', engine, schema='news_sentiment', if_exists='append', index=False, index_label=None, method="multi")
        return f"{dic['name']} Succefully added to the database", 201
    except Exception as e:
        return f"There was a problem adding news to the SQL database --> {type(e)} : {e}", 503