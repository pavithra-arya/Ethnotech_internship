import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PSaqvl@23"   # replace with your MySQL password
)

cursor = conn.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS university_view_db")
cursor.execute("USE university_view_db")

# -----------------------------
# Task 1: Create Students Table
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students(
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    marks INT,
    attendance INT
)
""")

# -----------------------------
# Clear old data
# -----------------------------
cursor.execute("DELETE FROM Students")

# -----------------------------
# Task 2: Insert Student Records
# -----------------------------
cursor.execute("""
INSERT INTO Students VALUES
(1,'Ravi','CSE',85,90),
(2,'Meena','ECE',78,88),
(3,'Arun','CSE',92,95),
(4,'Kiran','ME',65,80),
(5,'Pooja','CSE',88,91),
(6,'Rahul','ECE',70,75),
(7,'Sneha','IT',95,96),
(8,'Amit','IT',82,87),
(9,'Neha','CSE',60,70),
(10,'Vikas','ME',84,89)
""")

conn.commit()

# -----------------------------
# Task 3: Create VIEW
# -----------------------------
cursor.execute("DROP VIEW IF EXISTS eligible_scholarship_students")

cursor.execute("""
CREATE VIEW eligible_scholarship_students AS
SELECT *
FROM Students
WHERE marks > 80 AND attendance > 85
""")

# -----------------------------
# Task 4: Display eligible students
# -----------------------------
print("\nEligible Scholarship Students:\n")

cursor.execute("SELECT * FROM eligible_scholarship_students")

for row in cursor.fetchall():
    print(row)

# -----------------------------
# Task 5: Try inserting through view
# -----------------------------
print("\nTrying to insert student with low marks through view...\n")

try:
    cursor.execute("""
    INSERT INTO eligible_scholarship_students
    VALUES (11,'TestStudent','CSE',70,90)
    """)
    conn.commit()
except Exception as e:
    print("Insertion failed:", e)

# Close connection
cursor.close()
conn.close()