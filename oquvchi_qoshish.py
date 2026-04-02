from tobaseoz import *
import customtkinter
from tkinter import messagebox as mb
import datetime


class Oquvchi:

        def oquvchi_qosh(self):

            stat = Stat()  # ma'lumotlar ombori klassi obektini yaratish
            new_oq_window = customtkinter.CTkToplevel(self)
            #new_oq_window.geometry("500x800")
            new_oq_window.resizable(False, False)
            new_oq_window.title("Yangi o'quvchi qoshish oynasi")
            #-----------------------------
            window_width = 320
            window_height = 570

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

            title = customtkinter.CTkLabel(new_oq_window, text="Yangi o'quvchi qoshish oynasi", font=ft, text_color='blue')
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

            murabbiy_label = customtkinter.CTkLabel(new_oq_window, text="Murabbiy: ", font=ft)
            murabbiy_label.place(x=20, y=480)

            # ---------------------------------------
            #Entry

            fam_k = customtkinter.CTkEntry(new_oq_window, font=ft, width=150, border_width=1)
            fam_k.place(x=150, y=30)

            ism_k = customtkinter.CTkEntry(new_oq_window, font=ft, width=150, border_width=1)
            ism_k.place(x=150, y=60)

            sharif_k = customtkinter.CTkEntry(new_oq_window, font=ft, width=150, border_width=1)
            sharif_k.place(x=150, y=90)

            tugyil_k = customtkinter.CTkEntry(new_oq_window, font=ft, width=150, border_width=1, placeholder_text="kun.oy.yil")
            tugyil_k.place(x=150, y=120)

            tel1_k = customtkinter.CTkEntry(new_oq_window, font=ft, width=150, border_width=1)
            tel1_k.place(x=150, y=150)

            tel2_k = customtkinter.CTkEntry(new_oq_window, font=ft, width=150, border_width=1)
            tel2_k.place(x=150, y=180)

            pas_met_k = customtkinter.CTkEntry(new_oq_window, font=ft, width=150, border_width=1)
            pas_met_k.place(x=150, y=210)

            resp_k = customtkinter.CTkEntry(new_oq_window, font=ft, width=150, border_width=1)
            resp_k.place(x=150, y=240)

            vil_k = customtkinter.CTkComboBox(
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

            #vil_k = customtkinter.CTkEntry(new_oq_window, font=ft, width=250, border_width=1)
            vil_k.place(x=150, y=270)

            tum_k = customtkinter.CTkComboBox(
                master=new_oq_window,font=ft,width=150, border_width=1,

             values =  ["Marhamat",
            "Andijon(tuman)",
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
            "Andijon"])

            tum_k.place(x=150, y=300)

            mfy_k = customtkinter.CTkEntry(new_oq_window, font=ft, width=150, border_width=1)
            mfy_k.place(x=150, y=330)

            koch_k = customtkinter.CTkEntry(new_oq_window, font=ft, width=150, border_width=1)
            koch_k.place(x=150, y=360)

            jshshr_k = customtkinter.CTkEntry(new_oq_window, font=ft, width=150, border_width=1)
            jshshr_k.place(x=150, y=390)

            nogirg_k = customtkinter.CTkEntry(new_oq_window, font=ft, width=150, border_width=1)
            nogirg_k.place(x=150, y=420)

            status_k = customtkinter.CTkComboBox(
                master=new_oq_window,font=ft,width=150, border_width=1,

             values =  ["o'qimoqda",
            "davolanishda",
            "sportni tark etdi",
            "boshqa sabab bilan yo'q"])
            status_k.place(x=150, y=450)

            r1 = []
            for ifi in stat.fam_ism_mur_combo():
                r1.append(str(ifi[0])+" "+ifi[1]+" "+ifi[2])

            murabbiy = customtkinter.CTkComboBox(
                master=new_oq_window, font=ft, width=150, border_width=1,
                values=r1, state="readonly")
            murabbiy.place(x=150, y=480)



            def oq_qosh_baza():
                #print(murabbiy.get().split(" ")[0])
                date_str = tugyil_k.get()
                try:
                    datetime.datetime.strptime(date_str, "%d.%m.%Y")
                    tugyil_k.configure(border_color="green")
                except ValueError:
                    tugyil_k.configure(border_color="red")
                    mb.showerror("Xatolik", "Sanani kun.oy.yil ko'rinishida kiriting namuna: 01.01.2025 ")
                else:
                    entries = [ fam_k, ism_k, sharif_k, tugyil_k, tel1_k, tel2_k, pas_met_k, resp_k, vil_k, tum_k, mfy_k, koch_k, jshshr_k, nogirg_k, status_k]
                    all_filled = all(
                        (entry.get().strip() != '') if hasattr(entry, 'get') else False
                        for entry in entries
                    )
                    if all_filled:
                        id_murabbiy = murabbiy.get().split(" ")[0]
                        entries_get = (fam_k.get(), ism_k.get(), sharif_k.get(), tugyil_k.get(), tel1_k.get(), tel2_k.get(), pas_met_k.get(), resp_k.get(), vil_k.get(), tum_k.get(), mfy_k.get(),
                                   koch_k.get(), jshshr_k.get(), nogirg_k.get(), status_k.get(), id_murabbiy)
                        stat.oqchi_bazaga_qoshish(entries_get)
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
            button.place(x=20, y=530)

            def close_window():
                new_oq_window.destroy()

            button = customtkinter.CTkButton(new_oq_window, text="Bekor qilish", font=bt, width=60, fg_color="red", command=close_window)
            button.place(x=110, y=530)

            new_oq_window.grab_set()
            #new_oq_window.wait_window()