"""
Program verifies that every animal eats at least one food.

My approach to answering the question is to count the number 
of animals, then compare that count with the number of those
animals appearing with a minimum of one food item.
"""

import mysql.connector
from database import login_info


if __name__=="__main__":
    db = mysql.connector.Connect(**login_info)
    cursor = db.cursor()
    
    cursor.execute("SELECT COUNT(id) FROM animal")
    animal_count = cursor.fetchone()[0]
    cursor.execute("""SELECT COUNT(id) 
                      FROM animal 
                      WHERE id IN (SELECT anid FROM food)
                      """)
    animal_eats_count = cursor.fetchone()[0]
    print("Number of animals is", animal_count)
    print("Number of animals eating at least one food is", animal_eats_count)
    if animal_count > animal_eats_count:
        print("Not every animal eats at least one food!")
    else:
        print("Every animal eats at least one food.")

