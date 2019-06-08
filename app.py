from flask import Flask, request, render_template, jsonify
#from functions import *
from DB.Gestor import *
from DB.Gestor import Person
import sqlite3

app =Flask(__name__)

@app.route('/')
def index():
	return app.send_static_file("index.html")
@app.route('/crt_group')
def crt_group():
	return app.send_static_file("crt_group.html")
@app.route('/edt_group')
def edt_group():
	return app.send_static_file("edt_group.html")
@app.route('/rmv_group')
def rmv_group():
	return app.send_static_file("rmv_group.html")
@app.route('/vw_group')
def vw_group():
	return app.send_static_file("vw_group.html")
@app.route('/crt_person')
def crt_person():
	return app.send_static_file("crt_person.html")
@app.route('/edt_person')
def edt_person():
	return app.send_static_file("edt_person.html")
@app.route('/rmv_person')
def rmv_person():
	return app.send_static_file("rmv_person.html")
@app.route('/vw_person')
def vw_person():
	return app.send_static_file("vw_person.html")


@app.route('/insert', methods = ['POST'])
def insert():
	_age = request.form['age']
	_id = request.form['id']
	c = dbConector.getInstance()
	try:
		_name = request.form['firstname']
		newP = Person(identification = _id, name =_name, age = _age)
		c.insert(newP)
	except:
		_name = request.form['firstname']
		newP = Person(identification = _id, name =_name, age = _age)
		c.updateP(newP)

	return app.send_static_file("success.html")

@app.route('/vwPerson', methods = ['POST'])
def vwPerson():
	output = '''
				<table style="width:100%">
				  <tr>
				    <th>identification</th>
				    <th>name</th>
				    <th>Age</th>
				  </tr>
			'''
	_name = request.form['firstname']
	c = dbConector.getInstance()
	_result = c.queryByName(_name)

	output += ''' <tr><th>{0}</th>
					<th>{1}</th>
					<th>{2}</th>
					</tr>
				'''.format(_result.identification,_result.name,_result.age)

	output += "</table>"
	return output

@app.route('/edtPerson', methods =['POST'])
def edtPerson():
	_name = request.form['firstname']
	c = dbConector.getInstance()
	_result = c.queryByName(_name)
	output = '''
				<form action="/insert", method="post">
				  id:<br>
				  <input type="number" name="id"  value = "{0}"
				  readonly="readonly">
				  name:<br>
				  <input type="text" name="firstnameM"  value = "{1}">
				  <br>
				  age:<br>
				  <input type="number" name="age" value = "{2}">
				  <br><br>
				  <input type="submit" value="Submit">
				</form>
			'''.format(_result.identification,_result.name,_result.age)
	return output

@app.route('/rmvPerson', methods = ['POST'])
def rmvPerson():
	_id = request.form['id']
	c = dbConector.getInstance()
	c.deleteP(_id)
	return "Eliminado"

#------------------------------Groups-------------------------------------------

@app.route('/insertGroup', methods = ['POST'])
def insertGroup():

	_id = request.form['id']
	c = dbConector.getInstance()
	try:
		_name = request.form['name']
		c.insert("INSERT INTO groups VALUES  ({1} ,'{0}')".format(_name,_id))
	except:
		_name = request.form['nameM']
		c.insert("UPDATE groups SET name = '{0}'\
				 WHERE id = {1}".format(_name,_id))

	return app.send_static_file("success.html")

@app.route('/vwGroup', methods = ['POST'])
def vwGroup():
	output = '''
				<table style="width:100%">
				  <tr>
				    <th>id</th>
				    <th>name</th>
				  </tr>
			'''
	_name = request.form['name']
	c = dbConector.getInstance()
	_result = c.query("SELECT * FROM groups WHERE name = '{}'".format(_name))
	for row in _result:
		output += ''' <tr><th>{0}</th>
					<th>{1}</th>
					</tr>
				'''.format(row['id'],row['name'])

	output += "</table>"
	return output

@app.route('/edtGroup', methods =['POST'])
def edtGroup():
	_name = request.form['name']
	c = dbConector.getInstance()
	_result = c.query("SELECT * FROM groups WHERE name = '{}'".format(_name))
	output = '''
				<form action="/insertGroup", method="post">
				  id:<br>
				  <input type="number" name="id"  value = "{0}"
				  readonly="readonly">
				  name:<br>
				  <input type="text" name="nameM"  value = "{1}">
				  <br>
				  <br><br>
				  <input type="submit" value="Submit">
				</form>
			'''.format(_result[0]['id'],_result[0]['name'])
	return output

@app.route('/rmvGroup', methods = ['POST'])
def rmvGroup():
	_id = request.form['id']
	c = dbConector.getInstance()
	c.insert("DELETE FROM groups WHERE id = {}".format(_id))
	return "Eliminado"

#----------------------------End Points-----------------------------------------

@app.route('/getPersonsById/<id>')
def getPersons(id):
	c = dbConector.getInstance()
	_result = c.query("SELECT * FROM person WHERE identification = '{}'".format(id))
	out = []
	for row in _result:
		out.append({'id': row['identification'],'name': row['name'],'age': row['age']})
	return  jsonify(out)
@app.route('/getGroupById/<id>')
def getGroups(id):
	c = dbConector.getInstance()
	_result = c.query("SELECT * FROM groups WHERE id = '{}'".format(id))
	out = []
	for row in _result:
		out.append({'id': row['id'],'name': row['name']})
	return  jsonify(out)

app.run(debug=True)
