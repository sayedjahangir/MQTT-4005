import random
import math

def yes_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True

def prime_generation(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not yes_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime

def mod_of_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    raise ValueError("mod_inverse does not exist")

def message_encrypt(message, e, n):
    encoded_message = [ord(ch) for ch in message]
    ciphertext = [pow(ch, e, n) for ch in encoded_message]
    return ciphertext

def message_decrypted(ciphertext, d, n):
    message_encoded = [pow(ch, d, n) for ch in ciphertext]
    message = "".join(chr(ch) for ch in message_encoded)
    return message

lowest_value = int(input("Enter the minimum value for generating primes: "))
highest_value = int(input("Enter the maximum value for generating primes: "))

p, q = prime_generation(lowest_value, highest_value), prime_generation(lowest_value, highest_value)

while p == q:
    q = prime_generation(lowest_value, highest_value)

n = p * q
phi_of_n = (p - 1) * (q - 1)

e = random.randint(3, phi_of_n - 1)
while math.gcd(e, phi_of_n) != 1:
    e = random.randint(3, phi_of_n - 1)

d = mod_of_inverse(e, phi_of_n)

print("Public Key:", e)
print("Private Key:", d)
print("n:", n)
print("Phi_of n:", phi_of_n)
print("p:", p)
print("q:", q)

message = input("Enter the message to encrypt: ")

ciphered_text = message_encrypt(message, e, n)
print("Encrypted Message:", ciphered_text)

decrypted_message = message_decrypted(ciphered_text, d, n)
print("Decrypted Message:", decrypted_message)