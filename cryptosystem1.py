# Function to convert text to numbers
def text_to_numbers(text):
    alphabet = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
        'K': 10, 'L': 11, 'M': 12, 'N': 13, 'Ñ': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
        'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, ' ': 27, '*': 28
    }
    return [alphabet.get(char, -1) for char in text]

# Function to encrypt
def encrypt(text, a, b):
    numbers = text_to_numbers(text)
    return [(a * x + b) % 29 for x in numbers]

# Function to convert numbers back to text
def numbers_to_text(numbers):
    alphabet_inv = {v: k for k, v in {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
        'K': 10, 'L': 11, 'M': 12, 'N': 13, 'Ñ': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
        'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, ' ': 27, '*': 28
    }.items()}
    return ''.join([alphabet_inv[x] for x in numbers])

# Function to find the multiplicative inverse of 'a' modulo 29
def multiplicative_inverse(a):
    for x in range(29):
        if (a * x) % 29 == 1:
            return x
    return None

# Function to decrypt
def decrypt(encrypted_text, a, b):
    a_inv = multiplicative_inverse(a)
    if a_inv is None:
        print("No multiplicative inverse found.")
        return
    encrypted_numbers = text_to_numbers(encrypted_text)
    return [a_inv * (x - b) % 29 for x in encrypted_numbers]
