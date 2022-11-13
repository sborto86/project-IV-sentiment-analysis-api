from flask import Flask, request, jsonify
import random
import numpy as np
import markdown.extensions.fenced_code
import tools.sql_queries as esecuele
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


app = Flask(__name__)

# Render the markdwon
@app.route("/")
def readme ():
    readme_file = open("README.md", "r")
    return markdown.markdown(readme_file.read(), extensions = ["fenced_code"])

# GET ENDPOINTS: SQL 
# SQL get everything
@app.route("/sql/")
def sql ():
    return jsonify(esecuele.get_everything())

@app.route("/sql/<name>", )
def lines_from_characters (name):
    return jsonify(esecuele.get_everything_from_character(name))


@app.route("/sa/<name>/", )
def sa_from_character (name):
    everything = esecuele.get_just_dialogue(name)
    #return jsonify(everything)
    return jsonify([sia.polarity_scores(i["dialogue"])["compound"] for i in everything])


####### POST
@app.route("/insertrow", methods=["POST"])
def try_post ():
    # Decoding params
    my_params = request.args
    scene = my_params["scene"]
    character_name = my_params["character_name"]
    dialogue = my_params["dialogue"]

    # Passing to my function: do the inserr
    esecuele.insert_one_row(scene, character_name, dialogue)
    return f"Query succesfully inserted"


if __name__ == "__main__":
    app.run(port=9000, debug=True)