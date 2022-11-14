if "spacy" not in dir ():
    import spacy
if "nltk" not in dir ():
    import nltk
    from nltk.tokenize import word_tokenize
import re
import stylecloud
from IPython.display import Image

def token_leman(text, exclude=[]):
    '''
    Removes STOP words, Tokenize and Lemmaize a text str
    Arguments:
        text: str. text to tokenize
        exclude: list. list of words to remove from the text (such as names)
    Returns:
        str. cleaned
    '''
    # Retriving stop words
    nlp = spacy.load("en_core_web_sm")
    stop = nlp.Defaults.stop_words
    # Tokenize text and remove stop words        
    tokens = word_tokenize(text)
    tokens_nostop = [word for word in tokens if not word in stop and word not in exclude]
    #creating a spacy nlp object
    tokens_nostop = nlp(" ".join(tokens_nostop))
    #lemmanize the tokens
    lemmatized = [token.lemma_ for token in tokens_nostop]
    #clean for non text characters
    clean = [word for word in lemmatized if re.search('^[a-zA-Z][a-zA-Z]+$',word)]
    text2 = " ".join(clean)
    return text2

def word_cloud_gen(text, filename, icon="fa-user-secret", clean=True):
    '''
    Generates a word cloud of a given text and saves it to the img/ folder
    Atributes:
       text: str. text to generate the Word Cloud
       filename: str. name of the png file to generate
       icon: str. (default: fa-user-secret) name of the icon from font awseome
       clean: bool. Tokenize, Clean and Lemmize text
    '''
    if clean:
        text = token_leman(text)
    icon=f"fas {icon}"
    file=f"./img/{filename}.png"
    stylecloud.gen_stylecloud(text,
                            icon_name=icon,
                            palette='colorbrewer.diverging.Spectral_11',
                            output_name=file,
                            background_color='black',
                            gradient='horizontal')
    return Image(filename=file) 
