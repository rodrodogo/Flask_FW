from flask import Flask, request, render_template, jsonify
#from functions import *
from DB.Gestor import *
from DB.Gestor import Person
import sqlite3

app =Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")
@app.route('/crt_group')
def crt_group():
	return render_template('crt_group.html')
@app.route('/edt_group')
def edt_group():
	return render_template("edt_group.html")
@app.route('/rmv_group')
def rmv_group():
	return render_template("rmv_group.html")
@app.route('/vw_group')
def vw_group():
	return render_template("vw_group.html")
@app.route('/crt_person')
def crt_person():
	return render_template("crt_person.html")
@app.route('/edt_person')
def edt_person():
	return render_template("edt_person.html")
@app.route('/rmv_person')
def rmv_person():
	return render_template("rmv_person.html")
@app.route('/vw_person')
def vw_person():
	return render_template("vw_person.html")


@app.route('/insert', methods = ['POST'])
def insert():
	_age = request.form['age']
	_id = request.form['id']
	c = DtoPerson();
	try:
		_name = request.form['firstname']
		newP = Person(identification = _id, name =_name, age = _age)
		c.insert(newP)
	except:
		_name = request.form['firstnameM']
		newP = Person(identification = _id, name =_name, age = _age)
		c.update(newP)

	return render_template("index.html")

@app.route('/vwPerson', methods = ['POST'])
def vwPerson():

	_name = request.form['firstname']
	s = DtoPerson();
	_result = s.queryByName(_name)

	return render_template("vwPerson.html", id = _result.identification, name = _result.name, age = _result.age)

@app.route('/edtPerson', methods =['POST'])
def edtPerson():
	_name = request.form['firstname']
	c = DtoPerson();
	_result = c.queryByName(_name)
	return render_template("edtPerson.html", id = _result.identification, name = _result.name, age = _result.age )

@app.route('/rmvPerson', methods = ['POST'])
def rmvPerson():
	_id = request.form['id']
	c = DtoPerson();
	c.delete(_id)
	return "Eliminado"

#------------------------------Groups-------------------------------------------

@app.route('/insertGroup', methods = ['POST'])
def insertGroup():

	_id = request.form['id']
	c = DtoGroups()
	try:
		_name = request.form['name']
		gruop = Groups(id = _id, name = _name)
		c.insert(gruop)
	except:
		_name = request.form['nameM']
		gruop = Groups(id = _id, name = _name)
		c.update(gruop)

	return render_template("index.html")

@app.route('/vwGroup', methods = ['POST'])
def vwGroup():
	_name = request.form['name']
	c = DtoGroups()
	_result = c.queryByName(_name)
	return render_template("vwGroup.html", id = _result.id, name = _result.name)

@app.route('/edtGroup', methods =['POST'])
def edtGroup():
	_name = request.form['name']
	c = DtoGroups()
	_result = c.queryByName(_name)
	return render_template("edtGroup.html", id = _result.id, name = _result.name )

@app.route('/rmvGroup', methods = ['POST'])
def rmvGroup():
	_id = request.form['id']
	c = DtoGroups()
	c.delete(_id)
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
