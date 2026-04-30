email = input("Enter email: ")

if "@" in email and "." in email:
    if email.index("@") < email.rindex("."):
        print("Valid Email")
    else:
        print("Invalid Email")
else:
    print("Invalid Email")