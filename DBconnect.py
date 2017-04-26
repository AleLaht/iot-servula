import pymysql.cursors
import pymysql
from datetime import datetime

date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Connect to the database
connection = pymysql.connect(host='ip',
                             user='pi',
                             password='salasana',
                             db='sensori',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def connect():
	with connection.cursor() as cursor:
        	# Create a new record
        	sql = "INSERT INTO `raw_data` (datetime, movement) VALUES (%s, %s)"
        	cursor.execute(sql, (date, '1'))

		# connection is not autocommit by default. So you must commit to save
		# your changes.
		connection.commit()

		connection.close()
