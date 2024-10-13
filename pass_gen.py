import random

def apply_operation(char, operation, skip_value):
    # If the character is a special character, return it as is
    if not char.isalnum():
        return char

    ascii_value = ord(char)

    # Apply the selected operation
    if operation == '+':
        return chr((ascii_value + skip_value) % 128)  # Wrap around for ASCII range
    elif operation == '-':
        return chr((ascii_value - skip_value) % 128)  # Wrap around for ASCII range
    elif operation == '*':
        return chr((ascii_value * skip_value) % 128)  # Wrap around for ASCII range
    elif operation == '%':
        return chr(ascii_value % skip_value) if skip_value != 0 else char
    elif operation == '**':
        return chr((ascii_value ** 2) % 128)  # Square value and wrap around
    else:
        return char  # Default case, no change

def main():
    # Define available operations
    operations = ['+', '-', '*', '%', '**']
    print("Available operations: ", operations)

    # Get original password from the user
    original_password = input("Enter your password: ")

    # Ask user to select 3 valid operations
    selected_operations = []
    for i in range(3):
        while True:
            operation = input(f"Select operation {i + 1} from the available options: ")
            if operation in operations:
                selected_operations.append(operation)
                break  # Exit the loop if a valid operation is selected
            else:
                print("Invalid operation. Please select one of the following:", operations)

    # Get the skip value
    while True:
        try:
            skip_value = int(input("Enter a skip value (1 to 15): "))
            if 1 <= skip_value <= 15:
                break
            else:
                print("Skip value must be between 1 and 15.")
        except ValueError:
            print("Please enter a valid integer.")

    # Generate new password
    new_password = ''
    for i, char in enumerate(original_password):
        operation = selected_operations[i % 3]  # Cycle through selected operations
        new_password += apply_operation(char, operation, skip_value)

    # Jumble the final password
    jumbled_password = ''.join(random.sample(new_password, len(new_password)))

    print("Generated Jumbled Password:", jumbled_password)

if __name__ == "__main__":
    main()
