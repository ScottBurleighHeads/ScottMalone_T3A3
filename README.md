# T3A3 - Implement a System with Data and Application Layers.

## ASSESSORS PLEASE REFER TO Workbook_and_evidence.md TO FIND EVIDENCE OF ALL REQUIREMENTS.

This program is a class assessment completed to progress in my course. This is not a fully functioning deployable application. Time was limited so the program is made up of components to complete the requirements of the assessment only.

This assessment is a python server-side web application that takes advantage of the flask framework and its components to build a web application. It is inspired by spotify and I have tried to build a database to represent the main components that I think spotify would have as illustrated in the diagram below.

![database diagram](docs/images/DatabaseDiagram.jpeg)

### Endpoints API:

##### User:

begin with: localhost:5000/user

|Endpoint|Application|
|---|---|
|/|Query all saved data for all users|
|/login|Login into the server and get a JWT token|
|/id|Find details on the user with the matching ID|
|/create|Creates a new user|
|/update/id|Update details of the user matching the ID|
|/delete/id|Delete a user|

##### Tracks:

begin with: localhost:5000/tracks

|Endpoint|Application|
|---|---|
|/|Get all tracks|

##### Playlist:

begin with localhost:5000/tracks

|Endpoint|Application|
|---|---|
|/id|Get the playlist of the user with the id number|
|/add_track|Add tracks to your personal playlist. You will need to be signed in with a JWT token|
|/delete_track|Remove the track from the playlist|

##### Artist:

begin with localhost:5000/artist

|Endpoint|Application|
|---|---|
|/Highest_profit|Find the artist with the highest profit|
|/Lowest_profit|Find the artist with the lowest profit|
|/Average_profit|Find the average profit of all the artist|
|/Sum_profit|Sum all the profit of all the artist|
|/Ordering|Application|
|/filtering|Finds all the artist that earn less then $40 million|
|/id/Albums|Find all the albums that the artist created|
|/id/Tracks|Find all the tracks that the artist created|

##### Albums:

begin with localhost:5000/albums

|Endpoints|Application|
|---|---|
|/id|Get all information in the database related to the album|
|/update/id|Update the details of the album with the matching id number|
|/id/tracks|Get all tracks that are on the album|

### Installation instructions:

##### Set up the environment:

|Instruction|commands|
|---|---|
|clone the program from github|https://github.com/ScottBurleighHeads/ScottMalone_T3A3.git|
|Enter working directory in the terminal |cd ScottMalone_T3A3|
|Update all the latest apt packages |sudo apt-get update|
|Install python |sudo apt-get python3.8|
|update pip|Sudo apt install python3-pip|
|Install python virtual environment|sudo apt-get install python3|
|Set up virtual environment|source venv/bin/activate|
|Install requirements|pip install -r requirements.txt|
|Set up flask env variables|export FLASK_APP=main.py|
|Set up flask env variables|export FLASK_ENV=development|
|Install the database|flask db create|
|Drop all the tables|flask db drop|
|Start the flask server|flask run|

##### Set up Postgres server and database

If you already have your own SQL application that is fine. Remember to create a database name t3a3 then follow the command in setup environment. You will need to set up the you DB_URI environment variable. Here is example DB_URI=postgresql+psycopg2://{Your admin}:{Your password}@localhost:5432/t3a3.

|Instruction|Commands|
|---|---|---|
|Install postgres|sudo apt-get install posgresql-13|
|start the postgres server|sudo service postgresql start|
|login|psql postgres|
|if login fails then |sudo -i -u postgres|
|then login|psql postgres|
|create a database t3a3 in the postgres raw sql|CREATE DATABASE t3a3;|

##### Flask commands

|Instruction|Commands|
|---|---|---|
|start virtual environment|source venv/bin/activate|
|Create the database tables|flask db create|
|Delete all database tables|flask db drop|
|To seen the database with fake data|flask db seed|




