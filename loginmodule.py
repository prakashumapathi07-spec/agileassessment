def login(username, password):
    if len(password) < 6:
        print("Password too short")
    elif username == "admin" and password == "admin123":
        print("Login successful")
    else:
        print("Invalid username or password")


# Example usage
username = input("Enter username: ")
password = input("Enter password: ")

login(username, password)
