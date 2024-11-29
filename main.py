from cryptosystem1 import encrypt, decrypt, text_to_numbers, numbers_to_text, multiplicative_inverse
from cryptosystem2 import encrypt_blocks, decrypt_blocks, split_into_blocks, text_to_numbers, numbers_to_text
from text_processing import input_data, output_text, count_letters

def main():
    print("Bienvenido a los criptosistemas.")
    print("Elige una opción:")
    print("1. Criptosistema 1 (función lineal)")
    print("2. Criptosistema 2 (transformación lineal)")
    print("3. Salir")
    
    option = input("Ingrese el número de la opción: ")
   
    cleaned_text = input_data()
    print("Texto limpio: \n", count_letters(cleaned_text))
    
    if option == '1':
        # Criptosistema 1   
        
        # a = int(input("Ingrese el valor de 'a' (un número entre 1 y 28): "))
        # b = int(input("Ingrese el valor de 'b' (un número entre 0 y 28): "))
        a = 5
        b = 21
        
        # Encriptar el texto
        encrypted_text = encrypt(cleaned_text, a, b)
        
        output_text(numbers_to_text(encrypted_text), "encrypt_criptosistema1")
        print("")
        print("Texto Encriptado: \n", numbers_to_text(encrypted_text))
        print("")
        
        # Desencriptar el texto
        decrypted_text = decrypt(numbers_to_text(encrypted_text), a, b)
        output_text(numbers_to_text(decrypted_text), "decrypt_criptosistema1")
        print("Texto Desencriptado: \n", numbers_to_text(decrypted_text))
        print("")
        
        count_letters(numbers_to_text(encrypted_text))
        print("Texto limpio: \n", count_letters(cleaned_text))
        print("cantidad de letras en el texto encriptado: \n", count_letters(numbers_to_text(encrypted_text)))
    
    elif option == '2':
        # Criptosistema 2
        
        # Matriz de transformación T y vector b (puedes ajustarlos según sea necesario)
        T = [[2, 1, 0], [1, 1, 0], [0, 0, 1]]
        b = [1, 2, 3]
        
        # Dividir el texto en bloques
        blocks = split_into_blocks(cleaned_text)
        
        # Encriptar los bloques
        encrypted_blocks = encrypt_blocks(blocks, T, b)
        print("")
        #pasar los encrypted_blocks a Numeros to text 
        print("Texto Encriptado por Bloques: \n", ''.join([numbers_to_text(block) for block in encrypted_blocks]))
        print("")
        
        text = ''.join([numbers_to_text(block) for block in encrypted_blocks])
        count_letters(text)
        print("Texto limpio: \n", count_letters(cleaned_text))
        print("cantidad de letras en el texto encriptado: \n", count_letters(text))
        output_text(text, "encrypt_criptosistema2")
        
        # Desencriptar los bloques
        decrypted_blocks = decrypt_blocks(encrypted_blocks, T, b)
        decrypted_text = ''.join([numbers_to_text(block) for block in decrypted_blocks])
        print("Texto Desencriptado por Bloques: \n", decrypted_text)
        print("")
        output_text(decrypted_text, "decrypt_criptosistema2")
    
    elif option == '3':
        print("Saliendo del programa...")
    else:
        print("Opción no válida, por favor ingrese 1, 2 o 3.")

if __name__ == "__main__":
    main()
