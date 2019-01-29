# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import psycopg2


myFile = open("0.txt", "r")
data = str(myFile.read())
#myFile = open("1.txt", "r")
#data += str(myFile.read())
#myFile = open("2.txt", "r")
#data += str(myFile.read())
myFile = open("3.txt", "r")
data += str(myFile.read())
#myFile = open("4.txt", "r")
#data += str(myFile.read())
data = data.replace("\t", ",")
tokenList = data.split("\n")
formedData = {}

try:
    conn = psycopg2.connect(database = "youtube1", user = "postgres", password = "admin", host = "localhost", port = "5432")
except:
    print("I am unable to connect to the database")

cur = conn.cursor()

for tokenString in tokenList:
    tempDict = {
        "videoID":"",
        "uploader":"",
        "age":0,
        "category":"",
        "length":0,
        "views":0,
        "rate":0.0,
        "ratings":0,
        "comments":0,
        "relatedID":[]
    }
    tokens = tokenString.split(",")
    count = 0
    for token in tokens:
        if(count is 0):
            tempDict["videoID"] = token
        if(count is 1):
            tempDict["uploader"] = token
        if(count is 2):
            tempDict["age"] = int(token)
        if(count is 3):
            tempDict["category"] = token
        if(count is 4):
            tempDict["length"] = int(token)
        if(count is 5):
            tempDict["views"] = int(token)
        if(count is 6):
            tempDict["rate"] = float(token)
        if(count is 7):
            tempDict["ratings"] = int(token)
        if(count is 8):
            tempDict["comments"] = int(token)
        if(count > 8):
            tempDict["relatedID"].append(token)
        count += 1
        formedData[tempDict["videoID"]] = tempDict

item = formedData[1]

videoID = item["videoID"]
uploader = item["uploader"]
age = item["age"]
category = item["category"]
length = item["length"]
views = item["views"]
rate = item["rate"]
ratings = item["ratings"]
comments = item["comments"]
relatedID = item["relatedID"]
query =  "INSERT INTO video (videoID, uploader, age, category, length, rate, ratings, comments, relatedID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"

querydata = (videoID, uploader, age, category, length, rate, ratings, comments, relatedID)

cur.execute(query, querydata)

conn.commit()

#print len(tokenList)
