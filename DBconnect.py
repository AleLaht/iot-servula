import pymysql.cursors
import pymysql
from datetime import datetime

# Connect to the database
connection = pymysql.connect(host='*IP-address*',
                             user='*username*',
                             password='*Password*',
                             db='sensori',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
def connect():
	date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpeg")
	with connection.cursor() as cursor:
		# Create a new record
		sql = "INSERT INTO `raw_data` (datetime, movement, kuvaurl) VALUES (%s, %s, %s)"
		cursor.execute(sql, (date, '1', 'kuvat/' + filename))

	# connection is not autocommit by default. So you must commit to save
	# your changes.
	connection.commit()
