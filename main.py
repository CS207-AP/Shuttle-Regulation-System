from flask import Flask, redirect
from flask import render_template
from flask import request
import models as dbHandler

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('homepage.html')


@app.route("/login", methods =["GET", "POST"])
def shuttle():
	if request.method == 'GET':
		return render_template('index.html')
	else:
	
		email = request.form['email']
		shuttletime = request.form['shuttletime']
		
		dbHandler.insertUser(email,shuttletime)

		
		
		id = dbHandler.retrieveID()
		for row in id:
			s=row  #not fully functional 
			
		
			count = dbHandler.countFunction()
			for row in count:
				if row[1] == shuttletime:
					if row[0]< 21:
						return render_template('confirmed.html')
					else:
						return render_template('waitlisted.html', id=s) 
				
			
		
		users  = dbHandler.retrieveUsers()
		return render_template('index.html',users=users)


	


@app.route("/admin", methods =["GET", "POST"])
def admin():
	
	count  = dbHandler.countFunction()
	return render_template('admin.html', count=count)


	
		


if __name__ == '__main__':
	app.run(debug = True, host='10.1.36.30')
