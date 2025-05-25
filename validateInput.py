username = input("Enter your username: ")

if len(username) > 12:
    print("Max 12 characteres")
    username = input("Enter your username: ")
elif not username.find(" ") == -1:
    print("You can´t use spaces")
elif not username.isalpha():
    print("Only letters")
else:
    print(f"Welcome {username}")
