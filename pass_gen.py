import random
import string
def generate_password(length:int=10):
    alphabet=  string.punctuation + string.digits + string.ascii_letters 
    password= ''.join(random.choice(alphabet) for i in range(length))
    return password
password = generate_password()
print(f"Generate password: {password}")