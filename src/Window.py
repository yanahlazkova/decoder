import customtkinter as ctk

class MyWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("light")  # Настройка внешнего вида (может быть "light", "dark", или "system")
        ctk.set_default_color_theme("blue")  # Установка темы

        self.title("Decoder")
        self.geometry("500x300")

        # Заголовок
        self.label_title = ctk.CTkLabel(self, text="Шифр Цезаря", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_title.pack(pady=10)

        # Метка и поле ввода текста
        self.label_input = ctk.CTkLabel(self, text="Введи текст для зашифровки")
        self.label_input.pack(pady=5)
        self.entry_text = ctk.CTkEntry(self, width=300)
        self.entry_text.pack(pady=5)

        # Метка и слайдер для выбора размаха сдвига
        self.label_slider = ctk.CTkLabel(self, text="Выбери размах сдвига")
        self.label_slider.pack(pady=5)
        self.slider_shift = ctk.CTkSlider(self, width=300, from_=-15, to=15, number_of_steps=30, command=self.update_cipher)
        self.slider_shift.pack(pady=5)
        self.slider_shift.set(0)

        # Метка для отображения зашифрованного текста
        self.label_output = ctk.CTkLabel(self, text="Зашифрованный текст: ")
        self.label_output.pack(pady=10)

    def update_cipher(self, value):
        shift = int(value)
        text = self.entry_text.get()
        encrypted_text = self.caesar_cipher(text, shift)
        self.label_output.configure(text=f"Зашифрованный текст: {encrypted_text}")

    def caesar_cipher(self, text, shift):
        result = []
        for char in text:
            print('isascii', char.isascii())
            if char.isalpha():
                print(ord(char))
                shift_amount = 65 if char.isupper() else 97
                result.append(chr((ord(char) - shift_amount + shift) % 26 + shift_amount))
            else:
                result.append(char)
        return ''.join(result)



