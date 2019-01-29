import psycopg2
#run with python3 createtable.py
try:
    conn = psycopg2.connect(database = "Milestone1DB", user = "niko", password = "kent", host = "localhost", port = "6969")
except:
    print("I am unable to connect to the database")

cur = conn.cursor()
try:
    cur.execute("CREATE TABLE business (id INT PRIMARY KEY, businessName VARCHAR(255) NOT NULL,"
                "state VARCHAR(255),city VARCHAR(255))")
    print("TABLE CREATED")
except:
    print("I can't drop our test database!")

conn.commit() # <--- makes sure the change is shown in the database
conn.close()