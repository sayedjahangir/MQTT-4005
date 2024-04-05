e, d, n = 61003129, 39248809, 168594407

def encrypt(message):
    encoded_message = [ord(ch) for ch in message]
    ciphertext = [pow(ch, e, n) for ch in encoded_message]
    return ciphertext

def decrypt(ciphertext):
    message_encoded = [pow(ch, d, n) for ch in ciphertext]
    message = "".join(chr(ch) for ch in message_encoded)
    return message