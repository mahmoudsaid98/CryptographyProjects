import tkinter as tk
from tkinter import messagebox

 def create_matrix(key):
    matrix = []
    used_letters = set()
    key = key.upper().replace("J", "I")   
    
     for letter in key:
        if letter not in used_letters:
            matrix.append(letter)
            used_letters.add(letter)
    
     alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for letter in alphabet:
        if letter not in used_letters:
            matrix.append(letter)
            used_letters.add(letter)
    
     matrix_5x5 = [matrix[i:i+5] for i in range(0, 25, 5)]
    return matrix_5x5

 def prepare_text(text):
    text = text.upper().replace("J", "I")  
    text = text.replace(" ", "")   
     prepared_text = ""
    for i in range(0, len(text), 2):
        prepared_text += text[i]
        if i + 1 < len(text):
            if text[i] == text[i + 1]:
                prepared_text += "X"
            prepared_text += text[i + 1]
     if len(prepared_text) % 2 != 0:
        prepared_text += "X"
    return prepared_text

 def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None

 def encrypt_pair(matrix, pair):
    a, b = pair[0], pair[1]
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)
    
     if row_a == row_b:
        return matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
     elif col_a == col_b:
        return matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
     else:
        return matrix[row_a][col_b] + matrix[row_b][col_a]

 def decrypt_pair(matrix, pair):
    a, b = pair[0], pair[1]
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)
    
     if row_a == row_b:
        return matrix[row_a][(col_a - 1) % 5] + matrix[row_b][(col_b - 1) % 5]
     elif col_a == col_b:
        return matrix[(row_a - 1) % 5][col_a] + matrix[(row_b - 1) % 5][col_b]
     else:
        return matrix[row_a][col_b] + matrix[row_b][col_a]

 def encrypt(plaintext, key):
    matrix = create_matrix(key)
    prepared_text = prepare_text(plaintext)
    ciphertext = ""
    for i in range(0, len(prepared_text), 2):
        pair = prepared_text[i:i+2]
        ciphertext += encrypt_pair(matrix, pair)
    return ciphertext

 def decrypt(ciphertext, key):
    matrix = create_matrix(key)
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        pair = ciphertext[i:i+2]
        plaintext += decrypt_pair(matrix, pair)
     plaintext = plaintext.replace("X", "")
    return plaintext

 def open_encryption_interface():
    encryption_window = tk.Toplevel(root)
    encryption_window.title("Encryption")
    encryption_window.geometry("400x300")

     tk.Label(encryption_window, text="Plaintext:").grid(row=0, column=0, padx=10, pady=10)
    plaintext_entry = tk.Entry(encryption_window, width=30)
    plaintext_entry.grid(row=0, column=1, padx=10, pady=10)

     tk.Label(encryption_window, text="Key:").grid(row=1, column=0, padx=10, pady=10)
    key_entry = tk.Entry(encryption_window, width=30)
    key_entry.grid(row=1, column=1, padx=10, pady=10)

     matrix_label = tk.Label(encryption_window, text="Matrix will appear here", font=("Arial", 10))
    matrix_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

     result_label = tk.Label(encryption_window, text="", font=("Arial", 12))
    result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

     def on_encrypt():
        plaintext = plaintext_entry.get()
        key = key_entry.get()
        if not plaintext or not key:
            messagebox.showerror("Error", "Please enter both plaintext and key.")
            return
         matrix = create_matrix(key)
        matrix_text = "\n".join([" ".join(row) for row in matrix])
        matrix_label.config(text=f"Matrix:\n{matrix_text}")
         ciphertext = encrypt(plaintext, key)
        result_label.config(text=f"Encrypted Text: {ciphertext}")

    encrypt_button = tk.Button(encryption_window, text="Encrypt", command=on_encrypt)
    encrypt_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

 def open_decryption_interface():
    decryption_window = tk.Toplevel(root)
    decryption_window.title("Decryption")
    decryption_window.geometry("400x300")

     tk.Label(decryption_window, text="Ciphertext:").grid(row=0, column=0, padx=10, pady=10)
    ciphertext_entry = tk.Entry(decryption_window, width=30)
    ciphertext_entry.grid(row=0, column=1, padx=10, pady=10)

     tk.Label(decryption_window, text="Key:").grid(row=1, column=0, padx=10, pady=10)
    key_entry = tk.Entry(decryption_window, width=30)
    key_entry.grid(row=1, column=1, padx=10, pady=10)

     matrix_label = tk.Label(decryption_window, text="Matrix will appear here", font=("Arial", 10))
    matrix_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

     result_label = tk.Label(decryption_window, text="", font=("Arial", 12))
    result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

     def on_decrypt():
        ciphertext = ciphertext_entry.get()
        key = key_entry.get()
        if not ciphertext or not key:
            messagebox.showerror("Error", "Please enter both ciphertext and key.")
            return
         matrix = create_matrix(key)
        matrix_text = "\n".join([" ".join(row) for row in matrix])
        matrix_label.config(text=f"Matrix:\n{matrix_text}")
         plaintext = decrypt(ciphertext, key)
        result_label.config(text=f"Decrypted Text: {plaintext}")

    decrypt_button = tk.Button(decryption_window, text="Decrypt", command=on_decrypt)
    decrypt_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

 root = tk.Tk()
root.title("Playfair Cipher")
root.geometry("300x150")

 
tk.Label(root, text="Playfair Cipher", font=("Arial", 16)).pack(pady=10)

 encrypt_button = tk.Button(root, text="Encrypt", command=open_encryption_interface, width=20)
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=open_decryption_interface, width=20)
decrypt_button.pack(pady=5)

 root.mainloop()
