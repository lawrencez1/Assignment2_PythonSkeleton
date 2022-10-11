#瞎xx写 交作业的时候记得删


import psycopg2

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


def checkAdmCredentials():

    cur = openConnection().cursor()
    cur.execute("SELECT login, password, firstname, lastname, email, remuneration from administrator WHERE login = 'ciori'")
    row = cur.fetchall()
    data = row[0]
    print(data)

checkAdmCredentials()