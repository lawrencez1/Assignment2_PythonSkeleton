#!/usr/bin/env python3
import psycopg2

#####################################################
##  Database Connection
#####################################################

'''
Connect to the database using the connection string
'''
def openConnection():
    # connection parameters - ENTER YOUR LOGIN AND PASSWORD HERE
    userid = "COMP9120_test"
    passwd = "COMP9120_test"
    myHost = "120.48.94.214"

    # Create a connection to the database
    conn = None
    try:
        # Parses the config file and connects using the connect string
        conn = psycopg2.connect(database='COMP9120',
                                    user=userid,
                                    password=passwd,
                                    host=myHost)
    except psycopg2.Error as sqle:
        print("psycopg2.Error : " + sqle.pgerror)
    
    # return the connection to use
    return conn

'''
Validate administrator based on login and password
'''
def checkAdmCredentials(login, password):

    cur = openConnection().cursor()
    cur.execute(f"SELECT * from administrator WHERE login = '{login}'")
    row = cur.fetchall()
    data = row[0]
    if password == data[1]:
        return data


'''
List all the associated instructions in the database by administrator
'''
def findInstructionsByAdm(login):

    return


'''
Find a list of instructions based on the searchString provided as parameter
See assignment description for search specification
'''
def findInstructionsByCriteria(searchString):

    return


'''
Add a new instruction
'''
def addInstruction(amount, frequency, customer, administrator, etf, notes):

    return


'''
Update an existing instruction
'''
def updateInstruction(instructionid, amount, frequency, expirydate, customer, administrator, etf, notes):

    return
