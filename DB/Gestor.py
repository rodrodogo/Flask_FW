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

class dbConector:

    __instance = None   # singleton reference
    __dbAgent = None    # DAO

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

    def __doConection(self): # Do the connection with DB users in the same directory

        if not isfile('test.db'): # If is the first time, it will create the DB
            self.__dbAgent = Database("test.db")
            self.__dbAgent.query(Person).create().execute()
        else:
            self.__dbAgent = Database("test.db")

    # Receive the SQL Query and execute to insert new information
    def insert(self, per:Person)-> None:
        self.__doConection()
        self.__dbAgent.query().insert(per).execute()
        self.__closeConection()

    def queryById(self,id:int)-> None:
        for row in self.__dbAgent.query(Person).select().filter(Person.identification == id).execute():
            print(row)

    def queryByName(self,name:str):
        self.__doConection()
        _out = self.__dbAgent.query(Person).select().filter(Person.name == name).execute()

        for rw in _out:#Machete barbaro
            per = Person(identification = rw[0], name = rw[1], age = rw[2])
        self.__closeConection()
        return per

    def updateP(self, per:Person)-> None:
        self.__doConection()
        self.__dbAgent.query(Person).update(name = per.name, age = per.age).filter(Person.identification == camila.identification).execute()
        self.__closeConection()

    def deleteP(self, id:int)-> None:
        self.__doConection()
        self.__dbAgent.query(Person).delete().filter(Person.identification == id).execute()
        self.__closeConection()

    def __closeConection(self)->None:
        self.__dbAgent.close()

#if __name__ == '__main__':
#    camila = Person(identification = 5, name = 'azul', age = 32)
#    db = dbConector.getInstance()
    #db.insert(camila)
#    db.deleteP(camila)
#    db.closeConection()
#    temp = db.queryByName("azul")
#    print(temp.name + "holas")
#    db.update(camila)


    #db.queryById(5)

    #with Database("test.db") as db:
        #db.query(Person).create().execute()
        #person1 = Person(identification = 2, name = 'andrea')
        #db.query().insert(person1).execute()

    #    personQ = Person(identification = 2, name = 'andrea')
    #    for row in db.query(Person).select().filter(Person.name == 'andrea').execute():
    #        print(row)
