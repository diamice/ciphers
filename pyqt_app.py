import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QPushButton,
    QLineEdit, QTextEdit, QComboBox, QMessageBox
)
from xor import xor_cipher, xor_digits
from caesar import Caesar
from vigenere import Vigenere
from playfair import Playfair
from rsa import RSA


class CipherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Шифрование")
        self.setGeometry(100, 100, 400, 500)

        self.layout = QVBoxLayout()

        self.algorithm_label = QLabel("Выберите шифр:")
        self.layout.addWidget(self.algorithm_label)

        self.encryption_var = QComboBox()
        self.encryption_var.addItems(["XOR", "Цезарь", "Виженер", "Плейфер", "RSA"])
        self.encryption_var.currentIndexChanged.connect(self.toggle_rsa_fields)
        self.layout.addWidget(self.encryption_var)

        self.input_label = QLabel("Введите текст для шифрования:")
        self.layout.addWidget(self.input_label)

        self.input_text = QTextEdit()
        self.layout.addWidget(self.input_text)

        self.key_label = QLabel("Введите ключ (или сдвиг):")
        self.layout.addWidget(self.key_label)

        self.key_entry = QLineEdit()
        self.layout.addWidget(self.key_entry)

        self.p_label = QLabel("Введите простое число p (для RSA):")
        self.layout.addWidget(self.p_label)
        self.p_entry = QLineEdit()
        self.layout.addWidget(self.p_entry)

        self.q_label = QLabel("Введите простое число q (для RSA):")
        self.layout.addWidget(self.q_label)
        self.q_entry = QLineEdit()
        self.layout.addWidget(self.q_entry)

        self.p_label.hide()
        self.p_entry.hide()
        self.q_label.hide()
        self.q_entry.hide()

        self.encrypt_button = QPushButton("Зашифровать")
        self.encrypt_button.clicked.connect(self.encrypt)
        self.layout.addWidget(self.encrypt_button)

        self.decrypt_button = QPushButton("Расшифровать")
        self.decrypt_button.clicked.connect(self.decrypt)
        self.layout.addWidget(self.decrypt_button)

        self.result_label = QLabel("Результат:")
        self.layout.addWidget(self.result_label)

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.layout.addWidget(self.output_text)

        self.setLayout(self.layout)

    def toggle_rsa_fields(self):
        """Отображаем или скрываем поля для p и q при выборе алгоритма RSA."""
        if self.encryption_var.currentText() == "RSA":
            self.key_label.hide()
            self.key_entry.hide()
            self.p_label.show()
            self.p_entry.show()
            self.q_label.show()
            self.q_entry.show()
        else:
            self.key_label.show()
            self.key_entry.show()
            self.p_label.hide()
            self.p_entry.hide()
            self.q_label.hide()
            self.q_entry.hide()

    def encrypt(self):
        algorithm = self.encryption_var.currentText()
        text = self.input_text.toPlainText().strip()

        try:
            if algorithm == "XOR":
                key = self.key_entry.text().strip()
                if not key:
                    raise ValueError("Ключ для XOR не может быть пустым.")
                if text.isdigit():
                    result = xor_digits(int(text), int(key))
                else:
                    result = xor_cipher(text.encode('utf8'), key)
            elif algorithm == "Цезарь":
                key = self.key_entry.text().strip()
                if not key.isdigit():
                    raise ValueError("Сдвиг для Цезаря должен быть числом.")
                shift = int(key)
                caesar_cipher = Caesar(text, shift)
                result = caesar_cipher.encode()
            elif algorithm == "Виженер":
                key = self.key_entry.text().strip()
                if not key:
                    raise ValueError("Ключ для Виженера не может быть пустым.")
                vigenere_cipher = Vigenere(key)
                result = vigenere_cipher.encode(text)
            elif algorithm == "Плейфер":
                key = self.key_entry.text().strip()
                if not key:
                    raise ValueError("Ключ для Плейфера не может быть пустым.")
                playfair_cipher = Playfair(key)
                result = playfair_cipher.encode(text)
            elif algorithm == "RSA":
                p_text = self.p_entry.text().strip()
                q_text = self.q_entry.text().strip()

                if p_text and q_text:
                    p = int(p_text)
                    q = int(q_text)
                    rsa = RSA(p, q)
                else:
                    raise ValueError("Необходимо ввести оба простых числа p и q для RSA.")

                ciphertext = rsa.encode(text)
                result = f"Зашифрованное: {ciphertext}\nРасшифрованное: {rsa.decode(ciphertext)}"
            else:
                QMessageBox.critical(self, "Ошибка", "Выберите алгоритм шифрования")
                return

            self.output_text.setPlainText(str(result))

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))

    def decrypt(self):
        algorithm = self.encryption_var.currentText()
        text = self.input_text.toPlainText().strip()

        try:
            if algorithm == "XOR":
                key = self.key_entry.text().strip()
                if not key:
                    raise ValueError("Ключ для XOR не может быть пустым.")
                if text.isdigit():
                    result = xor_digits(int(text), int(key))
                else:
                    result = xor_cipher(text.encode('utf8'), key)
            elif algorithm == "Цезарь":
                key = self.key_entry.text().strip()
                if not key.isdigit():
                    raise ValueError("Сдвиг для Цезаря должен быть числом.")
                shift = int(key)
                caesar_cipher = Caesar(text, shift)
                result = caesar_cipher.decode()
            elif algorithm == "Виженер":
                key = self.key_entry.text().strip()
                if not key:
                    raise ValueError("Ключ для Виженера не может быть пустым.")
                vigenere_cipher = Vigenere(key)
                result = vigenere_cipher.decode(text)
            elif algorithm == "Плейфер":
                key = self.key_entry.text().strip()
                if not key:
                    raise ValueError("Ключ для Плейфера не может быть пустым.")
                playfair_cipher = Playfair(key)
                result = playfair_cipher.decode(text)
            elif algorithm == "RSA":
                p_text = self.p_entry.text().strip()
                q_text = self.q_entry.text().strip()

                if p_text and q_text:
                    p = int(p_text)
                    q = int(q_text)
                    rsa = RSA(p, q)
                else:
                    raise ValueError("Необходимо ввести оба простых числа p и q для RSA.")

                ciphertext = eval(text)
                result = rsa.decode(ciphertext)
            else:
                QMessageBox.critical(self, "Ошибка", "Дешифрование доступно только для RSA.")
                return

            self.output_text.setPlainText(str(result))

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cipher_app = CipherApp()
    cipher_app.show()
    sys.exit(app.exec_())
