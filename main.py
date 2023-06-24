import re

_starter = """
x############################x
|        WELCOME TO          |
|----------------------------|
|    EMAIL VALIDATOR REGEX   |
x############################x
"""

_required = """
------------------------------
|>  PLEASE ENTER SOMETHING! <|
------------------------------
"""

def is_valid(email):
    """
    Email Validator method to check email is valid or not.
    """
    re_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    try:
        pattern = re.compile(re_pattern)
        return re.match(pattern, email) is not None
    except ValueError:
        return "Something went wrong."


def email_validator(email):
    if not is_valid(email):
        print("[X___You entered, invalid email address___X]\n")
        return False
    else:
        print("Your Email is Perfect: {}\n".format(email))
        return True


if __name__ == "__main__":
    print(_starter)
    while True:
        email_input = input("Enter Your Email:\n>> ")
        validate = email_validator(email=email_input)
        
        if len(email_input) == 0:
            print(_required)
        elif validate == True or email_input == 'q':
            print("Thank you for using our Service!")
            break
        
        print("Press 'q' to Quit.\n")
        continue