import customtkinter as ctk
import threading
import time
import main  # Подключи сюда файл с App()
import sys
import os

class LoadingScreen(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Yuklanmoqda...")
        self.resizable(False, False)
        self.iconbitmap(self.resource_path("test_images/icon.ico"))
        psw_width = 400
        psw_height = 150

        # Получаем размеры экрана
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Вычисляем координаты для центра
        center_x = int((screen_width - psw_width) / 2)
        center_y = int((screen_height - psw_height) / 2)

        # Устанавливаем размеры и положение окна
        self.geometry(f"{psw_width}x{psw_height}+{center_x}+{center_y}")

        self.configure(fg_color="black")

        ctk.CTkLabel(self, text="Yuklanmoqda, iltimos kutib turing...", font=("Arial", 16), text_color="white").pack(pady=10)

        self.progress = ctk.CTkProgressBar(self, width=300, height=10)
        self.progress.pack(pady=20)
        self.progress.set(0)

        # Запуск загрузки в отдельном потоке
        threading.Thread(target=self.load_data, daemon=True).start()

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS  # путь при запуске .exe
        except AttributeError:
            base_path = os.path.abspath(".")  # путь при запуске .py
        return os.path.join(base_path, relative_path)

    def load_data(self):
        for i in range(101):
            time.sleep(0.02)  # Тут можно вставить реальные действия
            self.progress.set(i / 100)

        self.after(0, self.launch_main_app)

    def launch_main_app(self):
        self.destroy()
        main.App().mainloop()

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    app = LoadingScreen()
    app.mainloop()
