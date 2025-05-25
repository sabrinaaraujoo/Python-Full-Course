# Membership operators = used to test whether a value or a variable is found in a sequence
#                        (string, list, tuple, set, dictionary)
#                        1. not in
#                        2. in


email = "fakeemail@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid")

# if "@" not in email or "." not in email:
#     print("Invalid")
# else:
#     print("Valid email")