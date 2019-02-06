#
#   Parses data to the file and performs query to pgsql db
#
import json
import csv
from pprint import pprint
import psycopg2

try:
    conn = psycopg2.connect(database = "Milestone1DB", user = "postgres", password = "Cruzazul7", host = "localhost", port = "5432")
except:
    print("I am unable to connect to the database")

cur = conn.cursor()

items = []

with open("milestone1DB.csv", "r") as f:
    data = csv.reader(f)
    items = list(data)

for i in range(len(items)):
    line = str(i) + "," + items[i][0] + "," + items[i][1] + "," + items[i][2] + "\r\n"
    query =  "INSERT INTO business (id, businessName, state, city) VALUES (%s, %s, %s, %s);"
    querydata = (str(i), items[i][0], items[i][1], items[i][2])
    cur.execute(query, querydata)
    conn.commit()