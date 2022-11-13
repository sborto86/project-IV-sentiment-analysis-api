## Importing libraries
if "spacy" not in dir ():
    import spacy
if "nltk" not in dir ():
    import nltk
    from nltk.tokenize import word_tokenize
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
if "TextBlob" not in dir ():
    from textblob import TextBlob
if "pd" not in dir ():
    import pandas as pd

## loading spacy english dictionary

nlp = spacy.load("en_core_web_sm")

## loading stop words list

stop = nlp.Defaults.stop_words

def sentiment(text, type='pd.Series'):
    """
    Analyze sentiment of a text
    Arguments:
        text: str. text to be analyzed
        type: str. ('pd.Series', 'dic') type of response of the calculated parameters
    Returns:
        a dic or pd.Series with all the sentiment parameters calculated
    """

    # Creating text without stop words
    tokens = word_tokenize(text)
    tokens_nostop = [word for word in tokens if not word in stop]
    text_nostop = " ".join(tokens_nostop)

    #Analyzing sentiment
    blob = TextBlob(text_nostop).sentiment
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)
    dic = {
        'polarity': blob.polarity,
        'subjectivity': blob.subjectivity,
        'neg': scores['neg'],
        'neu': scores['neu'], 
        'pos': scores['pos'], 
        'compound': scores['compound']
    }
    if type == 'pd.Series':
        return pd.Series(dic.values())
    elif type == 'dic':
        return dic    
    else:
        print('Wrong type of response, returned a panda Series')
        return pd.Series(dic.values())

def add_sentiment(df, column='title'):
    '''
    Add sentiment calculations to a dataframe
    Arguments:
        df: pandas.DataFrame
        column (optional, default=title): column that contains the text to be analyzed
    Returns:
        pandas.DataFrame with 6 new columns
    """

    '''
    df[['polarity','subjectivity', 'neg', 'neu', 'pos', 'compound']] = df[column].apply(sentiment)
    return df
