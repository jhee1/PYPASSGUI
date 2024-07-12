import random
import tkinter as tk
from tkinter import messagebox

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    try:
        nr_letters = int(entry_letters.get())
        nr_symbols = int(entry_symbols.get())
        nr_numbers = int(entry_numbers.get())

        password_list = []
        for _ in range(nr_letters):
            password_list.append(random.choice(letters))

        for _ in range(nr_symbols):
            password_list.append(random.choice(symbols))

        for _ in range(nr_numbers):
            password_list.append(random.choice(numbers))

        random.shuffle(password_list)
        password = "".join(password_list)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for letters, symbols, and numbers.")

# Tworzenie głównego okna aplikacji
root = tk.Tk()
root.title("PyPassword Generator")

# Etykiety i pola wejściowe
label_letters = tk.Label(root, text="Number of letters:")
label_letters.grid(row=0, column=0, padx=10, pady=10)

entry_letters = tk.Entry(root)
entry_letters.grid(row=0, column=1, padx=10, pady=10)

label_symbols = tk.Label(root, text="Number of symbols:")
label_symbols.grid(row=1, column=0, padx=10, pady=10)

entry_symbols = tk.Entry(root)
entry_symbols.grid(row=1, column=1, padx=10, pady=10)

label_numbers = tk.Label(root, text="Number of numbers:")
label_numbers.grid(row=2, column=0, padx=10, pady=10)

entry_numbers = tk.Entry(root)
entry_numbers.grid(row=2, column=1, padx=10, pady=10)

# Pole wynikowe
label_password = tk.Label(root, text="Generated Password:")
label_password.grid(row=3, column=0, padx=10, pady=10)

entry_password = tk.Entry(root)
entry_password.grid(row=3, column=1, padx=10, pady=10)

# Przycisk generujący hasło
button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.grid(row=4, column=0, columnspan=2, pady=10)

# Uruchomienie głównej pętli aplikacji
root.mainloop()
