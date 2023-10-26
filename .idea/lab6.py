# Function to encode the password
def encoding_password(password):
    encoding_password = password  # This is a placeholder
    return encoding_password


# Main menu
while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    option = input("Please enter an option: ")  # Prompts the user to enter an option

    if option == "1":  # If the user enters 1, the program prompts the user to enter a password and calls the encoding_password() function to encode the password
        password = input("Please enter your password to encode: ")
        encoding_password = encoding_password(password)
        print("Your password has been encoded and stored!")
