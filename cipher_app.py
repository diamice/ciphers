import tkinter as tk
from tkinter import messagebox
from xor import xor_cipher, xor_digits
from caesar import Caesar
from vigenere import Vigenere
from playfair import Playfair
from rsa import RSA


def run_app():
    def encrypt():
        algorithm = encryption_var.get()
        text = input_text.get("1.0", tk.END).strip()
        key = key_entry.get().strip()

        try:
            if algorithm == "XOR":
                if not key:
                    raise ValueError("Ключ для XOR не может быть пустым.")
                if text.isdigit():
                    result = xor_digits(int(text), int(key))
                else:
                    result = xor_cipher(text.encode('utf8'), key)
            elif algorithm == "Цезарь":
                if not key.isdigit():
                    raise ValueError("Сдвиг для Цезаря должен быть числом.")
                shift = int(key)
                caesar_cipher = Caesar(text, shift)
                result = caesar_cipher.encode()
            elif algorithm == "Виженер":
                if not key:
                    raise ValueError("Ключ для Виженера не может быть пустым.")
                vigenere_cipher = Vigenere(key)
                result = vigenere_cipher.encode(text)
            elif algorithm == "Плейфер":
                if not key:
                    raise ValueError("Ключ для Плейфера не может быть пустым.")
                playfair_cipher = Playfair(key)
                result = playfair_cipher.encode(text)
            elif algorithm == "RSA":
                rsa = RSA()
                ciphertext = rsa.encode(text)
                result = f"Зашифрованное: {ciphertext}\nРасшифрованное: {rsa.decode(ciphertext)}"
            else:
                messagebox.showerror("Ошибка", "Выберите алгоритм шифрования")
                return

            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, result)

        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    window = tk.Tk()
    window.title("Шифрование")
    window.geometry("400x400")

    tk.Label(window, text="Выберите шифр").pack()

    encryption_var = tk.StringVar(value="XOR")
    tk.OptionMenu(window, encryption_var, "XOR", "Цезарь", "Виженер", "Плейфер", "RSA").pack()

    tk.Label(window, text="Введите текст для шифрования").pack()
    input_text = tk.Text(window, height=5, width=40)
    input_text.pack()

    tk.Label(window, text="Введите ключ (или сдвиг)").pack()
    key_entry = tk.Entry(window)
    key_entry.pack()

    tk.Button(window, text="Зашифровать", command=encrypt).pack()

    tk.Label(window, text="Результат").pack()
    output_text = tk.Text(window, height=5, width=40)
    output_text.pack()

    window.mainloop()


if __name__ == "__main__":
    run_app()
