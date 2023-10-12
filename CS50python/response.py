from validator_collection import checkers

def main():
    email=input("What's your email address?")
    print(validate(email))

def validate(x):
    if checkers.is_email(x):
        return "Valid"
    else:
        return "Invalid"
main()