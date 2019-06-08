from sqlite_orm.database import Database
from sqlite_orm.table import BaseTable
from sqlite_orm.field import IntegerField, TextField

from typing import List
from os.path import isfile
import sqlite3  #DataBase

class Person(BaseTable):
    __table_name__ = 'person'
    identification = IntegerField(primary_key=True, auto_increment=True)
    name = TextField(not_null=True)
    age = IntegerField()

class Groups(BaseTable):
    __table_name__ = 'groups'
    id = IntegerField(primary_key=True, auto_increment=True)
    name = TextField(not_null=True)

class dbConector:

    __instance = None   # singleton reference
    dbAgent = None

    @staticmethod
    def getInstance():  # Method to get the unique reference for the class
        if dbConector.__instance == None:
            dbConector()
        return dbConector.__instance

    def __init__(self):
        if dbConector.__instance != None:
            raise Exception("glitch in the matrix, talk to nio")
        else:
            dbConector.__instance = self

    def doConection(self): # Do the connection with DB users in the same directory

        if not isfile('Users.db'): # If is the first time, it will create the DB
            self.dbAgent = Database("Users.db")
            self.dbAgent.query(Person, Groups).create().execute()
        else:
            self.dbAgent = Database("Users.db")

    def closeConection(self)->None:
        self.dbAgent.close()


class DtoPerson:

    # Receive the SQL Query and execute to insert new information
    def insert(self, per:Person)-> None:
        c = dbConector.getInstance()
        c.doConection()
        c.dbAgent.query().insert(per).execute()
        c.closeConection()

    def queryById(self,id:int)-> None:
        for row in self.__dbAgent.query(Person).select().filter(Person.identification == id).execute():
            print(row)

    def queryByName(self,name:str):
        c = dbConector.getInstance()
        c.doConection()
        _out = c.dbAgent.query(Person).select().filter(Person.name == name).execute()

        for rw in _out:#Machete barbaro
            per = Person(identification = rw[0], name = rw[1], age = rw[2])
        c.closeConection()
        return per

    def update(self, per:Person)-> None:
        c = dbConector.getInstance()
        c.doConection()
        c.dbAgent.query(Person).update(name = per.name, age = per.age).filter(Person.identification == per.identification).execute()
        c.closeConection()

    def delete(self, id:int)-> None:
        c = dbConector.getInstance()
        c.doConection()
        c.dbAgent.query(Person).delete().filter(Person.identification == id).execute()
        c.closeConection()


class DtoGroups:

    # Receive the SQL Query and execute to insert new information
    def insert(self, per:Groups)-> None:
        c = dbConector.getInstance()
        c.doConection()
        c.dbAgent.query().insert(per).execute()
        c.closeConection()

    def queryById(self,id:int)-> None:
        for row in self.__dbAgent.query(Groups).select().filter(Groups.id == id).execute():
            print(row)

    def queryByName(self,name:str):
        c = dbConector.getInstance()
        c.doConection()
        _out = c.dbAgent.query(Groups).select().filter(Groups.name == name).execute()

        for rw in _out:#Machete barbaro
            per = Groups(id = rw[0], name = rw[1])
        c.closeConection()
        return per

    def update(self, per:Groups)-> None:
        c = dbConector.getInstance()
        c.doConection()
        c.dbAgent.query(Groups).update(name = per.name).filter(Groups.id == per.id).execute()
        c.closeConection()

    def delete(self, id:int)-> None:
        c = dbConector.getInstance()
        c.doConection()
        c.dbAgent.query(Groups).delete().filter(Groups.id == id).execute()
        c.closeConection()
