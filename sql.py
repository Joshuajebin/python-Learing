import sqlite3 #module 
connection = sqlite3.connect("\\home\\jpshua\\Documents\\python\\accadame.db") 
crsr = connection.cursor()
crsr.execute("SELECT DISTINCT(Grade) from Student")
result = crsr.fetchall()
print(result)

