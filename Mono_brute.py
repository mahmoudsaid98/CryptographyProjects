import tkinter as tk
from tkinter import messagebox

# Function to perform brute force attack
def brute_force_attack():
    ciphertext = entry_ciphertext.get().strip()
    if not ciphertext:
        messagebox.showwarning("Input Error", "Please enter ciphertext!")
        return

    output_text.delete(1.0, tk.END)  # Clear previous output

    alfabet = "abcdefghijklmnopqrstuvwxyz"
    results = []

    # Perform brute force attack for all possible shifts (0 to 25)
    for i in range(26):
        decrypted_text = ""
        for j in ciphertext.lower():
            if j in alfabet:
                shifted_char = alfabet[(alfabet.index(j) + i) % 26]
                decrypted_text += shifted_char
            else:
                decrypted_text += j
        # Display keys as letters (A-Z) instead of numbers (0-25)
        key_char = chr(ord('A') + i)
        results.append(f"Key {key_char}: {decrypted_text}\n")

    # Display results in the output text box
    output_text.insert(tk.END, "".join(results))

    # Display the "owe me" text below the output box
    owe_label.config(text="If I win, you owe me 10 dollars! 😊", fg="green")

# Function to restart the program
def restart():
    entry_ciphertext.delete(0, tk.END)  # Clear input field
    output_text.delete(1.0, tk.END)  # Clear output text box
    owe_label.config(text="")  # Clear the "owe me" text

# Create the main window
root = tk.Tk()
root.title("Monoalphabetic Cipher Brute Force Attack")
root.geometry("600x550")
root.configure(bg="#f0f0f0")  # Set background color

# Add a label for the ciphertext input
label_ciphertext = tk.Label(
    root,
    text="Enter Ciphertext:",
    font=("Arial", 12, "bold"),
    bg="#f0f0f0",
    fg="blue",
)
label_ciphertext.pack(pady=10)

# Add an entry box for the ciphertext
entry_ciphertext = tk.Entry(root, width=50, font=("Arial", 12))
entry_ciphertext.pack(pady=10)

# Add a button to trigger the brute force attack
button_attack = tk.Button(
    root,
    text="Brute Force Attack",
    command=brute_force_attack,
    font=("Arial", 12, "bold"),
    bg="lightblue",
    fg="black",
)
button_attack.pack(pady=10)

# Add a restart button
button_restart = tk.Button(
    root,
    text="Restart",
    command=restart,
    font=("Arial", 12, "bold"),
    bg="lightgreen",
    fg="black",
)
button_restart.pack(pady=10)

# Add a label for the output
label_output = tk.Label(
    root,
    text="Decryption Results:",
    font=("Arial", 12, "bold"),
    bg="#f0f0f0",
    fg="blue",
)
label_output.pack(pady=10)

# Add a text box to display the results
output_text = tk.Text(root, width=70, height=15, font=("Arial", 12))
output_text.pack(pady=10)

# Add a label for the "owe me" text
owe_label = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    bg="#f0f0f0",
    fg="green",
)
owe_label.pack(pady=10)

# Run the GUI
root.mainloop()