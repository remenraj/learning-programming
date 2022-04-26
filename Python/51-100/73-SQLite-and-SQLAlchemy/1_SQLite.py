# SQLite
# SQL commands: https://www.codecademy.com/article/sql-commands
# SQL CREATE TABLE Keyword: https://www.w3schools.com/sql/sql_ref_create_table.asp



import sqlite3

# create a connection to a new database (if the database does not exist then it will be created)
db = sqlite3.connect(
    r"learning-programming\Python\51-100\73-library\74-sqlite\books-collection.db"
)

# create a cursor which will control our database. This is used to execute SQL commands
cursor = db.cursor()

# creating a new table
try:
    cursor.execute(
        "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)"
    )
except sqlite3.OperationalError:
    print("Table already exists")
    
# add data to the table books
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")

# commit the changes to our database
db.commit()