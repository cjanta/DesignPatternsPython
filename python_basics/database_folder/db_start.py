import sqlite3

conn = sqlite3.connect("erste_db_db.db")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS person")
cursor.execute("CREATE TABLE IF NOT EXISTS person (id int, name text, age int)")
cursor.execute("INSERT INTO person VALUES (2, 'Susi', 73)")

conn.commit()

cursor.execute("SELECT * FROM person")
datasets = cursor.fetchall()
for data in datasets:
    print(data)

conn.close()


# DQL > Data Query Language
# DML > Data Manipulation Language
# TCL > Transaction Control Language
# DDL > Data Definition Language
# DCL > Data Control Language (nicht in SQLite)
# SQL > Structured Query Language