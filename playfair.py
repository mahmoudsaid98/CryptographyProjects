import tkinter as tk
from tkinter import messagebox

# Function to create the 5x5 matrix
def create_matrix(key):
    matrix = []
    used_letters = set()
    key = key.upper().replace("J", "I")  # Replace 'J' with 'I'
    
    # Add letters from the key to the matrix
    for letter in key:
        if letter not in used_letters:
            matrix.append(letter)
            used_letters.add(letter)
    
    # Add remaining letters from the alphabet
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for letter in alphabet:
        if letter not in used_letters:
            matrix.append(letter)
            used_letters.add(letter)
    
    # Convert the list into a 5x5 matrix
    matrix_5x5 = [matrix[i:i+5] for i in range(0, 25, 5)]
    return matrix_5x5

# Function to prepare the text for encryption/decryption
def prepare_text(text):
    text = text.upper().replace("J", "I")  # Replace 'J' with 'I'
    text = text.replace(" ", "")  # Remove spaces
    # Add 'X' between double letters
    prepared_text = ""
    for i in range(0, len(text), 2):
        prepared_text += text[i]
        if i + 1 < len(text):
            if text[i] == text[i + 1]:
                prepared_text += "X"
            prepared_text += text[i + 1]
    # If the length is odd, add 'X' at the end
    if len(prepared_text) % 2 != 0:
        prepared_text += "X"
    return prepared_text

# Function to find the position of a letter in the matrix
def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None

# Function to encrypt a pair of letters
def encrypt_pair(matrix, pair):
    a, b = pair[0], pair[1]
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)
    
    # Same row
    if row_a == row_b:
        return matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
    # Same column
    elif col_a == col_b:
        return matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
    # Rectangle
    else:
        return matrix[row_a][col_b] + matrix[row_b][col_a]

# Function to decrypt a pair of letters
def decrypt_pair(matrix, pair):
    a, b = pair[0], pair[1]
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)
    
    # Same row
    if row_a == row_b:
        return matrix[row_a][(col_a - 1) % 5] + matrix[row_b][(col_b - 1) % 5]
    # Same column
    elif col_a == col_b:
        return matrix[(row_a - 1) % 5][col_a] + matrix[(row_b - 1) % 5][col_b]
    # Rectangle
    else:
        return matrix[row_a][col_b] + matrix[row_b][col_a]

# Function to encrypt the plaintext
def encrypt(plaintext, key):
    matrix = create_matrix(key)
    prepared_text = prepare_text(plaintext)
    ciphertext = ""
    for i in range(0, len(prepared_text), 2):
        pair = prepared_text[i:i+2]
        ciphertext += encrypt_pair(matrix, pair)
    return ciphertext

# Function to decrypt the ciphertext
def decrypt(ciphertext, key):
    matrix = create_matrix(key)
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        pair = ciphertext[i:i+2]
        plaintext += decrypt_pair(matrix, pair)
    # Remove any extra 'X' added during encryption
    plaintext = plaintext.replace("X", "")
    return plaintext

# Encryption Interface
def open_encryption_interface():
    encryption_window = tk.Toplevel(root)
    encryption_window.title("Encryption")
    encryption_window.geometry("400x300")

    # Plaintext input
    tk.Label(encryption_window, text="Plaintext:").grid(row=0, column=0, padx=10, pady=10)
    plaintext_entry = tk.Entry(encryption_window, width=30)
    plaintext_entry.grid(row=0, column=1, padx=10, pady=10)

    # Key input
    tk.Label(encryption_window, text="Key:").grid(row=1, column=0, padx=10, pady=10)
    key_entry = tk.Entry(encryption_window, width=30)
    key_entry.grid(row=1, column=1, padx=10, pady=10)

    # Matrix display
    matrix_label = tk.Label(encryption_window, text="Matrix will appear here", font=("Arial", 10))
    matrix_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Result label
    result_label = tk.Label(encryption_window, text="", font=("Arial", 12))
    result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # Encrypt button
    def on_encrypt():
        plaintext = plaintext_entry.get()
        key = key_entry.get()
        if not plaintext or not key:
            messagebox.showerror("Error", "Please enter both plaintext and key.")
            return
        # Create and display the matrix
        matrix = create_matrix(key)
        matrix_text = "\n".join([" ".join(row) for row in matrix])
        matrix_label.config(text=f"Matrix:\n{matrix_text}")
        # Encrypt the plaintext
        ciphertext = encrypt(plaintext, key)
        result_label.config(text=f"Encrypted Text: {ciphertext}")

    encrypt_button = tk.Button(encryption_window, text="Encrypt", command=on_encrypt)
    encrypt_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Decryption Interface
def open_decryption_interface():
    decryption_window = tk.Toplevel(root)
    decryption_window.title("Decryption")
    decryption_window.geometry("400x300")

    # Ciphertext input
    tk.Label(decryption_window, text="Ciphertext:").grid(row=0, column=0, padx=10, pady=10)
    ciphertext_entry = tk.Entry(decryption_window, width=30)
    ciphertext_entry.grid(row=0, column=1, padx=10, pady=10)

    # Key input
    tk.Label(decryption_window, text="Key:").grid(row=1, column=0, padx=10, pady=10)
    key_entry = tk.Entry(decryption_window, width=30)
    key_entry.grid(row=1, column=1, padx=10, pady=10)

    # Matrix display
    matrix_label = tk.Label(decryption_window, text="Matrix will appear here", font=("Arial", 10))
    matrix_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Result label
    result_label = tk.Label(decryption_window, text="", font=("Arial", 12))
    result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # Decrypt button
    def on_decrypt():
        ciphertext = ciphertext_entry.get()
        key = key_entry.get()
        if not ciphertext or not key:
            messagebox.showerror("Error", "Please enter both ciphertext and key.")
            return
        # Create and display the matrix
        matrix = create_matrix(key)
        matrix_text = "\n".join([" ".join(row) for row in matrix])
        matrix_label.config(text=f"Matrix:\n{matrix_text}")
        # Decrypt the ciphertext
        plaintext = decrypt(ciphertext, key)
        result_label.config(text=f"Decrypted Text: {plaintext}")

    decrypt_button = tk.Button(decryption_window, text="Decrypt", command=on_decrypt)
    decrypt_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Main Menu
root = tk.Tk()
root.title("Playfair Cipher")
root.geometry("300x150")

# Title
tk.Label(root, text="Playfair Cipher", font=("Arial", 16)).pack(pady=10)

# Buttons
encrypt_button = tk.Button(root, text="Encrypt", command=open_encryption_interface, width=20)
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=open_decryption_interface, width=20)
decrypt_button.pack(pady=5)

# Run the application
root.mainloop()