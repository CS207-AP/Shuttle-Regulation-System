from flask import Flask, redirect
from flask import render_template
from flask import request
import models as dbHandler

app = Flask(__name__)

"""@app.route('/', methods=['POST', 'GET'])
def home():
	if request.method=='POST':
		email = request.form['email']
		shuttletime = request.form['shuttletime']
		dbHandler.insertUser(email,shuttletime)
		users = dbHandler.retrieveUsers()
		return render_template('index.html',users=users)
	else:
		return render_template('index.html') """

@app.route("/")
def index():
	return render_template('homepage.html')


@app.route("/login", methods =["GET", "POST"])
def shuttle():
	if request.method == 'GET':
		return render_template('index.html')
	else:
	#if request.method=='POST':
		email = request.form['email']
		shuttletime = request.form['shuttletime']
		unauthorized = dbHandler.insertUser(email,shuttletime)

		"""if unauthorized == 1:
			return render_template('unauthorized.html')"""
	
		count = dbHandler.countFunction(email,shuttletime)
		for row in count:
			if row[1] == shuttletime:
				if row[0]< 20:
					return render_template('confirmed.html')
				else:
					return render_template('waitlisted.html') 
			

		users  = dbHandler.retrieveUsers()
		return render_template('index.html',users=users)


@app.route("/admin", methods =["GET", "POST"])
def admin():
	if request.method == 'GET':
		return render_template('index.html')
	else:
	#if request.method=='POST':
		email = request.form['email']
		shuttletime = request.form['shuttletime']
		unauthorized = dbHandler.insertUser(email,shuttletime)
		users  = dbHandler.retrieveUsers()
		return render_template('admin.html',users=users)


	
		


if __name__ == '__main__':
	app.run(debug = True, host='10.1.36.30')
