__author__ = 'Kaiqun'

import pyodbc

with open('DBCredentials/MSSQL', 'r') as crdts:
	CrStr = crdts.readline()
	DBDriver = CrStr.split(',')[0]
	DBServer = CrStr.split(',')[1]
	DBDatabase = CrStr.split(',')[2]
	DBUid = CrStr.split(',')[3]
	DBPwd = CrStr.split(',')[4]

connStr = 'DRIVER={%s};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s' % (DBDriver, DBServer, DBDatabase, DBUid, DBPwd)

cnxn = pyodbc.connect(connStr)
cursor = cnxn.cursor()


def InsertionHandle(StationID, DateT, ChannelIndex, CountList):
	for i in range(len(CountList)):
		dataInsert(StationID, DateT, ChannelIndex, i + 1, CountList[i])


def dataInsert(StationID, DateT, ChannelIndex, Class, Count):
	try:
		InsertCommand = "insert into [speed].[tirs].[LoopsClass_new] values ('" + StationID + "','" + DateT + "'," + str(ChannelIndex) + "," + str(Class) + "," + str(Count) + ")"
		cursor.execute(InsertCommand)
		cnxn.commit()
		return "OK"
	except Exception, e:
		print str(e.message)
		return e.message