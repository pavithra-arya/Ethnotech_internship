import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PSaqvl@23",   # change this to your MySQL password
)

cursor = db.cursor()

# Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS food_delivery_db")
cursor.execute("USE food_delivery_db")

# Create Tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers(
customer_id INT PRIMARY KEY,
name VARCHAR(100),
city VARCHAR(100),
phone VARCHAR(15)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Restaurants(
restaurant_id INT PRIMARY KEY,
restaurant_name VARCHAR(100),
city VARCHAR(100),
rating FLOAT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Food_Items(
food_id INT PRIMARY KEY,
food_name VARCHAR(100),
price INT,
restaurant_id INT,
FOREIGN KEY (restaurant_id) REFERENCES Restaurants(restaurant_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Orders(
order_id INT PRIMARY KEY,
customer_id INT,
food_id INT,
quantity INT,
order_date DATE,
FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
FOREIGN KEY (food_id) REFERENCES Food_Items(food_id)
)
""")

# Insert Data
cursor.execute("INSERT IGNORE INTO Customers VALUES (1,'Amit','Chennai','9876543210')")
cursor.execute("INSERT IGNORE INTO Customers VALUES (2,'Rahul','Bangalore','9876543211')")
cursor.execute("INSERT IGNORE INTO Customers VALUES (3,'Anita','Hyderabad','9876543212')")

cursor.execute("INSERT IGNORE INTO Restaurants VALUES (1,'Pizza Hut','Chennai',4.2)")
cursor.execute("INSERT IGNORE INTO Restaurants VALUES (2,'Dominos','Bangalore',4.5)")
cursor.execute("INSERT IGNORE INTO Restaurants VALUES (3,'Burger King','Hyderabad',4.0)")

cursor.execute("INSERT IGNORE INTO Food_Items VALUES (1,'Veg Pizza',250,1)")
cursor.execute("INSERT IGNORE INTO Food_Items VALUES (2,'Chicken Pizza',350,2)")
cursor.execute("INSERT IGNORE INTO Food_Items VALUES (3,'Burger',150,3)")
cursor.execute("INSERT IGNORE INTO Food_Items VALUES (4,'French Fries',120,3)")

db.commit()

# ------------------------------
# TASK 1 – SELECT
# ------------------------------
print("\nAll Food Items:")
cursor.execute("SELECT * FROM Food_Items")
for row in cursor.fetchall():
    print(row)

# ------------------------------
# TASK 2 – WHERE
# ------------------------------
print("\nFood Items costing more than 200:")
cursor.execute("SELECT * FROM Food_Items WHERE price > 200")
for row in cursor.fetchall():
    print(row)

# ------------------------------
# TASK 3 – AND
# ------------------------------
print("\nFood items >150 AND restaurant_id = 2:")
cursor.execute("SELECT * FROM Food_Items WHERE price > 150 AND restaurant_id = 2")
for row in cursor.fetchall():
    print(row)

# OR condition
print("\nRestaurants in Chennai OR Bangalore:")
cursor.execute("SELECT * FROM Restaurants WHERE city='Chennai' OR city='Bangalore'")
for row in cursor.fetchall():
    print(row)

# ------------------------------
# TASK 4 – LIKE
# ------------------------------
print("\nCustomers starting with A:")
cursor.execute("SELECT * FROM Customers WHERE name LIKE 'A%'")
for row in cursor.fetchall():
    print(row)

print("\nFood items containing Pizza:")
cursor.execute("SELECT * FROM Food_Items WHERE food_name LIKE '%Pizza%'")
for row in cursor.fetchall():
    print(row)

# ------------------------------
# TASK 5 – BETWEEN
# ------------------------------
print("\nFood items price between 100 and 300:")
cursor.execute("SELECT * FROM Food_Items WHERE price BETWEEN 100 AND 300")
for row in cursor.fetchall():
    print(row)

# ------------------------------
# TASK 6 – ORDER BY
# ------------------------------
print("\nFood items sorted by price (High to Low):")
cursor.execute("SELECT * FROM Food_Items ORDER BY price DESC")
for row in cursor.fetchall():
    print(row)

# Close connection
cursor.close()
db.close()