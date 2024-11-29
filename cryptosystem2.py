import numpy as np

# Función para verificar si el determinante de T es 1 en módulo 29
def check_determinant(T, mod=29):
    det = int(np.linalg.det(T)) % mod
    return det == 1

# Definir la matriz T (debe tener determinante 1 en módulo 29)
T = np.array([[2, 1, 0], [1, 1, 0], [0, 0, 1]])

# Verificar que el determinante de T sea 1 en módulo 29
if not check_determinant(T):
    raise ValueError("La matriz T no tiene determinante 1 en módulo 29. Modifica la matriz T.")

# Vectores b, los coeficientes deben ser enteros
b = np.array([1, 2, 3])


# Función para convertir texto a números
def text_to_numbers(text):
    alphabet = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
        'K': 10, 'L': 11, 'M': 12, 'N': 13, 'Ñ': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
        'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, ' ': 27, '*': 28
    }
    return [alphabet.get(char, -1) for char in text]

# Función para dividir el texto en bloques de tamaño 3
def split_into_blocks(text):
    blocks = [text[i:i + 3] for i in range(0, len(text), 3)]
    if len(blocks[-1]) < 3:
        blocks[-1] = blocks[-1] + ' ' * (3 - len(blocks[-1]))  # Completar con espacios
    return blocks

# Función para encontrar la inversa de una matriz en módulo 29
def matrix_inverse(T, mod=29):
    det = int(np.linalg.det(T)) % mod
    det_inv = pow(det, -1, mod)  # Inversa del determinante en módulo 29
    T_adj = np.round(det * np.linalg.inv(T) * det_inv) % mod  # Matriz adjunta escalada por det_inv
    return T_adj.astype(int) % mod

# Función para encriptar los bloques usando la matriz T y el vector b
def encrypt_blocks(blocks, T, b):
    encrypted_blocks = []
    for block in blocks:
        block_numbers = text_to_numbers(block)
        encrypted_block = np.dot(T, block_numbers) + b
        encrypted_block_mod = [int(x) % 29 for x in encrypted_block]  # Aplicar módulo 29
        encrypted_blocks.append(encrypted_block_mod)
    return encrypted_blocks

# Función para desencriptar los bloques usando la matriz inversa de T
def decrypt_blocks(encrypted_blocks, T, b, mod=29):
    T_inv = matrix_inverse(T, mod)  # Obtener la matriz inversa de T
    
    decrypted_blocks = []
    for block in encrypted_blocks:
        # Convertir el bloque a un array de numpy para operaciones matriciales
        block_array = np.array(block)
        
        # Realizar el desencriptado usando la matriz inversa y restando b
        decrypted_block = np.dot(T_inv, block_array - b)  # Desencriptado
        decrypted_block = decrypted_block % mod  # Aplicar módulo 29
        decrypted_blocks.append(decrypted_block.tolist())
    
    return decrypted_blocks

# Función para convertir los números de vuelta a texto
def numbers_to_text(numbers):
    alphabet_inv = {v: k for k, v in {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
        'K': 10, 'L': 11, 'M': 12, 'N': 13, 'Ñ': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
        'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, ' ': 27, '*': 28
    }.items()}
    return ''.join([alphabet_inv[x] for x in numbers])