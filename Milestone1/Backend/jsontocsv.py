import json
from pprint import pprint
import psycopg2

try:
    conn = psycopg2.connect(database = "Milestone1DB", user = "niko", password = "kent", host = "localhost", port = "6969")
except:
    print("I am unable to connect to the database")

cur = conn.cursor()

items = []

with open("yelp_data/yelp_business.JSON") as f:
    for line in f:
        data = json.loads(line)
        items.append(data)

CSVFile = open("yelp_business.csv", "w+")

for i in range(len(items)):
    line = str(i) + "," + items[i]["name"] + "," + items[i]["state"] + "," + items[i]["city"] + "\r\n"
    CSVFile.write(line)
    query =  "INSERT INTO business (id, businessName, state, city) VALUES (%s, %s, %s, %s);"
    querydata = (str(i), items[i]["name"], items[i]["state"], items[i]["city"])
    cur.execute(query, querydata)
    conn.commit()


CSVFile.close()