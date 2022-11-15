# Sentiment Analysis of the Newspaper The Guardian

## Basic Information:
- Author: Sergi Portolés
- Project IV: for the Data Analytics Bootcamp in Ironhack (Sentiment Analyisis API)

## Objectives of the Project:

This project have two main objectives

1) Create a complete RestfulAPI with Flask ready to be deployed.

2) Test if Sentiment analysis can be used to infer the Political alignment of a newspaper.

## Data Sources Used:

| Source   |      Type      |  Data extracted  |
|----------|:-------------:|------:|
| [The Guardian](https://open-platform.theguardian.com/)| API | API of News published in the newspaper |

## Python Libraries Used:
 
| Library   |      Use     |
|----------|:-------------:|
| Pandas | Data Frame manipulation |
| Requests | HTTP Calls |
| Datetime | Classes for manipulating dates and times |
| Urllib | Url encode |
| dotenv | Import tokens |
| Os | Set paths |
| Tqdm | Show progress bar |
| Unidecode | Transform strings to unicode |
| Sqlalchemy | Connect with MySQL |
| Re | Regex's queries|
| Stylecloud | Generates Wordclouds |
| IPython | Visualize image |
| Matplotlib | Data visualization |
| Seaborn | Data visualization |

## File Structure:

### *main.py*

Python file that establishes the Flask local development server and the API endpoints

### *api-use-example.ipynb*

Jupyter notebook with examples on how to use this API and generate figures.

### ./src/

- ***queries.py*** &rarr; Functions to query The Guardian API
- ***sentiment.py*** &rarr; Functions to calculate the sentiment score.
- ***queries.py*** &rarr; Functions to generate a Worldcloud figure.
- ***score.py***  &rarr; Functions to generate figures with the sentiment scores

### ./data/

.sql files necessary to build the database structure

### ./tools/sql_queries.py

Functions to retrive the data from the database and populate it with new instances.

### ./config/sql_queries.py

Establishes the engine to connect with the SQL database

### ./img/

Folder to store all the figures generated

## How to use this repository

### Requirements:

1) Python verison 3.9 (might work in older versions)
2) MySQL (might work with other SQL database managment systems)
3) Python libraries specified before

### Initial Configuration:

1) Obtain a API token from [The Guardian Website](https://open-platform.theguardian.com/)
2) Create a .env file in the main folder of this repository with this structure:



<code>THE_GUARDIAN = `<API token>`</code>

<code>SQL = `<MySQL PASSWORD>`</code>


