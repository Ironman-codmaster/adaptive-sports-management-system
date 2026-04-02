from tobaseoz import *

import customtkinter
from tkinter import messagebox as mb
import datetime

class Korsatkich:

        def korsatkich_qosh(self, idu, fam, ism, shar):
            new_oq_window = customtkinter.CTkToplevel(self)
            new_oq_window.resizable(False, False)
            new_oq_window.title("Ko'rsatkich kiritish")
            #-----------------------------
            window_width = 320
            window_height = 450

            # Получаем размеры экрана
            screen_width = new_oq_window.winfo_screenwidth()
            screen_height = new_oq_window.winfo_screenheight()

            # Вычисляем координаты для центра
            center_x = int((screen_width - window_width) / 2)
            center_y = int((screen_height - window_height) / 2)

            # Устанавливаем размеры и положение окна
            new_oq_window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

            #------------------------------

            new_oq_window.configure(fg_color="#dee2fb")

            ft = customtkinter.CTkFont("",size=14, weight="bold")

            title = customtkinter.CTkLabel(new_oq_window, text=f" ID:{idu} {fam} { ism} {shar} ga \n ko'rsatkich qoshish", font=ft, text_color='blue')
            title.place(x=20, y=5)

            sana_label = customtkinter.CTkLabel(new_oq_window, text="Sanani kiriting: ", font=ft)
            sana_label.place(x=20, y=60)

            yuz_label = customtkinter.CTkLabel(new_oq_window, text="100 metrga yugurish: ", font=ft)
            yuz_label.place(x=20, y=90)

            tortyuz_label = customtkinter.CTkLabel(new_oq_window, text="400 metrga yugurish: ", font=ft)
            tortyuz_label.place(x=20, y=120)

            birmingbeshyuz_label = customtkinter.CTkLabel(new_oq_window, text="1500 metrga yugurish: ", font=ft)
            birmingbeshyuz_label.place(x=20, y=150)

            club_label = customtkinter.CTkLabel(new_oq_window, text="CLUB THROW uloqtirish: ", font=ft)
            club_label.place(x=20, y=180)

            arava_label = customtkinter.CTkLabel(new_oq_window, text="Arava: ", font=ft)
            arava_label.place(x=20, y=210)

            balsak_label = customtkinter.CTkLabel(new_oq_window, text="Balandlikka sakrash: ", font=ft)
            balsak_label.place(x=20, y=240)

            disk_label = customtkinter.CTkLabel(new_oq_window, text="Disk uloqtirish: ", font=ft)
            disk_label.place(x=20, y=270)

            nayza_label = customtkinter.CTkLabel(new_oq_window, text="Nayza uloqtirish: ", font=ft)
            nayza_label.place(x=20, y=300)

            uzunlik_label = customtkinter.CTkLabel(new_oq_window, text="Uzunlikka sakrash: ", font=ft)
            uzunlik_label.place(x=20, y=330)

            yadro_label = customtkinter.CTkLabel(new_oq_window, text="Yadro uloqtirish:", font=ft)
            yadro_label.place(x=20, y=360)

            # ---------------------------------------
            #Entry

            sana = customtkinter.CTkEntry(new_oq_window, font=ft, width=100, border_width=1,
                                          placeholder_text="kun.oy.yil")
            sana.place(x=200, y=60)

            yuz = customtkinter.CTkEntry(new_oq_window, font=ft, width=100, border_width=1)
            yuz.place(x=200, y=90)

            tortyuz = customtkinter.CTkEntry(new_oq_window, font=ft, width=100, border_width=1)
            tortyuz.place(x=200, y=120)

            birmingbeshyuz = customtkinter.CTkEntry(new_oq_window, font=ft, width=100, border_width=1)
            birmingbeshyuz.place(x=200, y=150)

            club = customtkinter.CTkEntry(new_oq_window, font=ft, width=100, border_width=1)
            club.place(x=200, y=180)

            arava = customtkinter.CTkEntry(new_oq_window, font=ft, width=100, border_width=1)
            arava.place(x=200, y=210)

            balandlsak = customtkinter.CTkEntry(new_oq_window, font=ft, width=100, border_width=1)
            balandlsak.place(x=200, y=240)

            disk = customtkinter.CTkEntry(new_oq_window, font=ft, width=100, border_width=1)
            disk.place(x=200, y=270)

            nayza = customtkinter.CTkEntry(new_oq_window, font=ft, width=100, border_width=1)
            nayza.place(x=200, y=300)

            uzunlik = customtkinter.CTkEntry(new_oq_window, font=ft, width=100, border_width=1)
            uzunlik.place(x=200, y=330)

            yadro = customtkinter.CTkEntry(new_oq_window, font=ft, width=100, border_width=1)
            yadro.place(x=200, y=360)

            def detect_type(s):
                if s=='':
                    return 0
                s = s.strip()
                try:
                    int(s)
                    return int
                except ValueError:
                    pass

                try:
                    float(s)
                    return float
                except ValueError:
                    pass

                return str


            def oq_qosh_baza():
                date_str = sana.get()
                try:
                    datetime.datetime.strptime(date_str, "%d.%m.%Y")
                    sana.configure(border_color="green")
                except ValueError:
                    sana.configure(border_color="red")
                    mb.showerror("Xatolik", "Sanani kun.oy.yil ko'rinishida kiriting namuna: 01.01.2025 ")
                else:
                    ddd =[str(idu),date_str]
                    int_float = [yuz.get(), tortyuz.get(), birmingbeshyuz.get(), club.get(), arava.get(), balandlsak.get(), disk.get(), nayza.get(), uzunlik.get(), yadro.get()]
                    xato = 0
                    for lll in int_float:
                        if detect_type(lll) == str:
                            xato+=1
                    if xato == 0:
                        for lll in int_float:
                            ddd.append(lll)
                        ddd = ['0' if x == '' else x for x in ddd]
                        ddd_tuple = tuple(ddd)
                        stat_obj = Stat()
                        stat_obj.korsatkich_kiritish(ddd_tuple)
                        mb.showinfo("Diqqat!", "Ma'lumotlar Muvaffaqiyatli saqlandi !!!")
                        new_oq_window.destroy()
                    else:
                        mb.showerror("Xatolik", "Ko'rsatkichlarni to'g'ri kiriting")


            bt = ("", 13, "bold")

            button = customtkinter.CTkButton(new_oq_window, text="Saqlash", font=bt, width=60, fg_color="green", command=oq_qosh_baza)
            button.place(x=20, y=410)

            def close_window():
                new_oq_window.destroy()

            button = customtkinter.CTkButton(new_oq_window, text="Bekor qilish", font=bt, width=60, fg_color="red", command=close_window)
            button.place(x=110, y=410)

            new_oq_window.grab_set()
