"""
write a program that encrypt a message using a key
key -> int
message -> str
message + key => encrypted_message
message = apple
key = 3
encrypted_message = dssoh
"""

import string


def encrypt_message(message,key):
    alphabet = string.ascii_letters + string.punctuation + string.digits + ' '
    encrypted_message = ''
    if not isinstance(key, int):
        return 'Key is not an integer, type a new integer key.'
    if key == 0:
        return 'Key can not be 0.'
    if not isinstance(message, str):
        return 'Type a string for input.'
    if len(message) == 0:
        return 'The message is empty, type a message.'

    for letter in message:
        index = alphabet.index(letter) + key
        if index >= len(alphabet):
            index %= len(alphabet)
        encrypted_message += alphabet[index]

        # encrypted_message += alphabet[alphabet.index(letter) + key]

    return encrypted_message

# print(string.ascii_letters + string.punctuation + string.digits)
# print(len(string.ascii_letters + string.punctuation + string.digits))
