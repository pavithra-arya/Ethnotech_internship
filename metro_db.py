import pymysql

# Connect to MySQL
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="PSaqvl@23"
)

cursor = conn.cursor()

# =========================
# CREATE DATABASE
# =========================
cursor.execute("CREATE DATABASE IF NOT EXISTS metro_db")
cursor.execute("USE metro_db")

# =========================
# DDL TASKS
# =========================

# Create Stations Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Stations(
    station_id INT PRIMARY KEY,
    station_name VARCHAR(100),
    location VARCHAR(100),
    platforms INT
)
""")

# Create Metro_Trains Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Metro_Trains(
    train_id INT PRIMARY KEY,
    train_name VARCHAR(100),
    capacity INT,
    station_id INT,
    FOREIGN KEY (station_id) REFERENCES Stations(station_id)
)
""")

# Add opening_year column
try:
    cursor.execute("ALTER TABLE Stations ADD opening_year INT")
except:
    pass

# Rename Table
try:
    cursor.execute("RENAME TABLE Metro_Trains TO Trains")
except:
    pass

# =========================
# DML TASKS
# =========================

# Insert Stations
stations = [
    (1, 'Central Station', 'Downtown', 6, 2015),
    (2, 'City Park', 'North Zone', 4, 2017),
    (3, 'Tech Park', 'IT Hub', 5, 2019),
    (4, 'Airport Station', 'Airport Road', 3, 2020),
    (5, 'Market Square', 'City Center', 4, 2016)
]

for s in stations:
    try:
        cursor.execute(
            "INSERT INTO Stations VALUES (%s,%s,%s,%s,%s)", s
        )
    except:
        pass


# Insert Trains
trains = [
    (101, 'Metro Express', 1000, 1),
    (102, 'City Rider', 800, 3),
    (103, 'Airport Link', 900, 4)
]

for t in trains:
    try:
        cursor.execute(
            "INSERT INTO Trains VALUES (%s,%s,%s,%s)", t
        )
    except:
        pass


# Update train capacity
cursor.execute("""
UPDATE Trains
SET capacity = 1200
WHERE train_id = 101
""")

# Delete station
cursor.execute("""
DELETE FROM Stations
WHERE station_id = 5
""")

# =========================
# DISPLAY DATA
# =========================

print("\nStations List:")
cursor.execute("SELECT * FROM Stations")
for row in cursor.fetchall():
    print(row)

print("\nTrains List:")
cursor.execute("SELECT * FROM Trains")
for row in cursor.fetchall():
    print(row)

# =========================
# DCL TASKS
# =========================

try:
    cursor.execute(
        "CREATE USER 'metro_staff'@'localhost' IDENTIFIED BY 'staff123'"
    )
except:
    pass

cursor.execute(
    "GRANT SELECT ON metro_db.Stations TO 'metro_staff'@'localhost'"
)

cursor.execute(
    "GRANT INSERT ON metro_db.Trains TO 'metro_staff'@'localhost'"
)

cursor.execute(
    "REVOKE INSERT ON metro_db.Trains FROM 'metro_staff'@'localhost'"
)

# Save changes
conn.commit()

print("\nAll tasks executed successfully!")

# Close connection
cursor.close()
conn.close()