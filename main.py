from flask import Flask, request, jsonify, make_response, render_template
import markdown.extensions.fenced_code
import tools.sql_queries as mysql

app = Flask(__name__)

# Render the markdwon
@app.route("/")
def readme ():
    readme_file = open("README.md", "r")
    return render_template('api.html')

# GET ENDPOINTS: SQL 
# Get All News Titles
@app.route('/news', defaults={'name': None})
@app.route("/news/<name>")
def get_news (name):
    if name:
        return jsonify(mysql.get_everything(name=name))
    else:
        return jsonify(mysql.get_everything())
# Get a string with all news titles
@app.route('/text', defaults={'name': None})
@app.route("/text/<name>", )
def get_alltext (name):
    if name:
        return jsonify(mysql.get_text(name))
    else:
        return jsonify(mysql.get_text(name))
### GET countries INFO
@app.route('/country', defaults={'name': None})
@app.route("/country/<name>", )
def get_countries(name):
    if name:
        return jsonify(mysql.get_country(name))
    else:
        return jsonify(mysql.get_country(name))
### GET SENTIMENT AVG and STD GROUPPED
@app.route('/sentiment', defaults={'name': None})
@app.route("/sentiment/<name>", )
def sentiment_get (name):
    if name:
        return jsonify(mysql.get_sentiment (name))
    else:
        return jsonify(mysql.get_sentiment (name))

####### PUT and GET People

@app.route("/people/", methods=["PUT", "GET"])
def people_put_get ():
    # Check method
    if request.method == 'PUT':
        put_request = request.args.to_dict()
        print(put_request)
        #passing to the function to add people
        add_people = mysql.add_people(put_request)
        return make_response(add_people)
    if request.method == 'GET':
        return jsonify(mysql.get_people())

if __name__ == "__main__":
    app.run(port=9000)