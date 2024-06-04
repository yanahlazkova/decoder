import customtkinter as ctk

class MyWindow(ctk.CTk):
    def __init__(self):
        self.current_value_slider = 0
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
        # self.slider_shift = ctk.CTkSlider(self, width=300, from_=-15, to=15, number_of_steps=30, command=self.update_cipher)
        self.slider_shift = CustomSlider(self, from_=-10, to=10, number_of_ticks=20, command=self.update_cipher)
        self.slider_shift.pack(pady=5)
        # self.slider_shift.set(0)

        # Метка для отображения зашифрованного текста
        self.label_output = ctk.CTkLabel(self, text="Зашифрованный текст: ")
        self.label_output.pack(pady=10)

    def update_cipher(self, value):
        if self.current_value_slider < value:
            self.current_value_slider += 1
            shift = self.current_value_slider
        else:
            self.current_value_slider -= 1
            shift = self.current_value_slider

        shift =
        text = self.entry_text.get()
        encrypted_text = self.caesar_cipher(text, shift)
        self.label_output.configure(text=f"Зашифрованный текст: {encrypted_text}")

    def caesar_cipher(self, text, shift):
        result = []
        for char in text:
            print('isascii', char.isascii())
            if char.isalpha():
                code_char = ord(char)
                print(code_char, chr(code_char), )
                shift_amount = 65 if char.isupper() else 97
                result.append(chr((ord(char) - shift_amount + shift) % 26 + shift_amount))
            else:
                result.append(char)

        return ''.join(result)


class CustomSlider(ctk.CTkFrame):
    def __init__(self, master, from_=0, to=100, number_of_ticks=10, **kwargs):
        super().__init__(master, **kwargs)
        self.slider = ctk.CTkSlider(self, width=450, from_=from_, to=to, command=self.update_value)
        self.slider.pack(pady=10, padx=10)
        self.slider.set(0)

        self.ticks_frame = ctk.CTkFrame(self)
        self.ticks_frame.pack(fill="x", padx=10)

        self.from_ = from_
        self.to = to
        self.number_of_ticks = number_of_ticks
        self.tick_labels = []

        self.create_ticks()

    def create_ticks(self):
        for i in range(self.number_of_ticks + 1):
            tick_value = self.from_ + i * (self.to - self.from_) / self.number_of_ticks
            tick_label = ctk.CTkLabel(self.ticks_frame, text=f"{int(tick_value)}")
            tick_label.pack(side="left", expand=True)
            self.tick_labels.append(tick_label)

    def update_value(self, value):
        self.slider.set(int(value))
        self.light_value(int(value))
        print(f"Slider value: {int(value)}")

    def light_value(self, value):
        for label in self.tick_labels:
            if int(label.cget("text")) == value:
                label.configure(text_color="red")
            else:
                label.configure(text_color="black")


