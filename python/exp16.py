class PasswordError(Exception):
    pass


correct_password = "securepassword123"

count = 0

while count < 3:
    try:
        password = input("Enter your password: ")
        if password != correct_password:
            if count == 2:
                print("Wrong password")
                print("Access denied")
            if count < 2:
                raise PasswordError(
                    f"Wrong password, you have {2 - count} attempts left"
                )
            else:
                raise PasswordError
        print("Access granted")
        break
    except PasswordError as e:
        print(e)
        count += 1
