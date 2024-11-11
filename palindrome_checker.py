def is_palindrome(s):
    # Normalize the string by removing spaces and converting to lowercase
    normalized_string = ''.join(s.split()).lower()
    # Check if the string is the same forwards and backwards
    return normalized_string == normalized_string[::-1]


# Main program
if __name__ == "__main__":
    user_input = input("Enter a string to check if it is a palindrome: ")

    if is_palindrome(user_input):
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')
