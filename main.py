
while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    user_input=(int(input("Please enter an option: ")))
    if user_input==1:
        password_in=(input("Please enter your password to encode:"))
        new_pass=""
        for char in password_in:
            if 0<= int(char)<=6:
                encoded_char= str(int(char)+3)
                new_pass+=encoded_char

            else:
                encoded_char=str((int(char)+3) % 10)
                new_pass+=encoded_char
    print("Your password has been encoded and stored!")
    elif user_input==2:
        pass
    elif user_input == 3:
        break

if __name__ == '__main__':


