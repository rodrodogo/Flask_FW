from typing import List
from os.path import isfile
import sqlite3  #DataBase




# Class for do the queries with the DataBase (DB), have a singleton pattern.
class dbConector:

    __instance = None   # singleton reference
    __conn = None       # connection with the DB
    __sql_gene = None   # cursor of the connection for do the queries

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


        if not isfile('users.db'): # If is the first time, it will create the DB
                self.__conn = sqlite3.connect('users.db')
                self.__conn.row_factory = sqlite3.Row # Change the format of the result row
                self.__sql_gene = self.__conn.cursor()
                self.__sql_gene.execute("CREATE TABLE person (\
                                            identification INTEGER PRIMARY KEY,\
                                            name varchar(255),  age int\
                                            )")
                self.__sql_gene.execute("CREATE TABLE groups (\
                                            id INTEGER PRIMARY KEY,\
                                        name varchar(255)\
                                            )")
        else:
            self.__conn = sqlite3.connect('users.db')
            self.__conn.row_factory = sqlite3.Row
            self.__sql_gene = self.__conn.cursor()



    # Receive the SQL Query and execute to insert new information
    def insert(self, msg: str)-> None:
        self.__doConection()
        self.__sql_gene.execute(msg)
        self.__conn.commit()
        self.__closeConection()
    # Receive the SQL Query and execute get information from DB
    def query(self, msg:str)->List:
        self.__doConection()
        self.__sql_gene.execute(msg)
        out = self.__sql_gene.fetchall()
        self.__closeConection()
        return out

    def __closeConection(self):
        self.__conn.close()
