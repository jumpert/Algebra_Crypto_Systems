import unicodedata
import re

def process_text(archivo_entrada):
    """
    Procesa el texto eliminando tildes, comas, puntos y lo convierte a mayúsculas.
    El resultado se guarda en 'cleaned_text.txt'.
    """
    # Leer el archivo de entrada
    with open(archivo_entrada, 'r', encoding='utf-8') as f:
        texto = f.read()
    
    # Normalizar el texto para separar los caracteres base de los acentos
    texto_sin_acentos = unicodedata.normalize('NFD', texto)
    
    # Eliminar los caracteres de acento (categoría 'Mn')
    texto_sin_acentos = ''.join(
        char for char in texto_sin_acentos if unicodedata.category(char) != 'Mn'
    )
    
    # Convertir a mayúsculas
    texto_mayusculas = texto_sin_acentos.upper()
    
    # Eliminar comas, puntos y otros caracteres no alfanuméricos, pero permitir el espacio y asterisco
    texto_limpio = re.sub(r'[^A-Z0-9\s\*]', '', texto_mayusculas)

    # Guardar el texto limpio en un nuevo archivo
    with open('cleaned_text.txt', 'w', encoding='utf-8') as f:
        f.write(texto_limpio)
    
    return texto_limpio

def input_data():
    
    # Limpiar el texto con la función process_text
    cleaned_text = process_text('input.txt')
    
    # Guardar el texto limpio en cleaned_text.txt
    with open('cleaned_text.txt', 'w') as f:
        f.write(cleaned_text)
        
    # Retornar el texto limpio
    return cleaned_text

# Función para leer el texto limpio desde cleaned_text.txt
def input_text():
    with open('cleaned_text.txt', 'r') as f:
        cleaned_text = f.read()
    return cleaned_text

def output_text(text, methodName):
    with open(f'output_{methodName}.txt', 'w') as f:
        f.write(text)
        
alphabet = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
        'K': 10, 'L': 11, 'M': 12, 'N': 13, 'Ñ': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
        'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, ' ': 27, '*': 28
    }

# Funcion para contar la frecuencia de cada letra en el texto desde el alfabeto definido
def count_letters(text):
    freq = {letter: 0 for letter in alphabet}
    for char in text:
        if char in alphabet:
            freq[char] += 1
    # devuelve ordenado por cantidad de letras
    return dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))