import json
import sqlite3
from datetime import datetime

# SQLite DB Name
db =  "Main.db"

class DatabaseManager():
	def __init__(self):
		self.conn = sqlite3.connect(db)
		self.conn.execute('pragma foreign_keys = on')
		self.conn.commit()
		self.cur = self.conn.cursor()
		
	def modifyDB(self, sql_query, args=()):
		self.cur.execute(sql_query, args)
		self.conn.commit()
		return

	def __del__(self):
		self.cur.close()
		self.conn.close()
 
# push temperature into database
def PushTempData(jsonData):
	# parse data 
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['Sensor_ID']
	Room = json_Dict['Room']
	Date = json_Dict['Date']
	Temperature = json_Dict['Temperature']
	# push into DB table

	dbObj = DatabaseManager()
	if int(Temperature) <15 or int(Temperature)>25:
		dbObj.modifyDB("insert into TempWarning (SensorID,Room, Date, Temperature) values (?,?,?,?)", [SensorID, Room, Date, Temperature])
		print ("Inserted temperature into TempWarning.")
	else:
		dbObj.modifyDB("insert into TemperatureData (SensorID,Room, Date, Temperature) values (?,?,?,?)", [SensorID, Room, Date, Temperature])
		print ("Inserted temperature into TemperatureData.")
	del dbObj
	
# push humdity data into database
def PushHumidityData(jsonData):
	# parse data 
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['Sensor_ID']
	Room = json_Dict['Room']
	Date = json_Dict['Date']
	Humidity = json_Dict['Humidity']
	
	# push into DB table
	dbObj = DatabaseManager()
	dbObj.modifyDB("insert into HumidityData (SensorID,Room, Date, Humidity) values (?,?,?,?)", [SensorID, Room, Date, Humidity])
	del dbObj
	print("Inserted Humidity Data into Database.")
	print("")

def PushMotionData(jsonData):
	# parse data 
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['Sensor_ID']
	Room = json_Dict['Room']
	Date = json_Dict['Date']
	Motion = json_Dict['Motion']
	
	# push into DB table
	dbObj = DatabaseManager()
	dbObj.modifyDB("insert into MotionData (SensorID,Room, Date, Motion) values (?,?,?,?)", [SensorID, Room, Date, Motion])
	del dbObj
	print("Inserted Motion Data into Database.")

def RecieveData(Topic, jsonData):
	if Topic == "Home/BedRoom/Temperature" or Topic == "Home/LivingRoom/Temperature" :
		PushTempData(jsonData)
	elif Topic == "Home/BedRoom/Humidity" or Topic == "Home/LivingRoom/Humidity":
		PushHumidityData(jsonData)
	elif Topic == "Home/BedRoom/Motion":
		PushMotionData(jsonData)
	elif Topic == "Home/LivingRoom/Motion":
		PushMotionDataLiving(jsonData)

def PushMotionDataLiving(jsonData):
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['Sensor_ID']
	Room = json_Dict['Room']
	Date = json_Dict['Date']
	Motion = json_Dict['Motion']
	# parse date to only have time
	
	newTime= (Date.split())
	actualtime = newTime[1] # get only the time
	checktime = actualtime.replace(":",".") # convert to decimal
	checktime = checktime[:-3] # remove the micro second
	dbObj = DatabaseManager()
	if (float(checktime) >float(22) or float(checktime)< float(4)) and Motion==1: # checks if time between 10pm and 4am and that there is motion 1 means that there is motion 0 means no motion
		print("Intruder")
		dbObj.modifyDB("insert into MotionWarning (SensorID,Room, Date, Motion) values (?,?,?,?)", [SensorID, Room, Date, Motion])
		print ("Inserted Motion warning into Database.")
	else:
		dbObj.modifyDB("insert into MotionData (SensorID,Room, Date, Motion) values (?,?,?,?)", [SensorID, Room, Date, Motion])
		print ("Inserted Motion Data into Database.")
	del dbObj