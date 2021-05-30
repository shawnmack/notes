import sqlite3
from random import randint
import random

#SKILLSHARE COURSE



#f = open("Path",'w')



#connect to database file, default will create file if it doesn't exist
conn = sqlite3.connect("iceCreamStore.db")

#cursor points to a specific index of the db
#used for updating, creating specifics of the db file
c = conn.cursor()
#f.write()

#This drop statement clears table if it exists from previous executions of this file so that I can have random values each time
c.execute("DROP TABLE IF EXISTS iceCreamStore")

#this creates the initial table and defines it's primary key and other attributes
c.execute("CREATE TABLE IF NOT EXISTS iceCreamStore(flavor TEXT PRIMARY KEY, calories INT, dessertType TEXT, idealTempF REAL)")

#similar to open("PATH","r")
#c.execute("SELECT flavorID FROM iceCreamStore")

#like a f.readline()
#result = c.fetchone()
#result = c.fetchall()
#print(result)

#c.execute("SELECT flavorID from iceCreamStore")
#print(c.fetchone())
#print(c.fetchmany(size = 5))

f = open('benandjerry.txt', 'r')
for name in f:
    c.execute("INSERT INTO iceCreamStore (flavor,calories,idealTempF) VALUES (?,?,?)",
          (name.strip(),str(randint(100,250)),str(round(random.uniform(1,10),2))))
conn.commit()

#c.execute("SELECT DISTINCT idealTempF FROM iceCreamStore ORDER BY idealTempF")
c.execute("SELECT * FROM iceCreamStore")
data = c.fetchall()
print(len(data),data)

c.execute("UPDATE iceCreamStore SET dessertType = 'Ice Cream' WHERE dessertType IS NULL")
conn.commit()
c.execute("SELECT * FROM iceCreamStore")
data = c.fetchall()
print(len(data),data)

#conn.commit()
c.close
conn.close()




