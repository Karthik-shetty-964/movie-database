import sqlite3
connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS 
movies(movie_id INTEGER PRIMARY KEY, movie_title TEXT, actor_name TEXT,
 year INTEGER, director_name TEXT)"""

cursor.execute(command1)
cursor.execute("INSERT INTO movies VALUES(1,'Charlie','Rakshit shetty',2021,'Kiran raj')")
cursor.execute("INSERT INTO movies VALUES(2,'Bahubali','prabas',1995,'Rajmouli')")
cursor.execute("INSERT INTO movies VALUES(3,'RRR','NTR',2001,'karan johar')")

cursor.execute("SELECT * FROM movies")
results = cursor.fetchall()

print(results)
print('Details of the movie in which  NTR was the lead actor')
cursor.execute("SELECT * FROM movies WHERE actor_name='NTR'")
res = cursor.fetchall()
print(res)