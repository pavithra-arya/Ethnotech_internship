import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",        # your mysql username
    password="PSaqvl@23" # your mysql password
)

cursor = conn.cursor()

# -----------------------------
# CREATE DATABASE
# -----------------------------
cursor.execute("CREATE DATABASE IF NOT EXISTS university_db")
cursor.execute("USE university_db")

# -----------------------------
# CREATE TABLES
# -----------------------------

# Students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students(
student_id INT PRIMARY KEY,
name VARCHAR(50)
)
""")

# Clubs table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Clubs(
club_id INT PRIMARY KEY,
club_name VARCHAR(50)
)
""")

# Student_Club table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Student_Club(
student_id INT,
club_id INT
)
""")

# Users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
user_id INT PRIMARY KEY,
name VARCHAR(50)
)
""")

# Subscriptions table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Subscriptions(
sub_id INT PRIMARY KEY,
user_id INT,
plan VARCHAR(50)
)
""")

# Authors table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Authors(
author_id INT PRIMARY KEY,
author_name VARCHAR(50)
)
""")

# Books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Books(
book_id INT PRIMARY KEY,
title VARCHAR(100),
author_id INT
)
""")

# -----------------------------
# INSERT DATA
# -----------------------------

cursor.execute("INSERT INTO Students VALUES (1,'Rahul'),(2,'Priya'),(3,'Amit'),(4,'Neha')")
cursor.execute("INSERT INTO Clubs VALUES (101,'Robotics'),(102,'Photography')")
cursor.execute("INSERT INTO Student_Club VALUES (1,101),(2,102),(3,101)")

cursor.execute("INSERT INTO Users VALUES (1,'Arjun'),(2,'Sneha'),(3,'Karan'),(4,'Meera')")
cursor.execute("INSERT INTO Subscriptions VALUES (201,1,'Premium'),(202,2,'Basic')")

cursor.execute("INSERT INTO Authors VALUES (1,'R.K. Narayan'),(2,'Chetan Bhagat')")
cursor.execute("INSERT INTO Books VALUES (301,'Malgudi Days',1),(302,'Five Point Someone',2),(303,'Unknown Mystery',NULL)")

conn.commit()

# -----------------------------
# INNER JOIN
# -----------------------------
print("\n--- INNER JOIN (Students & Clubs) ---")

cursor.execute("""
SELECT Students.name, Clubs.club_name
FROM Students
INNER JOIN Student_Club
ON Students.student_id = Student_Club.student_id
INNER JOIN Clubs
ON Student_Club.club_id = Clubs.club_id
""")

for row in cursor.fetchall():
    print("Student:", row[0], "| Club:", row[1])

# -----------------------------
# LEFT JOIN
# -----------------------------
print("\n--- LEFT JOIN (Users & Subscriptions) ---")

cursor.execute("""
SELECT Users.name, Subscriptions.plan
FROM Users
LEFT JOIN Subscriptions
ON Users.user_id = Subscriptions.user_id
""")

for row in cursor.fetchall():
    print("User:", row[0], "| Plan:", row[1])

# -----------------------------
# RIGHT JOIN
# -----------------------------
print("\n--- RIGHT JOIN (Authors & Books) ---")

cursor.execute("""
SELECT Books.title, Authors.author_name
FROM Authors
RIGHT JOIN Books
ON Authors.author_id = Books.author_id
""")

for row in cursor.fetchall():
    print("Book:", row[0], "| Author:", row[1])

# Close connection
cursor.close()
conn.close()