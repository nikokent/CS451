import json
from pprint import pprint

business = []
review = []
user = []
checkin = []

CSVFile = open("yelp_parsed.csv", "w+")

with open("yelp_data/yelp_business.JSON") as f:
    for line in f:
        data = json.loads(line)
        if 'neighborhood' in data:
            del data['neighborhood']
        business.append(data)

with open("yelp_data/yelp_review.JSON") as f:
    for line in f:
        data = json.loads(line)
        review.append(data)

with open("yelp_data/yelp_user.JSON") as f:
    for line in f:
        data = json.loads(line)
        del data["compliment_cool"]
        del data["compliment_cute"]
        del data["compliment_funny"]
        del data["compliment_hot"]
        del data["compliment_list"]
        del data["compliment_more"]
        del data["compliment_note"]
        del data["compliment_photos"]
        del data["compliment_plain"]
        del data["compliment_profile"]
        del data["compliment_writer"]
        del data["elite"]
        user.append(data)

with open("yelp_data/yelp_checkin.JSON") as f:
    for line in f:
        data = json.loads(line)
        checkin.append(data)

#For business
for i in range(len(business)):
    line = ""
    for key in business[i].keys():
        if(type(business[i][key])==dict):
            for newKey in business[i][key].keys():
                if(type(business[i][key][newKey])==dict):
                    for newerKey in business[i][key][newKey].keys():
                        line += str(newerKey) + ", " + str(business[i][key][newKey][newerKey]) + ", "
                else:
                    line += str(newKey) + ", " + str(business[i][key][newKey]) + ", "
        elif(type(business[i][key]) == list):
            for item in business[i][key]:
                line += str(item) + ", "
        else:
            line += str(business[i][key]) + ","
    line = line[:-1] + "/r/n"
    CSVFile.write(line)

#For review
for i in range(len(review)):
    line = ""
    for key in review[i].keys():
        if(type(review[i][key])==dict):
            for newKey in review[i][key].keys():
                if(type(review[i][key][newKey])==dict):
                    for newerKey in review[i][key][newKey].keys():
                        line += str(newerKey) + ", " + str(review[i][key][newKey][newerKey]) + ", "
                else:
                    line += str(newKey) + ", " + str(review[i][key][newKey]) + ", "
        elif(type(review[i][key]) == list):
            for item in review[i][key]:
                line += str(item) + ", "
        else:
            line += str(review[i][key]) + ","
    line = line[:-1] + "/r/n"
    CSVFile.write(line)

#For user
for i in range(len(user)):
    line = ""
    for key in user[i].keys():
        if(type(user[i][key])==dict):
            for newKey in user[i][key].keys():
                if(type(user[i][key][newKey])==dict):
                    for newerKey in user[i][key][newKey].keys():
                        line += str(newerKey) + ", " + str(user[i][key][newKey][newerKey]) + ", "
                else:
                    line += str(newKey) + ", " + str(user[i][key][newKey]) + ", "
        elif(type(user[i][key]) == list):
            for item in user[i][key]:
                line += str(item) + ", "
        else:
            line += str(user[i][key]) + ","
    line = line[:-1] + "/r/n"
    CSVFile.write(line)

#For checkin
for i in range(len(checkin)):
    line = ""
    for key in checkin[i].keys():
        if(type(checkin[i][key])==dict):
            for newKey in checkin[i][key].keys():
                if(type(checkin[i][key][newKey])==dict):
                    line += str(newKey) + ", "
                    for newerKey in checkin[i][key][newKey].keys():
                        line += str(newerKey) + ", " + str(checkin[i][key][newKey][newerKey]) + ", "
                else:
                    line += str(newKey) + ", " + str(checkin[i][key][newKey]) + ", "
        elif(type(checkin[i][key]) == list):
            for item in checkin[i][key]:
                line += str(item) + ", "
        else:
            line += str(checkin[i][key]) + ","
    line = line[:-1] + "/r/n"
    CSVFile.write(line)