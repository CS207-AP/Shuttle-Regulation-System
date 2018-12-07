import sqlite3 as sql

def insertUser(email,shuttletime):
	unauthorized = 0
	con = sql.connect("database.db")
	cur = con.cursor()

#database query to fetch all times that the particular email ID has registered for
#go through times list, see if the time entered exists on the list
#print error, you can't enter the same time again
	
	"""check = cur.execute("SELECT COUNT(Email), Email FROM users GROUP BY Shuttletime")
	for row in check:
		print (row)
		for row in check:
			if row[1] == email:
				if row[0]< 2:
					cur.execute("INSERT INTO users (Email,Shuttletime) VALUES (?,?)", (email,shuttletime))
					unauthorized = 0
				else:
					unauthorized = 1"""

	cur.execute("INSERT INTO users (Email,Shuttletime) VALUES (?,?)", (email,shuttletime))	
	con.commit()
	con.close()
	#return unauthorized
	
def countFunction(email, shuttletime):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT COUNT(Shuttletime), Shuttletime FROM users GROUP BY Shuttletime")
	count = cur.fetchall()
	#for row in count:
		#if row[1] == shuttletime:
		#	if row[0]< 2:
		#		confirm()

	
	con.close()
	return count


	
def retrieveUsers():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT Email, Shuttletime FROM users")
	users = cur.fetchall() 
	#count = cur.execute("SELECT COUNT(Shuttletime), Shuttletime FROM users GROUP BY Shuttletime")
	#print("TIME OF THE INPUT IS \n",cur)
	#for row in count:
		#print (row)
	# get your cur.execute('Select count group by datetime') over here. 
	# get a user_count list
	 
	con.close()
	# return an extra parameter (i.e. return two things from this function)
	# on the other end catch both, and use them both
	return users

#database request to get a column in sqlite
#send column to the count function in sqlite
#send column to the count function 