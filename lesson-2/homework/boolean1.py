username = input("Enter username: ")
password = input("Enter password: ")

if username.strip() and password.strip():
    print("Login successful!")
else:
    print("Error: Username and password cannot be empty.")