import customtkinter as ctk

# Inicializa a aplicação
ctk.set_appearance_mode("light")  # ou "dark"
ctk.set_default_color_theme("blue")  # ou qualquer outra cor

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Tela Inicial")
        self.geometry("400x300")

        # Botões
        self.button1 = ctk.CTkButton(self, text="Janela 1", command=lambda: self.open_window(1))
        self.button1.pack(pady=10)

        self.button2 = ctk.CTkButton(self, text="Janela 2", command=lambda: self.open_window(2))
        self.button2.pack(pady=10)

        self.button3 = ctk.CTkButton(self, text="Janela 3", command=lambda: self.open_window(3))
        self.button3.pack(pady=10)

        self.button4 = ctk.CTkButton(self, text="Janela 4", command=lambda: self.open_window(4))
        self.button4.pack(pady=10)

    def open_window(self, window_number):
        self.withdraw()  # Esconde a janela inicial
        new_window = SecondaryWindow(self, window_number)

    def restore(self):
        self.deiconify()  # Restaura a janela inicial

class SecondaryWindow(ctk.CTkToplevel):
    def __init__(self, parent, window_number):
        super().__init__(parent)
        self.title(f"Janela {window_number}")
        self.geometry("300x200")
        self.label = ctk.CTkLabel(self, text=f"Você está na Janela {window_number}")
        self.label.pack(pady=20)

        self.button_close = ctk.CTkButton(self, text="Fechar", command=self.close_window)
        self.button_close.pack(pady=10)

        # Restaura a janela inicial ao fechar
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def close_window(self):
        self.master.restore()  # Restaura a janela inicial
        self.destroy()  # Fecha a janela secundária

# Inicia a aplicação
if __name__ == "__main__":
    app = App()
    app.mainloop()
