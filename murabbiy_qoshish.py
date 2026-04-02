from tobaseoz import *
import customtkinter
from tkinter import messagebox as mb
import datetime

class Murabbiyqosh:

        def murabbiy_qosh(self):

            stat = Stat()  # ma'lumotlar ombori klassi obektini yaratish
            new_oq_window = customtkinter.CTkToplevel(self)
            #new_oq_window.geometry("500x800")
            new_oq_window.resizable(False, False)
            new_oq_window.title("Yangi murabbiy qoshish oynasi")
            #-----------------------------
            window_width = 320
            window_height = 550

            # Получаем размеры экрана
            screen_width = new_oq_window.winfo_screenwidth()
            screen_height = new_oq_window.winfo_screenheight()

            # Вычисляем координаты для центра
            center_x = int((screen_width - window_width) / 2)
            center_y = int((screen_height - window_height) / 2)

            # Устанавливаем размеры и положение окна
            new_oq_window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

            #------------------------------

            new_oq_window.configure(fg_color="silver")

            ft = customtkinter.CTkFont("",size=14, weight="bold")

            title = customtkinter.CTkLabel(new_oq_window, text="Yangi murabbiy qoshish oynasi", font=ft, text_color='blue')
            title.place(x=20, y=5)

            fam_label = customtkinter.CTkLabel(new_oq_window, text="Familiyasi: ", font=ft)
            fam_label.place(x=20, y=30)

            ism_label = customtkinter.CTkLabel(new_oq_window, text="Ismi: ", font=ft)
            ism_label.place(x=20, y=60)

            shar_label = customtkinter.CTkLabel(new_oq_window, text="Otasining ismi: ", font=ft)
            shar_label.place(x=20, y=90)

            tugs_label = customtkinter.CTkLabel(new_oq_window, text="Tug'ulgan sanasi: ", font=ft)
            tugs_label.place(x=20, y=120)

            tel1_label = customtkinter.CTkLabel(new_oq_window, text="Telefon raqami: ", font=ft)
            tel1_label.place(x=20, y=150)

            tel2_label = customtkinter.CTkLabel(new_oq_window, text="Telefon raqami: ", font=ft)
            tel2_label.place(x=20, y=180)

            pas_met_label = customtkinter.CTkLabel(new_oq_window, text="Pasport/Metrika: ", font=ft)
            pas_met_label.place(x=20, y=210)

            res_label = customtkinter.CTkLabel(new_oq_window, text="Respublika: ", font=ft)
            res_label.place(x=20, y=240)

            vil_label = customtkinter.CTkLabel(new_oq_window, text="Viloyati: ", font=ft)
            vil_label.place(x=20, y=270)

            tum_label = customtkinter.CTkLabel(new_oq_window, text="Tumani:", font=ft)
            tum_label.place(x=20, y=300)

            mfy_label = customtkinter.CTkLabel(new_oq_window, text="MFY: ", font=ft)
            mfy_label.place(x=20, y=330)

            koch_label = customtkinter.CTkLabel(new_oq_window, text="Ko'chasi uyi: ", font=ft)
            koch_label.place(x=20, y=360)

            jshshr_label = customtkinter.CTkLabel(new_oq_window, text="JSHSHR: ", font=ft)
            jshshr_label.place(x=20, y=390)

            nogirg_label = customtkinter.CTkLabel(new_oq_window, text="Nogironlik guv: ", font=ft)
            nogirg_label.place(x=20, y=420)

            status_label = customtkinter.CTkLabel(new_oq_window, text="Status: ", font=ft)
            status_label.place(x=20, y=450)

            # ---------------------------------------
            #Entry

            fam_km = customtkinter.CTkEntry(new_oq_window, font=ft, width=150, border_width=1)
            fam_km.place(x=150, y=30)

            ism_km = customtkinter.CTkEntry(new_oq_window, font=ft, width=150, border_width=1)
            ism_km.place(x=150, y=60)

            sharif_km = customtkinter.CTkEntry(new_oq_window, font=ft, width=150, border_width=1)
            sharif_km.place(x=150, y=90)

            tugyil_km = customtkinter.CTkEntry(new_oq_window, font=ft, width=150, border_width=1, placeholder_text="kun.oy.yil")
            tugyil_km.place(x=150, y=120)

            tel1_km = customtkinter.CTkEntry(new_oq_window, font=ft, width=150, border_width=1)
            tel1_km.place(x=150, y=150)

            tel2_km = customtkinter.CTkEntry(new_oq_window, font=ft, width=150, border_width=1)
            tel2_km.place(x=150, y=180)

            pas_met_km = customtkinter.CTkEntry(new_oq_window, font=ft, width=150, border_width=1)
            pas_met_km.place(x=150, y=210)

            resp_km = customtkinter.CTkEntry(new_oq_window, font=ft, width=150, border_width=1)
            resp_km.place(x=150, y=240)

            vil_km = customtkinter.CTkComboBox(
                master=new_oq_window,font=ft,width=150, border_width=1,
                values=["Andijon",
            "Buxoro",
            "Fargʻona",
            "Jizzax",
            "Xorazm",
            "Namangan",
            "Navoiy",
            "Qashqadaryo",
            "Qoraqalpogʻiston Respublikasi",
            "Samarqand",
            "Sirdaryo",
            "Surxondaryo",
            "Toshkent"])

            vil_km.place(x=150, y=270)

            tum_km = customtkinter.CTkComboBox(
                master=new_oq_window,font=ft,width=150, border_width=1,

             values =  ["Marhamat",
            "Andijon",
            "Asaka",
            "Baliqchi",
            "Boʻston",
            "Buloqboshi",
            "Izboskan",
            "Jalaquduq",
            "Xoʻjaobod",
            "Qoʻrgʻontepa",
            "Oltinkoʻl",
            "Paxtaobod",
            "Shahrixon",
            "Ulugʻnor",
            "Xonobod",
            "Andijon(shahar)"])

            tum_km.place(x=150, y=300)

            mfy_km = customtkinter.CTkEntry(new_oq_window, font=ft, width=150, border_width=1)
            mfy_km.place(x=150, y=330)

            koch_km = customtkinter.CTkEntry(new_oq_window, font=ft, width=150, border_width=1)
            koch_km.place(x=150, y=360)

            jshshr_km = customtkinter.CTkEntry(new_oq_window, font=ft, width=150, border_width=1)
            jshshr_km.place(x=150, y=390)

            nogirg_km = customtkinter.CTkEntry(new_oq_window, font=ft, width=150, border_width=1)
            nogirg_km.place(x=150, y=420)

            status_km = customtkinter.CTkComboBox(
                master=new_oq_window,font=ft,width=150, border_width=1,

             values =  ["ishlamoqda",
            "davolanishda",
            "sportni tark etdi",
            "boshqa sabab bilan yo'q"])
            status_km.place(x=150, y=450)

            def oq_qosh_baza():
                date_str = tugyil_km.get()
                try:
                    datetime.datetime.strptime(date_str, "%d.%m.%Y")
                    tugyil_km.configure(border_color="green")
                except ValueError:
                    tugyil_km.configure(border_color="red")
                    mb.showerror("Xatolik", "Sanani kun.oy.yil ko'rinishida kiriting namuna: 01.01.2025 ")
                else:
                    entries = [ fam_km, ism_km, sharif_km, tugyil_km, tel1_km, tel2_km, pas_met_km, resp_km, vil_km, tum_km, mfy_km, koch_km, jshshr_km, nogirg_km, status_km]
                    all_filled = all(
                        (entry.get().strip() != '') if hasattr(entry, 'get') else False
                        for entry in entries
                    )
                    if all_filled:
                        entries_get = (fam_km.get(), ism_km.get(), sharif_km.get(), tugyil_km.get(), tel1_km.get(), tel2_km.get(), pas_met_km.get(), resp_km.get(), vil_km.get(), tum_km.get(), mfy_km.get(),
                                   koch_km.get(), jshshr_km.get(), nogirg_km.get(), status_km.get())
                        stat.murabbiy_bazaga_qoshish(entries_get)
                        mb.showinfo("Diqqat!", "Ma'lumotlar Muvaffaqiyatli saqlandi !!!")
                        new_oq_window.destroy()
                    else:
                        for entry in entries:
                            if entry.get().strip() == '':
                                entry.configure(border_color="red")  # выделяем пустые
                            else:
                                entry.configure(border_color="green")  # правильные — зелёным
                        mb.showerror("Xatolik", "Ma'lumotlarni to'liq kiriting!!!")

            bt = ("", 13, "bold")

            button = customtkinter.CTkButton(new_oq_window, text="Saqlash", font=bt, width=60, fg_color="green", command=oq_qosh_baza)
            button.place(x=20, y=500)

            def close_window():
                new_oq_window.destroy()

            button = customtkinter.CTkButton(new_oq_window, text="Bekor qilish", font=bt, width=60, fg_color="red", command=close_window)
            button.place(x=110, y=500)

            new_oq_window.grab_set()
