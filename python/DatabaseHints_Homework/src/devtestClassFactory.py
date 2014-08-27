
from classFactory import build_row
from database import login_info
import mysql.connector

db = mysql.connector.Connect(**login_info)
cursor = db.cursor()

table = "animal"
cols = "id name weight".split()

condition = "family = 'Snake'"
condition_string = ""

query_string = "SELECT " + ", ".join(cols) + " FROM " + table
if True:
    query_string += " WHERE " + condition

print(query_string)

cursor.execute(query_string)

rows = cursor.fetchall()

for row in rows:
    print(row)
    
    
print("attempting class...:")

C = build_row("animal", "id name family weight")
condition = "family = 'Elephant'"
cursor2 = db.cursor()
c = C([100, "Joey", "Armadillo", 31])
genc = c.retrieve(cursor2)
for r in genc:
    print(r)

    

                
