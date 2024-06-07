import customtkinter as ctk


class MyWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("light")  # Настройка внешнего вида (может быть "light", "dark", или "system")
        ctk.set_default_color_theme("blue")  # Установка темы

        self.shift = 0
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
        self.entry_text.bind("<Return>", self.on_enter_pressed)

        # Метка и слайдер для выбора размаха сдвига
        self.label_slider = ctk.CTkLabel(self, text="Выбери размах сдвига")
        self.label_slider.pack(pady=5)
        self.slider_shift = CustomSlider(self, from_=-10, to=10, number_of_ticks=20, command=self.update_cipher)
        self.slider_shift.pack(pady=5)

        # Метка для отображения зашифрованного текста
        self.label_output = ctk.CTkLabel(self, text="Зашифрованный текст: ")
        self.label_output.pack(pady=10)

    def on_enter_pressed(self, event):
        print(event)
        self.shift = 0
        self.slider_shift.__set__(0)
        text = self.entry_text.get()
        encrypted_text = self.caesar_cipher(text)
        self.label_output.configure(text=f"Зашифрованный текст: {encrypted_text}")

    def update_cipher(self, value):

        print(value, self.shift)
        if value >= 0:
            if self.shift <= value:
                self.shift += 1
            else:
                self.shift -= 1
        else:
            if self.shift < value:
                self.shift += 1
            else:
                self.shift -= 1
        print(self.shift)
        self.slider_shift.__set__(self.shift)
        text = self.entry_text.get()
        encrypted_text = self.caesar_cipher(text)
        self.label_output.configure(text=f"Зашифрованный текст: {encrypted_text}")

    def caesar_cipher(self, text):
        result = []
        for char in text:
            if char.isalpha():
                shift_amount = 65 if char.isupper() else 97
                result.append(chr((ord(char) - shift_amount + self.shift) % 26 + shift_amount))
            else:
                result.append(char)

        return ''.join(result)


class CustomSlider(ctk.CTkFrame):
    def __init__(self, master, from_=0, to=100, number_of_ticks=10, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command
        self.slider = ctk.CTkSlider(self, width=450, from_=from_, to=to, command=self.update_value)
        self.slider.pack(pady=10, padx=10)
        self.slider.set(0)

        self.ticks_frame = ctk.CTkFrame(self, height=30)
        self.ticks_frame.pack_propagate(False)  # Prevent the frame from resizing with its content
        self.ticks_frame.pack(fill="x", padx=10)

        self.from_ = from_
        self.to = to
        self.number_of_ticks = number_of_ticks
        self.tick_labels = []

        self.create_ticks()

    def __set__(self, value):
        print(value)
        self.slider.set(value)
        self.light_value(value)

    def create_ticks(self):
        for i in range(self.number_of_ticks + 1):
            tick_value = self.from_ + i * (self.to - self.from_) / self.number_of_ticks
            tick_label = ctk.CTkLabel(self.ticks_frame, text=f"{int(tick_value)}")
            # tick_label.pack(side="left", expand=True)
            tick_label.place(relx=i / self.number_of_ticks, rely=0.5, anchor='center')
            self.tick_labels.append(tick_label)

    def update_value(self, value):
        self.slider.set(int(value))
        self.light_value(int(value))
        if self.command:
            self.command(int(value))

    def light_value(self, value):
        for label in self.tick_labels:
            if int(label.cget("text")) == value:
                label.configure(text_color="red")
            else:
                label.configure(text_color="black")


# if __name__ == "__main__":
#     app = MyWindow()
#     app.mainloop()


