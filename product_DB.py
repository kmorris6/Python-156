#Kate Morris
#PA_8

#Import sqlite3 to use the DB browser to create and make changes to a database
import sqlite3

#Connect to the database in sqlite3 in order to access and make changes
conn = sqlite3.connect('ABCRetail.db')

#generate a cursor that can be used to move around within the database
cur = conn.cursor()

#If the table exists, it will be erased or dropped. 
cur.execute('DROP TABLE IF EXISTS Product')

#Create table named Product and the column names using the execute function
cur.execute("""CREATE TABLE Product (prod_number text, prod_name text, department text,
price real, quantity integer)""")

#Use the SQLite INSERT INTO function to put in the first row's values and then the other 6 rows' values; total of 7 rows.
cur.execute("""INSERT INTO Product VALUES('B005OCFHHK','Harry Potter:8-Film Collection','Movies and TV',39.99,45)""")
prod = [('B07XJ8C8F5','Echo Dot Smart Speaker','Electronics',29.99,30),('B08G3MN6KP','Super Mario 3D All Stars','Video Games',49.94,12),('B07JCRY8WP','Minecraft','Video Games',29.88,10),('B082JP6VP5','John Wick: Chapters1-3','Movies and TV',22.29,18),('B07FKR6KXF','Fire 7 Tablet','Electronics',49.99,15),('B075XLWML4','Roku Streaming Stick','Electronics',47.92,5)]
cur.executemany('INSERT INTO Product VALUES(?,?,?,?,?)',prod) #Use executemany to put in many values into the rows at one time.

print('The table was created successfully')

conn.commit() #Save the changes made to the database. Must be done after each change is made. 

print() #Used to create a blank line to easier read the output

#Use SQLite UPDATE to update the database 
sql="""UPDATE Product SET price = 32.99 WHERE prod_number = 'B07XJ8C8F5' """
cur.execute(sql) #Execute the update function

print('The update was successful.')
conn.commit() #Save the update

#Use SQLite DELETE function to delete the product number specified
sql="""DELETE FROM Product WHERE prod_number = 'B07FKR6KXF' """
cur.execute(sql) #Execute the delete function

print('The delete was successful.')
conn.commit() #Save the changes made

#UPDATE two values in the same row for the specified product number
sql="""UPDATE Product SET quantity = 5, price = 23.99 WHERE prod_number = 'B082JP6VP5'"""
cur.execute(sql) #Execute the update function

print('The update was successful.')
conn.commit() #Save the changes made

print() #Used to create a blank line to easier read the output

print('Products with quantity<=10:')
#Assign 'result' variable to cur.execute to show the information for each column in the database Product that has a quantity of 10 or less 
result = cur.execute("SELECT prod_number,prod_name,department,price, quantity FROM Product WHERE quantity <='10' ORDER BY quantity")
for row in result: 
    print(f"'{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}'") #Use f" to make each output result that has a quantity of 10 or less from the database be on separate lines

print() #Used to create a blank line to easier read the output

print('Electronics Department Products:')
#Assign 'el' variable to cur.execute to show the information for each column in the database Product that are electronics
el = cur.execute("SELECT prod_number,prod_name,department,price,quantity FROM Product WHERE department='Electronics' ORDER BY price desc")
for row in el:
    print(f"'{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}'") #Once again used the f" to print each output on a separate line

print() #Used to create a blank line to easier read the output

print('Products with quantity > 30 and price >= 29.99:')
#Assign 'tw' variable to cur.execute to show the information for each column in the database Product that have a quantity of more than 30 and a price equal or greater than 29.99
tw = cur.execute("SELECT prod_number,prod_name FROM ProducT WHERE quantity > '30' and price >= 29.99 ORDER BY quantity")
for row in tw:
    print(row)

cur.close()
