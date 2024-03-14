class InvalidEmailError(Exception):
    def __init__(self, email):
        self.email = email

def validate_email(email):
    if '@' not in email:
        raise InvalidEmailError(email)

try:
    user_email = input("Enter your email address: ")
    validate_email(user_email)
    print("Email address is valid!")
except InvalidEmailError as e:
    print("Invalid email address provided:", e.email)
