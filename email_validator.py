import re


def is_valid_email(email):
    # Define a regex pattern for validating an email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False


# Main program
if __name__ == "__main__":
    user_input = input("Enter an email address to validate: ")

    if is_valid_email(user_input):
        print(f"{user_input} is a valid email address.")
    else:
        print(f"{user_input} is not a valid email address.")
