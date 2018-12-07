import sqlite3 as sql

def insertUser(email,shuttletime):
	unauthorized = 0
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("INSERT INTO users (Email,Shuttletime) VALUES (?,?)", (email,shuttletime))	
	
			
	con.commit()
	con.close()
	
	
def countFunction():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT COUNT(Shuttletime), Shuttletime FROM users GROUP BY Shuttletime ORDER BY Shuttletime ASC")
	count = cur.fetchall()
	con.close()
	return count
	

def retrieveID():
	con = sql.connect("database.db")
	cur = con.cursor()  
	cur.execute("SELECT id FROM users ORDER BY id DESC LIMIT 1")
	id = cur.fetchone()
	con.close()
	return id



def retrieveUsers():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT Email, Shuttletime FROM users")
	users = cur.fetchall()  
	con.close()
	return users

