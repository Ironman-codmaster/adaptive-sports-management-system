# pyinstaller --onefile --add-data "test_images;test_images" loading.py
# pyinstaller --onefile --noconsole --icon=icon.ico --add-data "test_images;test_images" loading.py
# pyinstaller --onefile --noconsole --icon=icon.ico --add-data "test_images;test_images" loading.py
import customtkinter
import tkinter as tk

import os
import sys
from PIL import Image, ImageTk
import sqlite3 as sqm

from anketa import Anketa
from murabbiy import Murabbiy
from protokol import Protokol
from tobase import Stat
class App(customtkinter.CTk):

    user_tuple_on_base = ()

    def __init__(self):
        super().__init__()

        # -NEW ing getting--------------------------------------------------------------------------------------------------------------------------------

        # Функция для безопасной загрузки ресурсов (работает и в .py, и в .exe)
        def resource_path(relative_path):
            try:
                base_path = sys._MEIPASS  # путь при запуске .exe
            except AttributeError:
                base_path = os.path.abspath(".")  # путь при запуске .py
            return os.path.join(base_path, relative_path)

        # Путь к папке с изображениями
        image_path = resource_path("test_images")
        # Загрузка изображений
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logoparauz1.png")),
                                                 size=(60, 66))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logoparauz1.png")),
                                                       size=(500, 520))

        self.icon_image_excell = customtkinter.CTkImage(Image.open(os.path.join(image_path, "excell.png")),
                                                        size=(30, 30))
        self.icon_image_word = customtkinter.CTkImage(Image.open(os.path.join(image_path, "word.png")), size=(30, 30))
        self.icon_image_grafik = customtkinter.CTkImage(Image.open(os.path.join(image_path, "grafik.png")),
                                                        size=(30, 30))
        self.icon_image_printer = customtkinter.CTkImage(Image.open(os.path.join(image_path, "printer.png")),
                                                         size=(30, 30))
        self.icon_image_icfoto = customtkinter.CTkImage(Image.open(os.path.join(image_path, "iconfoto.png")),
                                                        size=(30, 30))
        self.icon_image_greenpasport = customtkinter.CTkImage(Image.open(os.path.join(image_path, "greenpasport.png")),
                                                              size=(30, 30))
        self.icon_image_redpasport = customtkinter.CTkImage(Image.open(os.path.join(image_path, "redpasport.png")),
                                                            size=(30, 30))
        self.icon_image_m1 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "m1.png")), size=(30, 30))
        self.icon_image_m2 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "m2.png")), size=(30, 30))
        self.icon_image_m3 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "m3.png")), size=(30, 30))
        self.icon_image_dir = customtkinter.CTkImage(Image.open(os.path.join(image_path, "dir.png")), size=(30, 30))

        self.murabbiy_img = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "murabbiy_light.png")),
            dark_image=Image.open(os.path.join(image_path, "murabbiy_light.png")),
            size=(60, 60)
        )

        self.buyurtma_img = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "blar.png")),
            dark_image=Image.open(os.path.join(image_path, "blar_light.png")),
            size=(40, 40)
        )

        self.kassa_img = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "kassa_light.png")),
            dark_image=Image.open(os.path.join(image_path, "kassa_light.png")),
            size=(40, 40)
        )

        self.users_img = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "kassa_light.png")),
            dark_image=Image.open(os.path.join(image_path, "kassa_light.png")),
            size=(40, 40)
        )

        # -NEW ing getting-END-------
        # Proektning papkalarini bor yoki yoqligini tekshirish agar papka yo bo'lsa o'zi qoshib qoyadi
        papkalar = ["fotopath","mukofot1","mukofot2","mukofot3","murabbiy_pasport_uz","murabbiy_pasport_zagran","murabbiy_photo","pasport_uz","pasport_zagran"] #,"test_images"
        for pk in papkalar:
            if not os.path.exists(pk):
                os.makedirs(pk)

        if not os.path.exists("sb.db"):
            with sqm.connect("sb.db") as con:
                cur = con.cursor()
                cur.execute("""
                        CREATE TABLE IF NOT EXISTS autoraize (
                            idau INTEGER PRIMARY KEY AUTOINCREMENT,
                            login TEXT,
                        	password TEXT
                        )
                        """)
                # Login va parol yaratadi
                logpar = ("Mavlonbek", "Grin_tay")
                cur.execute(f"INSERT INTO autoraize (login, password) VALUES {logpar}")

                cur.execute("""
                        CREATE TABLE IF NOT EXISTS korsatkichlar (
                           	idk	INTEGER PRIMARY KEY AUTOINCREMENT,
                        	id_user	TEXT,
                        	sana TEXT,
                        	yuzm TEXT,
                        	tortyuzm TEXT,
                        	birmingbeshm TEXT,
                        	club TEXT,
                        	arava TEXT,
                        	balandlik TEXT,
                        	disk TEXT,
                        	nayza TEXT,
                        	uzunlik	TEXT,
                        	yadro TEXT
                        )
                        """)

                cur.execute("""
                        CREATE TABLE IF NOT EXISTS murabbiy (
                        	idmurabbiy	INTEGER PRIMARY KEY AUTOINCREMENT,
                        	fam TEXT,
                        	ism TEXT,
                        	sharif TEXT,
                        	tugyil TEXT,
                        	tel1 TEXT,
                        	tel2 TEXT,
                        	pasmet TEXT,
                        	resp TEXT,
                        	vil TEXT,
                        	tum TEXT,
                        	mfy TEXT,
                        	koch TEXT,
                        	jshshr TEXT,
                        	nogirg TEXT,
                        	status TEXT,
                        	murabbiy_photo TEXT,
                        	murabbiy_pasport_uz	TEXT,
                        	murabbiy_pasport_zagran	TEXT,
                        	mukofot1 TEXT,
                        	mukofot2 TEXT,
                        	mukofot3 TEXT
                        )
                        """)

                cur.execute("""
                        CREATE TABLE IF NOT EXISTS user (
                        	id INTEGER PRIMARY KEY AUTOINCREMENT,
                        	fam TEXT,
                        	ism TEXT,
                        	sharif TEXT,
                        	tugyil NUMERIC,
                        	tel1 TEXT,
                        	tel2 TEXT,
                        	pasmet TEXT,
                        	resp TEXT,
                        	vil TEXT,
                        	tum TEXT,
                        	mfy TEXT,
                        	koch TEXT,
                        	jshshr TEXT,
                        	nogirg TEXT,
                        	status TEXT,
                        	fotopath TEXT,
                        	pasport_uz TEXT,
                        	pasport_zagran TEXT,
                        	murabbiy TEXT,
                        	mukofot1 TEXT,
                        	mukofot2 TEXT,
                        	mukofot3 TEXT
                        )
                        """)

                con.commit()

        # password window #############################################################
        password_window = customtkinter.CTkToplevel(self)
        password_window.resizable(False, False)
        password_window.overrideredirect(True)
        password_window.title("Parrolni kiriting!!!")

        # -----------------------------
        psw_width = 500
        psw_height = 300

        # Получаем размеры экрана
        screen_width = password_window.winfo_screenwidth()
        screen_height = password_window.winfo_screenheight()

        # Вычисляем координаты для центра
        center_x = int((screen_width - psw_width) / 2)
        center_y = int((screen_height - psw_height) / 2)

        # Устанавливаем размеры и положение окна
        password_window.geometry(f"{psw_width}x{psw_height}+{center_x}+{center_y}")

        # ------------------------------

        password_window.configure(fg_color="black")

        ft = customtkinter.CTkFont("", size=17, weight="bold")

        login_entry = customtkinter.CTkEntry(password_window,
                                             font=ft,
                                             width=250,
                                             border_width=1,
                                             placeholder_text="login",
                                             corner_radius=20,
                                             height=35)
        login_entry.place(relx=0.5, y=80, anchor="center")

        password_entry = customtkinter.CTkEntry(password_window,
                                                font=ft,
                                                width=250,
                                                border_width=1,
                                                placeholder_text="password",
                                                show="*",
                                                corner_radius=20,
                                                height=35)
        password_entry.place(relx=0.5, y=140, anchor="center")


        def close_window():
            lp = Stat.login_password()
            lpz = 0
            for ilp in lp:
                if login_entry.get() == ilp[1] and password_entry.get() == ilp[2]:
                   lpz += 1

            if lpz > 0:
                password_window.destroy()
            else:
                attenshen_label_pass.configure(text="Siz noto'g'li login va parol kiritdingiz!!!")


        kirish_button = customtkinter.CTkButton(password_window,
                                         text="Kirish",
                                         font=ft,
                                         height=35,
                                         width=250,
                                         corner_radius=20,
                                         fg_color="red",

                                         command=close_window)

        kirish_button.place(relx=0.5, y=200, anchor="center")

        attenshen_label_pass = customtkinter.CTkLabel(password_window, text="", font=ft, text_color="red")
        attenshen_label_pass.place(relx=0.5, y=260, anchor="center")

        def close_programm():
            self.destroy()

        chiqish_button = customtkinter.CTkButton(password_window,
                                         text="X",
                                         font=ft,
                                         height=10,
                                         width=25,
                                         corner_radius=30,
                                         fg_color="red",

                                         command=close_programm)

        chiqish_button.place(relx=1.0, rely=0.0, x=-10, y=10, anchor="ne")

        attenshen_label_pass = customtkinter.CTkLabel(password_window, text="", font=ft, text_color="red")
        attenshen_label_pass.place(relx=0.5, y=260, anchor="center")


        password_window.grab_set()

        # password window end#############################################################
        #------------------------------------------------------------------------------------------------------------------------

        self.title("ANDIJON SHAXAR YENGIL ATLETIKA ISM")
        self.iconbitmap(resource_path("test_images/icon.ico"))
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()

        # Задаем максимальный размер, если экран меньше
        window_width = min(w - 100, 1080)
        window_height = min(h - 100, 670)

        # print(window_width)
        # print(window_height)

        # Центрируем окно
        pos_x = (w - window_width) // 2
        pos_y = (h - window_height) // 2

        # print(pos_x)
        # print(pos_y)


        self.geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")


        #screen = str(w - 450) + 'x' + str(h - 150)
        #self.geometry(screen)

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(7, weight=1)

        # lOGO
        # Andijon shaxar\nsportning o'yin turlari\nva yengil atletikaga\nihtisoslashtirilgan\nsport maktabi
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="ANDIJON SHAXAR\nYENGIL ATLETIKA\nISM", image=self.logo_image, text_color="#c31934",
                                                            compound="top", font=customtkinter.CTkFont(size=10, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=10, pady=10)

        # Buttons Shrift
        self.button_font = customtkinter.CTkFont(size=10, weight="bold")

        # Murabbiy Botton
        self.murabbiy_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=20, border_spacing=5,
                                                   text="",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.murabbiy_img, anchor="center", compound="top",
                                                   font=self.button_font, command=self.murabbiy_button_event)
        self.murabbiy_button.grid(row=1, column=0, sticky="ew")

        # Home Botton
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=20, border_spacing=5, text="Sportchilar",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.buyurtma_img, anchor="center",compound="top",font=self.button_font, command=self.home_button_event)
        self.home_button.grid(row=2, column=0, sticky="ew")

        # Frame 2 Botton
        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=20, border_spacing=5, text="Protokol",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.kassa_img, anchor="center",compound="top",font=self.button_font, command=self.frame_2_button_event)
        self.frame_2_button.grid(row=3, column=0, sticky="ew")

        # Frame 3 Botton
        # self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=20, border_spacing=5, text="Milliy O'zbekiston \n chempionati \n KICHKINALAR",
        #                                               fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
        #                                               image=self.users_img, anchor="center",compound="top",font=self.button_font, command=self.frame_3_button_event)
        # self.frame_3_button.grid(row=4, column=0, sticky="ew")

        # Frame 4 Botton
        # self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=20, border_spacing=5, text="Milliy O'zbekiston \n chempionati \n KATTALAR",
        #                                               fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
        #                                               image=self.users_img, anchor="center",compound="top",font=self.button_font, command=self.frame_4_button_event)
        # self.frame_4_button.grid(row=5, column=0, sticky="ew")

        # Frame 5 Botton
        # self.frame_5_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=20,
        #                                               border_spacing=5, text="Xalqaro \n musobaqalar",
        #                                               fg_color="transparent", text_color=("gray10", "gray90"),
        #                                               image=self.users_img,hover_color=("gray70", "gray30"), anchor="center",compound="top",font=self.button_font, command=self.frame_5_button_event)
        # self.frame_5_button.grid(row=6, column=0, sticky="ew")

        # Menu Light Dark System

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark"],command=self.change_appearance_mode_event, width=90)
        self.appearance_mode_menu.grid(row=7, column=0, padx=5, pady=10, sticky="s")

        # Murabbiy anketasi
        # ===================================================
        Murabbiy.murabbiy(self)
        # ===================================================

        # O'quvchi anketasi
        # ===================================================
        Anketa.anketa(self)
        # ===================================================

        # Protokol anketasi
        # ===================================================
        Protokol.protokol(self)
        # ===================================================

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame.grid_columnconfigure(0, weight=1)

        self.third_frame_large_image_label = customtkinter.CTkLabel(self.third_frame, text="3",
                                                                     image=self.large_test_image)
        self.third_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        # create forth frame
        self.forth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.forth_frame.grid_columnconfigure(0, weight=1)

        self.forth_frame_large_image_label = customtkinter.CTkLabel(self.forth_frame, text="4",
                                                                    image=self.large_test_image)
        self.forth_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)


        # create fifth frame
        self.fifth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fifth_frame.grid_columnconfigure(0, weight=1)

        self.fifth_frame_large_image_label = customtkinter.CTkLabel(self.fifth_frame, text="Fifth frame",
                                                                    image=self.large_test_image)
        self.fifth_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)


        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.murabbiy_button.configure(fg_color=("gray75", "gray25") if name == "murabbiy" else "transparent")
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        #self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        # self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")
        # self.frame_5_button.configure(fg_color=("gray75", "gray25") if name == "frame_5" else "transparent")

        # show selected frame
        if name == "murabbiy":
            self.murabbiy_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()

        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()

        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()

        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

        if name == "frame_4":
            self.forth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.forth_frame.grid_forget()

        if name == "frame_5":
            self.fifth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fifth_frame.grid_forget()

    def murabbiy_button_event(self):
        self.select_frame_by_name("murabbiy")
    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")

    def frame_5_button_event(self):
        self.select_frame_by_name("frame_5")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

def run():
    app = App()
    app.run()

# datas=[('test_images/icon.ico', 'test_images'),
#     	('test_images/icon.png', 'test_images'),
#     	('test_images/blar.png', 'test_images'),
#     	('test_images/blar_light.png', 'test_images'),
#     	('test_images/dir.png', 'test_images'),
#     	('test_images/excell.png', 'test_images'),
#     	('test_images/ft.png', 'test_images'),
#     	('test_images/grafik.png', 'test_images'),
#     	('test_images/greenpasport.png', 'test_images'),
#     	('test_images/iconfoto.png', 'test_images'),
#     	('test_images/kassa_light.png', 'test_images'),
#     	('test_images/kyoq.png', 'test_images'),
#     	('test_images/laylak.png', 'test_images'),
#     	('test_images/logoparauz.png', 'test_images'),
#     	('test_images/logoparauz1.png', 'test_images'),
#     	('test_images/logoparauzbf.png', 'test_images'),
#     	('test_images/m1.png', 'test_images'),
#     	('test_images/m2.png', 'test_images'),
#     	('test_images/m3.png', 'test_images'),
#     	('test_images/murabbiy.png', 'test_images'),
#     	('test_images/murabbiy_light.png', 'test_images'),
#     	('test_images/printer.png', 'test_images'),
#     	('test_images/qyoq.png', 'test_images'),
#     	('test_images/redpasport.png', 'test_images'),
#     	('test_images/settings.png', 'test_images'),
#     	('test_images/userfoto.png', 'test_images'),
#     	('test_images/userfoto2.png', 'test_images'),
#     	('test_images/word.png', 'test_images')
#     	],

