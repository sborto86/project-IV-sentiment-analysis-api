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

```txt
THE_GUARDIAN = <API token>
SQL = <MySQL PASSWORD>
```
3) Execute the main.py in the console:
```console
python main.py
```
4) Start sending request to the API. [Click here for Full documentation]()

## Database

The SQL database schema and tables are created automatically upon the first request.

Alternativetly, fulldatabase.sql file can be executed in MySQL to create the database

### SQL database schema

![SQL Diagram](./img/sql-schema.png)

## Results Summary

### Initial considerations

1) The following relevant political figures where used to perform this analysis: Liz Truss, Boris Johnson, Rishi Sunak, Keir Starmer, Angela Rayner, King Charles III, Queen Elisabeth II, Volodymyr Zelenskiy, Vladimir Putin, Xi Jinping.

2)  The analysis was performed in a two year window (starting November 2020) using the titles of the news published in The Guardian about each one of the political figures mentioned before.

3) Only the most representative figures of the analysis have been included in this file, all the figures generated can be found in the [jupyter file](./api-use-example.ipynb) and in the *img/* folder

### Individual Analysis

For each relevant political figure a WordCloud and a Sentiment Score figure was generated, all the figures can be found in the [jupyter file](./api-use-example.ipynb) and in the *img/* folder

Here are some examples:

#### Queen Elisabeth II Wordcloud

![Queen Elisabeth II Wordcloud](./img/queen-wordcloud.png)

#### Boris Johnson Wordcloud

![Donald Trump Wordcloud](./img/johnson-wordcloud.png)

#### Queen Elsiabeth II Sentiment

![Queen Elsiabeth II Sentiment](./img/queen-sentiment.png)

### UK Presidents Comparison

![UK Presidents Comparison](./img/presidents-compound.png)

#### Conclusions:

1) It seems that there are not big differences in the sentiment score between the last 3 UK presidents. 

2) Liz Truss was rellatively irrelevant in the newspaper before November 2021

### Labour vs Conservative Parties

![Labour vs Conservative](./img/party-compound.png)

#### Conclusions

1) There is a slightly higher compound sentiment score in the news about Labour Party leaders.

2) Lower sentiment scores would be expected for the parties in the oposition. However, the contrary was observed in that case.

### King Charles III vs Queen Elisabeth II

![King Charles III vs Queen Elisabeth II](./img/kq-compound.png)

#### Conclusions

1) It seems that Queen Elisabeth II have a slightly better compound sentiment score over time than King Charles III.

2) The compound sentiment score decreased abruptly  during the last 2 months of the analysis specially for Queen Elisabeth. This is probably realted with the news about her death and funeral as shown in the Wordcloud that are considered as negative sentiment score.

### Joe Biden vs Donald Trump

![Joe Biden vs Donald Trump](./img/usa-compound.png)

#### Conclusions

1) As expected Joe Biden have an slightly better compund sentiment score over time than Donald trumnp

2) Considering the political style of Donald Trump the sentiment score is suspringly close to Joe Biden with a profile more institutional


