import tkinter as tk
from tkinter import filedialog, messagebox

# Fungsi Vigenere Cipher
def vigenere_cipher(text, key, encrypt=True):
    result = []
    key_length = len(key)
    key = key.lower()
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('a')
            if not encrypt:
                shift = -shift
            new_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char if char.islower() else new_char.upper())
        else:
            result.append(char)
    return ''.join(result)

# Fungsi Playfair Cipher
def playfair_cipher(text, key, encrypt=True):
    key = ''.join(key.split()).lower()
    text = ''.join(text.split()).lower()

    # Membuat tabel Playfair
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key_table = []
    for char in key:
        if char not in key_table and char in alphabet:
            key_table.append(char)
    
    for char in alphabet:
        if char not in key_table:
            key_table.append(char)

    # Membuat pasangan huruf
    pairs = []
    i = 0
    while i < len(text):
        if i + 1 < len(text):
            if text[i] == text[i + 1]:
                pairs.append(text[i] + 'x')
                i += 1
            else:
                pairs.append(text[i] + text[i + 1])
                i += 2
        else:
            pairs.append(text[i] + 'x')
            i += 1

    # Enkripsi dan Dekripsi
    result = []
    for pair in pairs:
        row1, col1 = divmod(key_table.index(pair[0]), 5)
        row2, col2 = divmod(key_table.index(pair[1]), 5)

        if row1 == row2: 
            new_pair = key_table[row1 * 5 + (col1 + (1 if encrypt else -1)) % 5] + \
                       key_table[row2 * 5 + (col2 + (1 if encrypt else -1)) % 5]
        elif col1 == col2: 
            new_pair = key_table[((row1 + (1 if encrypt else -1)) % 5) * 5 + col1] + \
                                 key_table[((row2 + (1 if encrypt else -1)) % 5) * 5 + col2]
        else:
            new_pair = key_table[row1 * 5 + col2] + key_table[row2 * 5 + col1]

        result.append(new_pair)

    decrypted_text = ''.join(result)
    if not encrypt:
        # Menghapus 'x' yang tidak perlu pada dekripsi
        decrypted_text = decrypted_text.replace('x', '')
        if len(decrypted_text) > 0 and decrypted_text[-1] == 'x':
            decrypted_text = decrypted_text[:-1]

    return decrypted_text

# Fungsi untuk mencari invers modular
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Fungsi untuk menghitung determinan matriks 3x3
def determinant(matrix):
    return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[2][1] * matrix[1][2]) -
            matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
            matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))

# Fungsi untuk menghitung invers matriks 3x3
def matrix_mod_inv(matrix, mod):
    det = determinant(matrix)
    det_inv = mod_inverse(det, mod)
    if det_inv is None:
        raise ValueError("Invers determinan tidak ditemukan, matriks tidak dapat diinvers.")

    # Menghitung matriks kofaktor
    cofactor_matrix = [
        [
            (matrix[(i + 1) % 3][(j + 1) % 3] * matrix[(i + 2) % 3][(j + 2) % 3] - 
             matrix[(i + 1) % 3][(j + 2) % 3] * matrix[(i + 2) % 3][(j + 1) % 3]) % mod
            for j in range(3)
        ]
        for i in range(3)
    ]

    # Transpose kofaktor untuk mendapatkan matriks adjoin
    adjugate_matrix = [[cofactor_matrix[j][i] for j in range(3)] for i in range(3)]

    # Menghitung invers
    inverse_matrix = [[(det_inv * adjugate_matrix[i][j]) % mod for j in range(3)] for i in range(3)]
    return inverse_matrix

# Fungsi Hill Cipher
def hill_cipher(text, key, encrypt=True):
    # Mengkonversi kunci ke dalam matriks 3x3
    key_matrix = [[ord(key[i * 3 + j].upper()) - 65 for j in range(3)] for i in range(3)]

    if not encrypt:
        key_matrix = matrix_mod_inv(key_matrix, 26)

    # Mengkonversi teks ke dalam blok 3 karakter
    def text_to_matrix(text):
        matrix = []
        for i in range(0, len(text), 3):
            row = []
            for char in text[i:i + 3]:
                row.append(ord(char.upper()) - 65)
            while len(row) < 3:
                row.append(0)
            matrix.append(row)
        return matrix

    # Melakukan operasi matriks untuk enkripsi/dekripsi
    text_matrix = text_to_matrix(text)
    result_matrix = []
    
    for row in text_matrix:
        result_row = []
        for j in range(3):
            result_value = sum(row[k] * key_matrix[k][j] for k in range(3)) % 26
            result_row.append(result_value)
        result_matrix.append(result_row)

    result = []
    for row in result_matrix:
        for num in row:
            result.append(chr(num + 65))

    return ''.join(result)

# Fungsi dekripsi
def decrypt():
    try:
        text = input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Masukkan teks atau unggah file!")
            return
        
        key = key_entry.get().strip()
        if len(key) < 12:
            messagebox.showwarning("Warning", "Kunci minimal 12 karakter!")
            return
        
        method = cipher_method.get()
        if method == "Vigenere":
            result = vigenere_cipher(text, key, encrypt=False)
        elif method == "Playfair":
            result = playfair_cipher(text, key, encrypt=False)
        elif method == "Hill":
            result = hill_cipher(text, key, encrypt=False)
        else:
            result = "Metode tidak valid."

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Fungsi enkripsi
def encrypt():
    try:
        text = input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Masukkan teks atau unggah file!")
            return
        
        key = key_entry.get().strip()
        if len(key) < 12:
            messagebox.showwarning("Warning", "Kunci minimal 12 karakter!")
            return
        
        method = cipher_method.get()
        if method == "Vigenere":
            result = vigenere_cipher(text, key, encrypt=True)
        elif method == "Playfair":
            result = playfair_cipher(text, key, encrypt=True)
        elif method == "Hill":
            result = hill_cipher(text, key, encrypt=True)
        else:
            result = "Metode tidak valid."

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Fungsi untuk mengunggah file
def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            input_text.delete("1.0", tk.END)
            input_text.insert(tk.END, file.read())

# GUI
root = tk.Tk()
root.title("Program Cipher")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

cipher_method = tk.StringVar(value="Vigenere")
tk.Label(frame, text="Pilih Metode Cipher:").grid(row=0, column=0)
tk.OptionMenu(frame, cipher_method, "Vigenere", "Playfair", "Hill").grid(row=0, column=1)

tk.Label(frame, text="Masukkan Kunci (minim 12 karakter):").grid(row=1, column=0)
key_entry = tk.Entry(frame, width=30)
key_entry.grid(row=1, column=1)

tk.Label(frame, text="Masukkan Teks atau Unggah File:").grid(row=2, column=0)
input_text = tk.Text(frame, height=10, width=40)
input_text.grid(row=3, columnspan=2)

tk.Button(frame, text="Unggah File", command=upload_file).grid(row=4, column=0)
tk.Button(frame, text="Enkripsi", command=encrypt).grid(row=4, column=1)
tk.Button(frame, text="Dekripsi", command=decrypt).grid(row=4, column=2)

tk.Label(frame, text="Hasil:").grid(row=5, column=0)
output_text = tk.Text(frame, height=10, width=40)
output_text.grid(row=6, columnspan=2)

root.mainloop()