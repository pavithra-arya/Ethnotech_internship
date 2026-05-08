import pymysql

def connect():
    return pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="PSaqvl@23",  # your MySQL password
        database="hospital_db"
    )

# ---------------- FUNCTIONS ---------------- #

def add_patient():
    conn = connect()
    cursor = conn.cursor()

    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    disease = input("Enter Disease: ")
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")

    sql = """INSERT INTO patients 
             (name, age, gender, disease, phone, address) 
             VALUES (%s, %s, %s, %s, %s, %s)"""

    values = (name, age, gender, disease, phone, address)

    cursor.execute(sql, values)
    conn.commit()

    print("✅ Patient Added Successfully!\n")

    cursor.close()
    conn.close()


def show_patients():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients")
    records = cursor.fetchall()

    if len(records) == 0:
        print("No patients found.\n")
    else:
        print("\n--- Patient List ---")
        for row in records:
            print(row)
        print()

    cursor.close()
    conn.close()


def delete_patient():
    conn = connect()
    cursor = conn.cursor()

    pid = int(input("Enter Patient ID to delete: "))

    sql = "DELETE FROM patients WHERE patient_id = %s"
    cursor.execute(sql, (pid,))
    conn.commit()

    if cursor.rowcount > 0:
        print("✅ Patient Deleted Successfully!\n")
    else:
        print("❌ Patient ID not found!\n")

    cursor.close()
    conn.close()


def update_patient():
    conn = connect()
    cursor = conn.cursor()

    pid = int(input("Enter Patient ID to update: "))

    name = input("Enter New Name: ")
    age = int(input("Enter New Age: "))
    gender = input("Enter New Gender: ")
    disease = input("Enter New Disease: ")
    phone = input("Enter New Phone: ")
    address = input("Enter New Address: ")

    sql = """UPDATE patients 
             SET name=%s, age=%s, gender=%s, disease=%s, phone=%s, address=%s
             WHERE patient_id=%s"""

    values = (name, age, gender, disease, phone, address, pid)

    cursor.execute(sql, values)
    conn.commit()

    if cursor.rowcount > 0:
        print("✅ Patient Updated Successfully!\n")
    else:
        print("❌ Patient ID not found!\n")

    cursor.close()
    conn.close()


# ---------------- MENU ---------------- #

while True:
    print("===== Hospital Management System =====")
    print("1. Add Patient")
    print("2. Delete Patient")
    print("3. Show Patient List")
    print("4. Update Patient")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_patient()
    elif choice == '2':
        delete_patient()
    elif choice == '3':
        show_patients()
    elif choice == '4':
        update_patient()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.\n")