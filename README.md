# Warmup Project
### Members: Mish Wilson, Lola Wesson, Bret Chandler, Steven De Jesus Bonilla


## General Setup
The Firebase module will need to be installed to run this application. 
Use `pip` (or `pip3`), Python's package manager to install firebase-admin in your virtual environment:

    pip install --upgrade firebase-admin

## Description of Data

For this assignment we decided on Musical Artists as our data. The information was sourced from Spotify's Top Artists of 2023, and we selected from the fields we wanted to use. In this project our fields are:
- Name: The full name of the musical artist.
- Location: The geographical location of the artist's origin.
- Songs: The artists top 3 songs.
- Genre (as an array): An array of the main genres the artist plays.
- Start of Career: The year the artist debuted.
- End of Career (optional): In cases where applicable, the year the artist concluded their career.

## Query Spec

Query Spec:
Our query language features keywords which act similarly to the familiar database language SQL, where we can select all records given certain conditions. 

The keywords we’ll use are Get, which is similar to select, if, which is similar to where, All, and various conditional operators, such as ==, &&, >>, <<, <=, >=, then we would have keywords for the program, which are Help and Quit. 

All is the operator we will use to display all information of a record from all fields instead of just one field, such as name. For example, if the user asks “Get Artist Names”, it would select only all artist names. On the other hand, users can use the All keyword to select all information for a given column. For example, “Get All if Artist Name == example”, would return every field of information for the given record.

 == is the operator we’ll use to compare a field of our data to user input. For example, “Get Artist Name if genre == pop”, which would provide all instances of artists where pop is one of their genres. An example for && would be “Get Artist Name if genre == pop && location == United States”, where this query selects all the artists whose one or more genres is pop, and their location is the United States. 

We would use <<, >>, <= or >= for our only numerical fields, start date and end date. The user would provide an integer and the conditional operators would select a record which is less than, greater than, less than or equal to, or greater than or equal to the integer provided by the user. 
The Help keyword would provide the list of keywords, and Quit quits the program.
