import sqlite3

# SQLite DB Name
db = "Main.db"

script = """
drop table if exists TemperatureData;
create table TemperatureData(
  id integer primary key autoincrement,
  SensorID text,
  Room text,
  Date text,
  Temperature text
);

drop table if exists HumidityData;
create table HumidityData(
  id integer primary key autoincrement,
  SensorID text,
  Room text,
  Date text,
  Humidity text
);

drop table if exists MotionData;
create table MotionData(
  id integer primary key autoincrement,
  SensorID text,
  Room text,
  Date text,
  Motion text
);

drop table if exists LightingData;
create table LightingData(
  id integer primary key autoincrement,
  SensorID text,
  Room text,
  Date text,
  Light text 
);

drop table if exists TempWarning; 
create table TempWarning(
  id integer primary key autoincrement,
  SensorID text,
  Room text,
  Date text,
  Temperature text
);

drop table if exists MotionWarning;
create table MotionWarning(
  id integer primary key autoincrement,
  SensorID text,
  Room text,
  Date text,
  Motion text
);
"""

connection = sqlite3.connect(db)
cursor = connection.cursor() # cursors be used to fetch data from the DBMS into an application and also to identify a row in a table to be updated or deleted
sqlite3.complete_statement(script) # runs the SQL
cursor.executescript(script)
cursor.close() # terminates connection
connection.close()