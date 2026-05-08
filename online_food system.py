import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PSaqvl@23"
)

cursor = db.cursor()

# Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS online_food_system")
cursor.execute("USE online_food_system")

# Create Tables
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
restaurant_id INT
)
""")

db.commit()


# =========================
# FUNCTIONS
# =========================

# CREATE
def add_food():
    food_id = int(input("Enter Food ID: "))
    name = input("Enter Food Name: ")
    price = int(input("Enter Price: "))
    restaurant_id = int(input("Enter Restaurant ID: "))

    query = "INSERT INTO Food_Items VALUES(%s,%s,%s,%s)"
    values = (food_id, name, price, restaurant_id)

    cursor.execute(query, values)
    db.commit()

    print("Food Item Added Successfully\n")


# READ
def show_food():
    cursor.execute("SELECT * FROM Food_Items")
    data = cursor.fetchall()

    print("\nFood Items List")
    print("---------------------------")

    for row in data:
        print(row)

    print()


# UPDATE
def update_food():
    food_id = int(input("Enter Food ID to Update: "))
    new_price = int(input("Enter New Price: "))

    query = "UPDATE Food_Items SET price=%s WHERE food_id=%s"
    values = (new_price, food_id)

    cursor.execute(query, values)
    db.commit()

    print("Food Price Updated\n")


# DELETE
def delete_food():
    food_id = int(input("Enter Food ID to Delete: "))

    query = "DELETE FROM Food_Items WHERE food_id=%s"
    value = (food_id,)

    cursor.execute(query, value)
    db.commit()

    print("Food Item Deleted\n")


# =========================
# MENU
# =========================

while True:

    print("\n====== Online Food Delivery System ======")
    print("1. Add Food Item")
    print("2. Show Food Items")
    print("3. Update Food Price")
    print("4. Delete Food Item")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_food()

    elif choice == "2":
        show_food()

    elif choice == "3":
        update_food()

    elif choice == "4":
        delete_food()

    elif choice == "5":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Try Again")