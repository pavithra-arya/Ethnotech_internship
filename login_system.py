# Step 1: Create Account
print("=== Create Your Account ===")
created_username = input("Create Username: ")
created_password = input("Create Password: ")

print("\nAccount Created Successfully ✅")
print("=== Login Now ===")

# Step 2: Login System
max_attempts = 3
attempts = 0
account_locked = False

while attempts < max_attempts:
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == created_username and password == created_password:
        print("Login Successful ✅")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print(f"Invalid credentials ❌. Attempts left: {remaining}")

        if attempts == max_attempts:
            account_locked = True
            print("Account Locked 🔒. Too many failed attempts.")

if account_locked:
    print("Please try again later.")