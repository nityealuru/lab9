# My name is Nitin Yealuru
def main():
    while True:
        print("Welcome to the Password Encoder/Decoder Program!")
        print("Please select an option:")
        print("1. Encode a password")
        print("2. Decode a password")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            password = input("Enter an 8-digit password containing only integers: ")
            encoded_password = encode(password)
            print(f"The encoded password is: {encoded_password}")
        elif choice == "2":
            encoded_password = input("Enter the encoded password: ")
            # decoded_password = decode(encoded_password)
            # print(f"The decoded password is: {decoded_password}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def encode(password):
    encoded_password = " "
    for char in password:
        if char.isdigit():
            encoded_digit = (int(char) + 3) % 10
            encoded_password += str(encoded_digit)
        else:
            print("Error: Password must contain only integers.")
            return " "
    return encoded_password

def encode(password):
    if not password.isdigit() or len(password) != 8:
        raise ValueError("Password should be 8 digits long and contain only integers.")

    digit_pw = [int(digit) for digit in password]
    digit_encoded = [(digit + 3) % 10 for digit in digit_pw]
    pw_encoded = [str(digit) for digit in digit_encoded]
    return ''.join(pw_encoded)

def decode(password):
    if not password.isdigit() or len(password) != 8:
        raise ValueError("Password should be 8 digits long and contain only integers.")

    digit_pw = [int(digit) for digit in password]
    digit_decoded=""
    for digit in digit_pw:
        if digit > 2:
            digit_decoded += str(digit - 3)
        else:
            digit_decoded += str(digit+7)

    return digit_decoded
    
if __name__ == "__main__":
    main()
