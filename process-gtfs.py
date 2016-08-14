#!/usr/bin/python

import csv
import os
import sys
import mysql.connector
from mysql.connector import connect, errorcode

if (len(sys.argv) < 3):
    sys.exit("Not enough arguments")

directory = sys.argv[1]
transport_type = sys.argv[2]

def loadFiles(cnx):
    TABLES = ['calendar', 'calendar_dates', 'routes', 'trips', 'stops', 'stop_times']
    for table in TABLES:
        print 'processing %s' % table
        fname = '%s/%s.txt' % (directory, table)
        try:
            f = open(fname, 'r')
            reader = csv.reader(f)
            columnsRaw = reader.next()
            columns = ['shape_dist_traveled' if x=='shape_dist_travelled' else x for x in columnsRaw]
            f.close()
            load_sql = "LOAD DATA INFILE '%s' REPLACE INTO TABLE %s FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\\n' IGNORE 1 LINES (%s)" % (os.path.abspath(fname), table, ','.join(columns))
            cur = cnx.cursor()
            cur.execute(load_sql)
            t = cur.fetchwarnings()
            print t
            cnx.commit()
            cur.close()
        except IOError:
            print "Error opening file '%s'" % (fname)

env_host = os.environ['MYSQL_HOST']
env_user = os.environ['MYSQL_USER']
env_passwd = os.environ['MYSQL_PASSWD']
env_db = os.environ['MYSQL_DB']

try:
    cnx = connect(user=env_user, password=env_passwd,
                                  host=env_host,
                                  database=env_db)
    cnx.get_warnings = True
    loadFiles(cnx)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()

