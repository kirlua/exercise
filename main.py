
# Ask the user to enter a 4-digit PIN
while True:
    pin = input("Please enter a 4-digit PIN: ")

# Check if the input PIN has exactly 4 characters and consists only of digits
    if len(pin) == 4 and pin.isdigit():
        print(f"Your pin is: {pin}")
        break


    else:
        print("Invalid PIN. Please make sure your PIN has exactly 4 digits.")


