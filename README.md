# Program Cipher

Program ini adalah implementasi dari beberapa algoritma cipher, yaitu Vigenere, Playfair, dan Hill Cipher. Program menggunakan antarmuka GUI berbasis Tkinter untuk memudahkan pengguna dalam melakukan enkripsi dan dekripsi teks.

## Fitur Utama
- **Vigenere Cipher**: Menggunakan sebuah kata kunci untuk melakukan pergeseran pada setiap karakter dari teks.
- **Playfair Cipher**: Menggunakan sebuah tabel 5x5 dengan pasangan karakter untuk mengenkripsi dan mendekripsi teks.
- **Hill Cipher**: Menggunakan matriks 3x3 untuk melakukan enkripsi dan dekripsi teks berbasis aljabar linear.

## Persyaratan Sistem
- Python 3.x
- Library Tkinter

## Instalasi
1. Clone repository atau unduh program ini.
2. Install library yang dibutuhkan.

## Menjalankan Program

### Menggunakan Terminal

1. Buka terminal di direktori tempat menyimpan file program ini.
   
2. Jalankan program dengan perintah:
    ```bash
    python chiper.py
    ```

### Menggunakan Editor Kode seperti Visual Studio Code

1. Buka Visual Studio Code atau editor kode Python lain yang digunakan.

2. Buka folder proyek di mana program berada:
    - Pilih **File > Open Folder** di Visual Studio Code.
    - Arahkan ke folder tempat menyimpan file program ini, kemudian klik **Select Folder**.

3. Jalankan program:
    - Di Visual Studio Code, pastikan telah membuka file `chiper.py`.
    - Tekan tombol **F5** atau pilih **Run > Start Debugging** untuk menjalankan program.
    - Jendela GUI akan muncul dan program dapat digunakan.

## Cara Penggunaan

1. **Pilih metode cipher**: Bisa memilih antara tiga metode cipher yang tersedia:
   - **Vigenere**
   - **Playfair**
   - **Hill**

2. **Masukkan Kunci**: Kunci harus minimal 12 karakter. Kunci ini akan digunakan untuk proses enkripsi atau dekripsi.

3. **Masukkan teks**: Dapat mengetikkan teks secara langsung di kotak teks atau mengunggah file `.txt` yang berisi teks yang akan dienkripsi atau didekripsi.

4. **Klik 'Enkripsi' atau 'Dekripsi'**: Pilih operasi yang diinginkan. Program akan menampilkan hasilnya di bagian "Hasil".

5. **Unggah file**: Jika ingin mengenkripsi atau mendekripsi teks dari file, klik tombol "Unggah File" dan pilih file teks.

### Catatan
- Pastikan kunci yang digunakan cocok dengan cipher yang dipilih. Misalnya, kunci untuk Hill Cipher harus bisa diubah menjadi matriks 3x3.
- Saat menggunakan Hill Cipher, pastikan teks yang dimasukkan panjangnya merupakan kelipatan dari 3. Jika tidak, teks akan diisi dengan karakter tambahan.

## Struktur Program

- **vigenere_cipher()**: Fungsi untuk enkripsi dan dekripsi dengan Vigenere cipher.
- **playfair_cipher()**: Fungsi untuk enkripsi dan dekripsi dengan Playfair cipher.
- **hill_cipher()**: Fungsi untuk enkripsi dan dekripsi dengan Hill cipher.
- **matrix_mod_inv()**: Fungsi untuk menghitung invers matriks 3x3 untuk Hill cipher.
- **encrypt()**: Fungsi untuk meng-enkripsi teks yang dimasukkan.
- **decrypt()**: Fungsi untuk mendekripsi teks yang dimasukkan.
- **upload_file()**: Fungsi untuk mengunggah file teks yang akan dienkripsi atau didekripsi.
