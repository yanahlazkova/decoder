import customtkinter as ctk

class MyWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("My CustomTkinter App")
        self.geometry("400x400")

        # Создание и размещение виджетов

        # Метка
        self.label = ctk.CTkLabel(self, text="Hello, CustomTkinter!")
        self.label.pack(pady=10)

        # Поле ввода
        self.entry = ctk.CTkEntry(self, placeholder_text="Enter text here")
        self.entry.pack(pady=10)

        # Кнопка
        self.button = ctk.CTkButton(self, text="Click Me", command=self.button_clicked)
        self.button.pack(pady=10)

        # Список
        self.listbox = ctk.CTkListbox(self)
        self.listbox.pack(pady=10)
        self.listbox.insert(0, "Item 1")
        self.listbox.insert(1, "Item 2")
        self.listbox.insert(2, "Item 3")

        # Переключатель
        self.checkbox = ctk.CTkCheckBox(self, text="Check Me")
        self.checkbox.pack(pady=10)

        # Радиокнопки
        self.radio_var = ctk.StringVar(value="1")
        self.radiobutton1 = ctk.CTkRadioButton(self, text="Option 1", variable=self.radio_var, value="1")
        self.radiobutton2 = ctk.CTkRadioButton(self, text="Option 2", variable=self.radio_var, value="2")
        self.radiobutton1.pack(pady=5)
        self.radiobutton2.pack(pady=5)

    def button_clicked(self):
        print("Button clicked! Entry text:", self.entry.get())

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
