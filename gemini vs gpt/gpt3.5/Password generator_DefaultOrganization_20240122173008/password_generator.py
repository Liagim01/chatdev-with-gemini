'''
This file contains the PasswordGenerator class responsible for generating random passwords.
'''
import random
import string
class PasswordGenerator:
    def generate_password(self, length, include_lowercase, include_uppercase, include_numbers, include_symbols):
        characters = ""
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_numbers:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password