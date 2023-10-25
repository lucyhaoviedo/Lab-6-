#Function to encode the password
def encoding_password(password):
    encoding_password = password
    return encoding_password
#Main menu
print("Menu")
print("-------------")
print("1. Encode")
print("2. Decode")
print("3. Quit")

option = input("Please enter an option: ")

if option == "1": #Option 1
    password = input("Please enter your password to encode: ")
    encoding_password = encoding_password(password)
    print("Your password has been encoded and stored!")

elif option == "2": #Option 2
    print("Decoding option is not implemented yet.")

elif option == "3": #Option 3
    print("Goodbye!")

else: #If else print the invalid statement
    print("Invalid option. Please select a valid option.")


