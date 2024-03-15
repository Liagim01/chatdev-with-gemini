'''This module contains the PasswordGenerator class.'''
import random
class PasswordGenerator:
    def __init__(self):
        self.characters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()")
    def generate_password(self, length, password_label):
        password = ""
        for i in range(length):
            password += random.choice(self.characters)
        password_label.configure(text=password)