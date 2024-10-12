import random
import string

def jumble_string(input_string,length=10):
    input_list = list(input_string)  # Convert the input string to a list
    random.shuffle(input_list)        # Shuffle the list
    return ''.join(input_list)         # Join the list back into a string

# User input for password characters
input_string = input("Enter password : ")

# Generation of the jumbled password
jumbled_password = jumble_string(input_string)

# Output of the generated password
print(f"Generated password: {jumbled_password}")
