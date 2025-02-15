while True:
    password = input("Enter a password: ")
    chars = password.strip()

    if len(chars) < 8 or not any(char.isupper() for char in chars):
        print("Your password should contain at least 8 characters and at least 1 uppercase letter. Enter a new password!")
        continue

    print("Password accepted!")
    print(password)