def reverse_string(input_string):
    # Reverse the string using slicing
    reversed_string = input_string[::-1]
    return reversed_string

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a string to reverse: ")
    print("Reversed string:", reverse_string(user_input))
