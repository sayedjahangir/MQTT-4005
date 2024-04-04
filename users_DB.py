import sqlite3

# SQLite DB Name
db = "users.db"

script = """
drop table if exists UserData;
create table UserData(
  id integer primary key autoincrement,
  Username text,
  Password text
);
"""

connection = sqlite3.connect(db)
cursor = connection.cursor() # cursors be used to fetch data from the DBMS into an application and also to identify a row in a table to be updated or deleted
sqlite3.complete_statement(script) # runs the SQL
cursor.executescript(script)
cursor.close() # terminates connection
connection.close()