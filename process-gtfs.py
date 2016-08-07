#!/usr/bin/python

import csv
import os
import sys
import MySQLdb

if (len(sys.argv) < 3):
    sys.exit("Not enough arguments")

directory = sys.argv[1]
transport_type = sys.argv[2]

# STOPS
def processStops(db):
    cur = db.cursor()
    fname = ''.join([directory, '/stops.txt'])
    with open(fname, "r") as fileobj:
        csvreader = csv.reader(fileobj)
        for row in csvreader:
            stopid = row[0]
            if (stopid == 'stop_id'):
                idx_name = row.index('stop_name') if ('stop_name' in row) else -1
                idx_lat = row.index('stop_lat') if ('stop_lat' in row) else -1
                idx_lon = row.index('stop_lon') if ('stop_lon' in row) else -1
                idx_loctype = row.index('location_type') if ('location_type' in row) else -1
                idx_parent = row.index('parent_station') if ('parent_station' in row) else -1
                idx_wheelchair = row.index('wheelchair_boarding') if ('wheelchair_boarding' in row) else -1
            else:
                name = row[idx_name] if (idx_name >= 0) else ''
                latitude = row[idx_lat] if (idx_lat >= 0 and row[idx_lat] != '') else '0'
                longitude = row[idx_lon] if (idx_lon >= 0 and row[idx_lon] != '') else '0'
                # 0 - Stop; 1 - Station
                location_type = row[idx_loctype] if (idx_loctype >= 0 and row[idx_loctype] != '') else '0'
                parent_station = row[idx_parent] if (idx_parent >= 0 and row[idx_parent] != '') else '0'
                # 0 - No Info; 1 - Wheelchair Accessible; 2 - Wheelchair Inaccessible
                wheelchair = row[idx_wheelchair] if (idx_wheelchair >= 0 and row[idx_wheelchair] != '') else '0'
                print ''.join(['ID:', stopid, ' STOP:', name, ' LAT:', latitude, ' LONG:', longitude, 
                    ' LOCATION TYPE:', location_type,
                    ' PARENT STATION:', parent_station,
                    ' WHEELCHAIR:', wheelchair,
                    ' TYPE:', transport_type])
                insert_sql = ("INSERT INTO stops "
                    "(id, name, latitude, longitude, location_type, parent_station, wheelchair_boarding, transport_type)"
                    "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)")
                insert_data = (stopid, name, latitude, longitude, location_type, parent_station, wheelchair, transport_type)
                cur.execute(insert_sql, insert_data)

    db.commit()
    cur.close()


# STOP_TIMES
def processStopTimes(db):
    cur = db.cursor()
    fname = ''.join([directory, '/stop_times.txt'])
    with open(fname, "r") as fileobj:
        csvreader = csv.reader(fileobj)
        for row in csvreader:
            tripid = row[0]
            if (tripid == 'trip_id'):
                idx_arrival = row.index('arrival_time') if ('arrival_time' in row) else -1
                idx_departure = row.index('departure_time') if ('departure_time' in row) else -1
                idx_stop_id = row.index('stop_id') if ('stop_id' in row) else -1
                idx_stop_seq = row.index('stop_sequence') if ('stop_sequence' in row) else -1
                idx_stop_headsign = row.index('stop_headsign') if ('stop_headsign' in row) else -1
                idx_pickup_type = row.index('pickup_type') if ('pickup_type' in row) else -1
                idx_dropoff_type = row.index('drop_off_type') if ('drop_off_type' in row) else -1
                idx_shape_dist_traveled = row.index('shape_dist_traveled') if ('shape_dist_traveled' in row) else -1
            else:
                arrival = row[idx_arrival] if (idx_arrival >= 0) else ''
                departure = row[idx_departure] if (idx_departure >= 0 and row[idx_departure] != '') else '0'
                stop_id = row[idx_stop_id] if (idx_stop_id >= 0 and row[idx_stop_id] != '') else '0'
                stop_seq = row[idx_stop_seq] if (idx_stop_seq >= 0 and row[idx_stop_seq] != '') else '0'
                stop_headsign = row[idx_stop_headsign] if (idx_stop_headsign >= 0 and row[idx_stop_headsign] != '') else '0'
                pickup_type = row[idx_pickup_type] if (idx_pickup_type >= 0 and row[idx_pickup_type] != '') else '0'
                dropoff_type = row[idx_dropoff_type] if (idx_dropoff_type >= 0 and row[idx_dropoff_type] != '') else '0'
                shape_dist_traveled = row[idx_shape_dist_traveled] if (idx_shape_dist_traveled >= 0 and row[idx_shape_dist_traveled] != '') else '0'
                print ''.join(['ID:', tripid, ' ARRIVAL:', arrival, ' DEPARTURE:', departure, 
                    ' STOP ID:', stop_id, 
                    ' STOP SEQ:', stop_seq,
                    ' STOP HEADSIGN:', stop_headsign,
                    ' PICKUP TYPE:', pickup_type,
                    ' DROPOFF TYPE:', dropoff_type,
                    ' SHAPE DIST TRAVELED:', shape_dist_traveled])
                insert_sql = ("INSERT INTO stop_times "
                    "(id, arrival_time, departure_time, stop_id, stop_sequence, stop_headsign, pickup_type, dropoff_type)"
                    "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)")
                insert_data = (tripid, arrival, departure, stop_id, stop_seq, stop_headsign, pickup_type, dropoff_type)
                cur.execute(insert_sql, insert_data)
        db.commit()
        cur.close()


env_host = os.environ['MYSQL_HOST']
env_user = os.environ['MYSQL_USER']
env_passwd = os.environ['MYSQL_PASSWD']
env_db = os.environ['MYSQL_DB']

db = MySQLdb.connect(host=env_host,
                     user=env_user,
                     passwd=env_passwd,
                     db=env_db)


# processStops(db)
processStopTimes(db)
db.close()

# you must create a Cursor object. It will let
#  you execute all the queries you need

# # Use all the SQL you like
# cur.execute("SELECT * FROM stop_times")

# # print all the first cell of all the rows
# for row in cur.fetchall():
#     print row[0]

# db.close()
