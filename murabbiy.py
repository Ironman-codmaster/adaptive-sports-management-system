from tobaseoz import *
from todox import *
from murabbiy_qoshish import Murabbiyqosh

import customtkinter
from tkinter import ttk
from tkinter import messagebox as mb # Xatoliklarda va ogohlantirishlarda ma'lumot chiqarish uchun
from PIL import Image, ImageTk, ImageGrab
from tkinter import Label, filedialog
import sys
import shutil

from datetime import date, datetime


class Murabbiy:

    def murabbiy(self):

        stat = Stat() # ma'lumotlar ombori klassi obektini yaratish
        ft = customtkinter.CTkFont("",size=14, weight="bold")

        self.murabbiy_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.murabbiy_frame.grid_columnconfigure(0, weight=1)
        # Comboboxga kiritgan ma'lumotni harfini boshqa sozlarda qatnashganligiga qarab saralab beradi
        def searchtv(event):
            value = event.widget.get()
            oqch = stat.fam_mur_combo()
            data = []
            for item in oqch:
                find_txt = item[0].lower()
                value_lower = value.lower()
                if find_txt.find(value_lower) >= 0:
                    data.append(item[0])
            murabbiy_combo['value'] = data

        # O'quvchi kiritilsa shunga qarab ma'lumotlar o'zgaradi
        def callbackFuncShtr(event):
            mur_fam = murabbiy_combo.get()
            r = stat.fam_mur_base(mur_fam)
            print_to_dashboard_mur(r)

        def print_to_dashboard_mur(r):
            # O'quvchi kodini chiqarish
            idn_mur.configure(text=r[0])
            ids = r[0]
            fam_mur.delete(0, "end");
            fam_mur.insert(0, r[1])
            ism_mur.delete(0, "end");
            ism_mur.insert(0, r[2])
            sharif_mur.delete(0, "end");
            sharif_mur.insert(0, r[3])
            tugyil_mur.delete(0, "end");
            tugyil_mur.insert(0, r[4])

            curr = date.today()
            try:
                yo=int(str(curr)[0:4]) - int(str(r[4])[-4:])
                if int(str(curr)[5:7]) < int(str(r[4][3:5])):
                    yo = yo - 1
            except Exception:
                yo = 0

            yoshi_mur.configure(text=str(yo))
            murabbiy_combo.set('') # Komboboxdagi ma'lumotlarni o'chiradi
            tel1_mur.delete(0, "end");
            tel1_mur.insert(0, r[5])
            tel2_mur.delete(0, "end");
            tel2_mur.insert(0, r[6])
            pasmet_mur.delete(0, "end");
            pasmet_mur.insert(0, r[7])
            resp_mur.delete(0, "end");
            resp_mur.insert(0, r[8])
            vil_mur.delete(0, "end");
            vil_mur.insert(0, r[9])
            tum_mur.delete(0, "end");
            tum_mur.insert(0, r[10])
            mfy_mur.delete(0, "end");
            mfy_mur.insert(0, r[11])
            kocha_mur.delete(0, "end");
            kocha_mur.insert(0, r[12])
            jshshr_mur.delete(0, "end");
            jshshr_mur.insert(0, r[13])
            nogirg_mur.delete(0, "end");
            nogirg_mur.insert(0, r[14])
            status_mur.delete(0, "end");
            status_mur.insert(0, r[15])

            murabbiylar_tree_delete()
            mur_to_tree(self)

            oquvchilar_tree_delete()
            muroq_to_tree()

            # Функция для безопасной загрузки ресурсов (работает и в .py, и в .exe)
            def resource_path(relative_path):
                try:
                    base_path = sys._MEIPASS  # путь при запуске .exe
                except AttributeError:
                    base_path = os.path.abspath(".")  # путь при запуске .py
                return os.path.join(base_path, relative_path)

            # murabbiyning fotosurati
            try:
                img = Image.open("murabbiy_photo/" + r[16])
            except Exception:
                img = Image.open(resource_path("test_images/ft.png"))

            img = img.resize((150, 200), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            panel = Label(self.murabbiy_frame, image=img)
            panel.image = img
            panel.place(x=320, y=5, width=150, height=200)

            # Murabbiy pasporti_uzb
            try:
                img = Image.open("murabbiy_pasport_uz/" + r[17])
            except Exception:
                img = Image.open(resource_path("test_images/kyoq.png"))

            img = img.resize((65, 65), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            panel = Label(self.murabbiy_frame, image=img, bg="green")
            panel.image = img
            panel.place(x=320, y=215, width=70, height=70)

            # Murabbiy pasporti_zagran
            try:
                img = Image.open("murabbiy_pasport_zagran/" + r[18])
            except Exception:
                img = Image.open(resource_path("test_images/qyoq.png"))

            img = img.resize((65, 65), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            panel = Label(self.murabbiy_frame, image=img, bg="red")
            panel.image = img
            panel.place(x=400, y=215, width=70, height=70)

            # -----------------Murabbiyning Mukofot1-------------------
            if r[19] == "":
                pas_uz = "psza.jpg"
            else:
                pas_uz = r[19]
            try:
                img = Image.open("mukofot1/" + pas_uz)
            except Exception:
                img = Image.open(resource_path("test_images/qyoq.png"))

            img = img.resize((65, 65), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            panel = Label(self.murabbiy_frame, image=img, bg="blue")
            panel.image = img
            panel.place(x=320, y=295, width=70, height=70)
            # ______________________________________________________

            # ----------------Murabbiyning Mukofot2-----------------
            if r[20] == "":
                pas_uz = "psza.jpg"
            else:
                pas_uz = r[20]
            try:
                img = Image.open("mukofot2/" + pas_uz)
            except Exception:
                img = Image.open(resource_path("test_images/qyoq.png"))

            img = img.resize((65, 65), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            panel = Label(self.murabbiy_frame, image=img, bg="blue")
            panel.image = img
            panel.place(x=400, y=295, width=70, height=70)
            # _____________________________________________________

            # ---------------Murabbiyning Mukofot3-----------------
            if r[21] == "":
                pas_uz = "psza.jpg"
            else:
                pas_uz = r[21]
            try:
                img = Image.open("mukofot3/" + pas_uz)
            except Exception:
                img = Image.open(resource_path("test_images/qyoq.png"))

            img = img.resize((65, 65), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            panel = Label(self.murabbiy_frame, image=img, bg="blue")
            panel.image = img
            panel.place(x=320, y=375, width=70, height=70)
            # _______________________________________________________________________

        # O'quvchini combo yozuvi
        oquvchi_top = customtkinter.CTkLabel(self.murabbiy_frame, text="Murabbiy: ", font=("",13,'bold'), anchor='w', width=200, height=30)
        oquvchi_top.place(y=5, x=20)

        # Sportsmenlarni Combo orqali kiritish

        murabbiy_combo = ttk.Combobox(self.murabbiy_frame, font=('',10, 'bold'), value=stat.fam_mur_combo())
        murabbiy_combo.set('')
        murabbiy_combo.bind('<KeyRelease>', searchtv)
        murabbiy_combo.bind("<<ComboboxSelected>>", callbackFuncShtr)
        murabbiy_combo.place(y=5, x=150, width=150, height=25)

        # EndCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCComboBox

        idn_mur_label = customtkinter.CTkLabel(self.murabbiy_frame, text="ID: ", font=ft)
        idn_mur_label.place(x=20, y=40)

        fam_mur_label = customtkinter.CTkLabel(self.murabbiy_frame, text="Familiyasi: ", font=ft)
        fam_mur_label.place(x=20, y=70)

        ism_mur_label = customtkinter.CTkLabel(self.murabbiy_frame, text="Ismi: ", font=ft)
        ism_mur_label.place(x=20, y=100)

        sharif_mur_label = customtkinter.CTkLabel(self.murabbiy_frame, text="Otasining ismi: ", font=ft)
        sharif_mur_label.place(x=20, y=130)

        tugyil_mur_label = customtkinter.CTkLabel(self.murabbiy_frame, text="Tug'ulgan sanasi: ", font=ft)
        tugyil_mur_label.place(x=20, y=160)

        yoshi_mur_label = customtkinter.CTkLabel(self.murabbiy_frame, text="Yoshi: ")
        yoshi_mur_label.place(x=240, y=160)

        tel1_mur_label = customtkinter.CTkLabel(self.murabbiy_frame, text="Telefon raqami: ", font=ft)
        tel1_mur_label.place(x=20, y=190)

        tel2_mur_label = customtkinter.CTkLabel(self.murabbiy_frame, text="Telefon raqami: ", font=ft)
        tel2_mur_label.place(x=20, y=220)

        pasmet_mur_label = customtkinter.CTkLabel(self.murabbiy_frame, text="Pasport/Metrika: ", font=ft)
        pasmet_mur_label.place(x=20, y=250)

        resp_mur_label = customtkinter.CTkLabel(self.murabbiy_frame, text="Respublika: ", font=ft)
        resp_mur_label.place(x=20, y=280)

        vil_mur_label = customtkinter.CTkLabel(self.murabbiy_frame, text="Viloyati: ", font=ft)
        vil_mur_label.place(x=20, y=310)

        tum_mur_label = customtkinter.CTkLabel(self.murabbiy_frame, text="Tumani:", font=ft)
        tum_mur_label.place(x=20, y=340)

        mfy_mur_label = customtkinter.CTkLabel(self.murabbiy_frame, text="MFY: ", font=ft)
        mfy_mur_label.place(x=20, y=370)

        kocha_mur_label = customtkinter.CTkLabel(self.murabbiy_frame, text="Ko'chasi uyi: ", font=ft)
        kocha_mur_label.place(x=20, y=400)

        jshshr_mur_label = customtkinter.CTkLabel(self.murabbiy_frame, text="JSHSHR: ", font=ft)
        jshshr_mur_label.place(x=20, y=430)

        nogrg_mur_label = customtkinter.CTkLabel(self.murabbiy_frame, text="Nogironlik guv: ", font=ft)
        nogrg_mur_label.place(x=20, y=460)

        status_mur_label = customtkinter.CTkLabel(self.murabbiy_frame, text="Status: ", font=ft)
        status_mur_label.place(x=20, y=490)

        # ---------------------------------------

        idn_mur = customtkinter.CTkLabel(self.murabbiy_frame, text="",font=ft, width=150, fg_color=("white","silwer"))
        idn_mur.place(x=150, y=40)

        fam_mur = customtkinter.CTkEntry(self.murabbiy_frame, font=ft, width=150, border_width=0)
        fam_mur.place(x=150, y=70)

        ism_mur = customtkinter.CTkEntry(self.murabbiy_frame, font=ft, width=150, border_width=0)
        ism_mur.place(x=150, y=100)

        sharif_mur = customtkinter.CTkEntry(self.murabbiy_frame, font=ft, width=150, border_width=0)
        sharif_mur.place(x=150, y=130)

        tugyil_mur = customtkinter.CTkEntry(self.murabbiy_frame, font=ft, width=85, border_width=0)
        tugyil_mur.place(x=150, y=160)

        yoshi_mur = customtkinter.CTkLabel(self.murabbiy_frame, text="", font=ft)
        yoshi_mur.place(x=280, y=160)

        tel1_mur = customtkinter.CTkEntry(self.murabbiy_frame, font=ft, width=150, border_width=0)
        tel1_mur.place(x=150, y=190)

        tel2_mur = customtkinter.CTkEntry(self.murabbiy_frame, font=ft, width=150, border_width=0)
        tel2_mur.place(x=150, y=220)

        pasmet_mur = customtkinter.CTkEntry(self.murabbiy_frame, font=ft, width=150, border_width=0)
        pasmet_mur.place(x=150, y=250)

        resp_mur = customtkinter.CTkEntry(self.murabbiy_frame, font=ft, width=150, border_width=0)
        resp_mur.place(x=150, y=280)

        vil_mur = customtkinter.CTkEntry(self.murabbiy_frame, font=ft, width=150, border_width=0)
        vil_mur.place(x=150, y=310)

        tum_mur = customtkinter.CTkEntry(self.murabbiy_frame, font=ft, width=150, border_width=0)
        tum_mur.place(x=150, y=340)

        mfy_mur = customtkinter.CTkEntry(self.murabbiy_frame, font=ft, width=150, border_width=0)
        mfy_mur.place(x=150, y=370)

        kocha_mur = customtkinter.CTkEntry(self.murabbiy_frame, font=ft, width=150, border_width=0)
        kocha_mur.place(x=150, y=400)

        jshshr_mur = customtkinter.CTkEntry(self.murabbiy_frame, font=ft, width=150, border_width=0)
        jshshr_mur.place(x=150, y=430)

        nogirg_mur = customtkinter.CTkEntry(self.murabbiy_frame, font=ft, width=150, border_width=0)
        nogirg_mur.place(x=150, y=460)

        status_mur = customtkinter.CTkEntry(self.murabbiy_frame, font=ft, width=150, border_width=0)
        status_mur.place(x=150, y=490)

        bt = ("", 13, "bold")


        # Murabbiy qoshish funktsiyasi
        def murabbiy_qoshish_event():
            Murabbiyqosh.murabbiy_qosh(self)

        # Yangi murabbiy qoshish tugmasi
        button = customtkinter.CTkButton(self.murabbiy_frame, text="Qoshish", font=bt, width=60, fg_color="green",command=murabbiy_qoshish_event)
        button.place(x=20, y=580)


        # ma'lumotlarni o'chirishga yonaltirish funktsiyasi
        def delete_murabbiy():
            ask = mb.askyesno("OGOHLANTIRISH!!!", "Ogohlantirish. Ushbu murabbiy ma'lumotlari o'chiriladi. O'chirilgandan so'ng qaytarib bo'lmaydi\n SIZ ROSTDAN HAM O'CHIRMOQCHIMISIZ!!!")
            if ask:
                id = idn_mur.cget("text")
                if id != '':
                    stat.murabbiyni_bazadan_ochirish(id)
                    mb.showinfo("Ma'lumot", '{}'.format("Murabbiy ma'lumotlari muvaffaqiyatli o'chirildi!!!"))
                    murabbiylar_tree_delete()
                    mur_to_tree(self)
                else:
                    mb.showinfo("Ma'lumot", '{}'.format("Murabbiyni tanlang va keyin o'chiring !!!"))

        # Murabbiyni o'chirish tugmasi
        button = customtkinter.CTkButton(self.murabbiy_frame, text="O'chirish", font=bt, width=60, fg_color="red", command=delete_murabbiy)
        button.place(x=90, y=580)

        # Tahrirlash funktsiyasi
        def murabbiy_tahrirlash():
            ask = mb.askyesno("Diqqat!!!", "Siz ushbu o'quvchi ma'lumotlarini o'zgartirmoqchimisiz???")
            if ask:
                #idn.cget()
                tah = (fam_mur.get(),ism_mur.get(),sharif_mur.get(),tugyil_mur.get(),tel1_mur.get(),tel2_mur.get(),pasmet_mur.get(),resp_mur.get(),vil_mur.get(),
                tum_mur.get(),mfy_mur.get(),kocha_mur.get(),jshshr_mur.get(),nogirg_mur.get(),status_mur.get())
                j = 0
                for i in tah:
                    if i == "":
                        j+=1
                if j == 0:
                    stat.murabbiyniozgartirish(idn_mur.cget("text"),tah)
                    ask1 = mb.showinfo("Diqqat!!!", f"Ma'lumotlar o'zgartirildi!!!")
                    murabbiylar_tree_delete()
                    mur_to_tree(self)
                else:
                    ask2 = mb.showinfo("Diqqat!!!", f"Ma'lumotlarni to'liq kiriting. Siz {j} ta bo'sh joy qoldirdingiz!!!")

        # Tahrirlash tugmasi
        button = customtkinter.CTkButton(self.murabbiy_frame, text="Tahrirlash", font=bt, width=60, command=murabbiy_tahrirlash)
        button.place(x=165, y=580)

        # Anketani fotosi bilan excel fayliga chiqarish
        def murabbiy_gotoexcel():
            if idn_mur.cget("text") !="":
                dat = (stat.fromidmurabbiy(idn_mur.cget("text")))
                ex = Docs.docs_excell(dat)
                if ex:
                    mb.showerror("Xatolik",ex)
            else:
                mb.showerror("Xatolik", "Murabbiyning ma'lumotlarini toping!!!")

        # Anketani Excelga chiqarib berish tugmasi
        button_exc = customtkinter.CTkButton(self.murabbiy_frame, text="Excel",image=self.icon_image_excell, width=35, height=35, fg_color="white", hover_color="silver",command=murabbiy_gotoexcel, anchor="center",compound="top")
        button_exc.place(x=250, y=580)

        # Anketani fotolari bilan word fayliga chiqarish
        def murabbiy_gotoword():
            if idn_mur.cget("text") !="":
                dat1 = (stat.fromidmurabbiy(idn_mur.cget("text")))
                ex = Docs.docs_word(dat1, 1)
                if ex:
                    mb.showerror("Xatolik",ex)
            else:
                mb.showerror("Xatolik", "Murabbiyning ma'lumotlarini toping!!!")


        button_word = customtkinter.CTkButton(self.murabbiy_frame, text="Word", image=self.icon_image_word, width=35,
                                             height=35, fg_color="white", hover_color="silver", command=murabbiy_gotoword, anchor="center",compound="top")
        button_word.place(x=300, y=580)

        # Anketani fotosini pechatga berish
        def murabbiy_gotoprint():
            # Получаем координаты точек формы x и y
            x = self.winfo_x()+150
            y = self.winfo_y()+35
            # Получаем высоту и ширину формы
            height = self.murabbiy_frame.winfo_height()-120
            width = self.murabbiy_frame.winfo_width()/2+15
            # Делаем снимок, сохраняем, печатаем
            image = ImageGrab.grab((x, y, x + width, y + height))
            image.save("screen.bmp", "BMP")
            os.startfile("screen.bmp", "print")

        # Anketa oynasini fotoga chiqarib beruvchi tugma
        button_print = customtkinter.CTkButton(self.murabbiy_frame, text="", image=self.icon_image_printer, width=35,
                                             height=35, fg_color="white", hover_color="silver", command=murabbiy_gotoprint)
        button_print.place(x=350, y=580)

        # Foto qoshish funktsiyasi
        def savefoto_murabbiy(path):
            if idn_mur.cget('text'):
                destination_folder = path
                os.makedirs(destination_folder, exist_ok=True)
                file_path = filedialog.askopenfilename(
                    title="Fotosuratni tanlang",
                    filetypes=[("Faqat fotosuratlar turi", "*.png *.jpg *.jpeg *.bmp")]
                )

                if file_path:
                    fn = os.path.basename(file_path)
                    filename = "m" + str(idn_mur.cget('text'))+fn[fn.rfind("."):]
                    destination_path = os.path.join(destination_folder, filename)
                    shutil.copy(file_path, destination_path)
                    # if path == "murabbiy_photo":
                    #     base_table_name = "murabbiy_photo"
                    # elif path == "murabbiy_pasport_uz":
                    #     base_table_name = "pasport_uz"
                    # elif path == "murabbiy_pasport_zagran":
                    #     base_table_name = "pasport_zagran"
                    tobd = (path, filename, idn_mur.cget('text'))
                    stat.murabbiy_bazaga_foto_qoshish(tobd)
                    mb.showinfo("Xabar",f"Fotosurat: {destination_path} papkasiga ko'chirildi")
                    rr = stat.fromidmurabbiy(idn_mur.cget('text'))
                    print_to_dashboard_mur(rr)
                else:
                    mb.showinfo("Diqqat","Fayl tanlanmadi")
            else:
                mb.showinfo("Diqqat", "O'quvchi tanlanmadi. Yangi o'quvchi kiriting yoki tanlang")


        # Fotosurat qoshish yoki o'zgartirish tugmasi
        button_foto_save = customtkinter.CTkButton(self.murabbiy_frame, text="", image=self.icon_image_icfoto, width=35,
                                             height=35, fg_color="white", hover_color="silver", command=lambda:savefoto_murabbiy("murabbiy_photo"))
        button_foto_save.place(x=400, y=580)


        # Pasport_skaneri qoshish yoki o'zgartirish tugmasi
        button_pasport_save = customtkinter.CTkButton(self.murabbiy_frame, text="", image=self.icon_image_greenpasport, width=35,
                                                   height=35, fg_color="white", hover_color="silver", command=lambda:savefoto_murabbiy("murabbiy_pasport_uz"))
        button_pasport_save.place(x=450, y=580)

        # Zagran Pasport_skaneri qoshish yoki o'zgartirish tugmasi
        button_zagran_pasport_save = customtkinter.CTkButton(self.murabbiy_frame, text="", image=self.icon_image_redpasport,
                                                      width=35,
                                                      height=35, fg_color="white", hover_color="silver",
                                                      command=lambda:savefoto_murabbiy("murabbiy_pasport_zagran"))
        button_zagran_pasport_save.place(x=500, y=580)

        # Mukofot1 qoshish yoki o'zgartirish tugmasi
        button_mukofot1_save = customtkinter.CTkButton(self.murabbiy_frame, text="", image=self.icon_image_m1,
                                                       width=35,
                                                       height=35, fg_color="white", hover_color="silver",
                                                       command=lambda: savefoto_murabbiy("mukofot1"))
        button_mukofot1_save.place(x=550, y=580)

        # Mukofot2 qoshish yoki o'zgartirish tugmasi
        button_mukofot2_save = customtkinter.CTkButton(self.murabbiy_frame, text="", image=self.icon_image_m2,
                                                       width=35,
                                                       height=35, fg_color="white", hover_color="silver",
                                                       command=lambda: savefoto_murabbiy("mukofot2"))
        button_mukofot2_save.place(x=600, y=580)

        # Mukofot3 qoshish yoki o'zgartirish tugmasi
        button_mukofot3_save = customtkinter.CTkButton(self.murabbiy_frame, text="", image=self.icon_image_m3,
                                                       width=35,
                                                       height=35, fg_color="white", hover_color="silver",
                                                       command=lambda: savefoto_murabbiy("mukofot3"))
        button_mukofot3_save.place(x=650, y=580)


       # Treevew Murabbiylar ko'rsatib turuvchi oyna

        self.tree_murabbiy_frame = customtkinter.CTkFrame(self.murabbiy_frame, corner_radius=0, fg_color="transparent", width=430, height=277, border_width=1, border_color=("blue","red"))
        self.tree_murabbiy_frame.place(x=490, y=5)

        # Scrollar
        scrollbarx = ttk.Scrollbar(self.tree_murabbiy_frame, orient="horizontal")
        scrollbary = ttk.Scrollbar(self.tree_murabbiy_frame, orient="vertical")

        # Trevewning ko'rinishi
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 10),
                        rowheght=25)  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 12, 'bold'))  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        # Treevew
        mur_tree = ttk.Treeview(self.tree_murabbiy_frame, style="mystyle.Treeview")
        mur_tree.place(x=5, y=5, width=400, height=250) #height=680
        mur_tree.configure(yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        mur_tree.configure(selectmode="extended")
        # scrollbar larning korinishi va joylashgan joyi
        scrollbary.configure(command=mur_tree.yview)
        scrollbarx.configure(command=mur_tree.xview)

        scrollbary.place(x=405, y=5, width=15, height=250)
        scrollbarx.place(x=5, y=255, width=400, height=15)

        mur_tree.configure(
            columns=(
                "ID",
                "Familiyasi",
                "Ismi",
                "Sharifi",
                "Tug'ulgan yili"
            )
        )

        # Headings
        mur_tree.heading("#0", text="N")
        mur_tree.heading("ID", text="ID")
        mur_tree.heading("Familiyasi", text="Familiyasi")
        mur_tree.heading("Ismi", text="Ismi")
        mur_tree.heading("Sharifi", text="Sharifi")
        mur_tree.heading("Tug'ulgan yili", text="Tug'ulgan yili")
        # Colums
        mur_tree.column("#0", minwidth=0, width=5)  # Tartib raqami
        mur_tree.column("#1", minwidth=0, width=7)  # ID
        mur_tree.column("#2", minwidth=0, width=50)  # Familiyasi
        mur_tree.column("#3", minwidth=0, width=50)  # Ismi
        mur_tree.column("#4", minwidth=0, width=50)  # Sharifi
        mur_tree.column("#5", minwidth=0, width=50)  # Tug'ulgan yili
        #Treewevga ma'lumotlarni kirituvchi funktsiya

        # Murabbiylarning treesini o'chiradi
        def murabbiylar_tree_delete():
            for i in mur_tree.get_children():
                mur_tree.delete(i)

        def mur_to_tree(self):
            """ Murabbiylarni trewev oynasi"""
            murabbiylar_tree_delete()
            tr = 1
            mur_tree.tag_configure('oddrow', background="white")
            mur_tree.tag_configure('evenrow', background="#ecf8fe")
            result = stat.allmurabbiy()
            for record in result:
                if tr % 2 == 0:
                    mur_tree.insert(parent='', index='end', text=str(tr), values=(
                    record[0], record[1], record[2], record[3], record[4]),
                                   tags=('evenrow',))
                else:
                    mur_tree.insert(parent='', index='end', text=str(tr), values=(
                    record[0], record[1], record[2], record[3], record[4]),
                                   tags=('oddrow',))
                tr += 1

        mur_to_tree(self)

        # Treewevni malumottini sichqonchani ikki marotaba bossa ma'lumot ko'rinadi
        def OnDoubleClick_mur_tree(event):
            selected = mur_tree.selection()
            if selected:
                item = mur_tree.item(selected[0])
                values = item["values"]
                try:
                    r = values[0]
                except Exception:
                    return mb.showinfo("Diqqat!!!", "Malumot yo'q!!!")
                else:
                    rr = stat.from_mur_id(r)
                    print_to_dashboard_mur(rr)

        mur_tree.bind("<Double-1>", OnDoubleClick_mur_tree)

        # Treevew Murabbiylarning o'quvchilarini ko'rsatib turuvchi oyna

        self.tree_murabbiy_oqu_frame = customtkinter.CTkFrame(self.murabbiy_frame, corner_radius=0, fg_color="transparent",
                                                          width=430, height=227, border_width=1,
                                                          border_color=("blue", "red"))
        self.tree_murabbiy_oqu_frame.place(x=490, y=290)

        # Scrollar
        scrollbarxm2 = ttk.Scrollbar(self.tree_murabbiy_oqu_frame, orient="horizontal")
        scrollbarym2 = ttk.Scrollbar(self.tree_murabbiy_oqu_frame, orient="vertical")

        # Treevew
        muroq_tree = ttk.Treeview(self.tree_murabbiy_oqu_frame, style="mystyle.Treeview")
        muroq_tree.place(x=5, y=5, width=400, height=200)  # height=680
        muroq_tree.configure(yscrollcommand=scrollbarym2.set, xscrollcommand=scrollbarxm2.set)
        muroq_tree.configure(selectmode="extended")
        # scrollbar larning korinishi va joylashgan joyi
        scrollbarym2.configure(command=muroq_tree.yview)
        scrollbarxm2.configure(command=muroq_tree.xview)

        scrollbarym2.place(x=405, y=5, width=15, height=200)
        scrollbarxm2.place(x=5, y=205, width=400, height=15)

        muroq_tree.configure(
            columns=(
                "ID",
                "Familiyasi",
                "Ismi",
                "Sharifi",
                "Tug'ulgan yili"
            )
        )

        # Headings
        muroq_tree.heading("#0", text="N")
        muroq_tree.heading("ID", text="ID")
        muroq_tree.heading("Familiyasi", text="Familiyasi")
        muroq_tree.heading("Ismi", text="Ismi")
        muroq_tree.heading("Sharifi", text="Sharifi")
        muroq_tree.heading("Tug'ulgan yili", text="Tug'ulgan yili")
        # Colums
        muroq_tree.column("#0", minwidth=0, width=5)  # Tartib raqami
        muroq_tree.column("#1", minwidth=0, width=7)  # ID
        muroq_tree.column("#2", minwidth=0, width=50)  # Familiyasi
        muroq_tree.column("#3", minwidth=0, width=50)  # Ismi
        muroq_tree.column("#4", minwidth=0, width=50)  # Sharifi
        muroq_tree.column("#5", minwidth=0, width=50)  # Tug'ulgan yili

        # Oquvchining oqigan gruhlar treesini o'chiradi
        def oquvchilar_tree_delete():
            for i in muroq_tree.get_children():
                muroq_tree.delete(i)

        # Treewevga ma'lumotlarni kirituvchi funktsiya
        def muroq_to_tree():
            """ Murabbiylarning shogirdlari trewev oynasi"""
            muroq_tree.tag_configure('oddrow', background="white")
            muroq_tree.tag_configure('evenrow', background="#ecf8fe")
            result = stat.oquvchi_mur_id(idn_mur.cget("text"))
            tr = 1
            for record in result:
                if tr % 2 == 0:
                    muroq_tree.insert(parent='', index='end', text=str(tr), values=(
                        record[0], record[1], record[2], record[3], record[4]),
                                    tags=('evenrow',))
                else:
                    muroq_tree.insert(parent='', index='end', text=str(tr), values=(
                        record[0], record[1], record[2], record[3], record[4]),
                                    tags=('oddrow',))
                tr += 1



        # Barcha murabbiylarni Excelga chiqarib berish funktsiyasi
        def all_murabbiy_to_excel():
            dat = stat.allmurabbiy()
            ex = Docs.allpupilexcel(dat, 1)
            if ex:
                mb.showerror("Xatolik", ex)


        # O'quvchini grafigini chiqarib beruvchi knopka
        button_murabbiylar = customtkinter.CTkButton(self.murabbiy_frame, text="Murabbiy", image=self.icon_image_excell, width=35,
                                                height=35, fg_color="white", hover_color="silver", command=all_murabbiy_to_excel, anchor="center",compound="top")
        button_murabbiylar.place(x=700, y=580)

        # Murabbiyning shogirdlarini Excelga chiqarib berish funktsiyasi
        def all_murabbiy_sogird_to_excel():
            if idn_mur.cget('text'):
                dat = stat.oquvchi_mur_id(idn_mur.cget('text'))
                if dat == []:
                    mb.showinfo("Diqqat!", "Bu murabbiyning shogirdlari mavjud emas !!!")
                else:
                    ex = Docs.allpupilexcel(dat, 1)
                    if ex:
                        mb.showerror("Xatolik", ex)
            else:
                mb.showerror("Iltimos","Murabbiyni tanlang!")

        # Shogirdlarning grafigini chiqarib beruvchi knopka
        button_shogirdlar = customtkinter.CTkButton(self.murabbiy_frame, text="Shogird",
                                                    image=self.icon_image_excell, width=35,
                                                    height=35, fg_color="white", hover_color="silver",
                                                    command=all_murabbiy_sogird_to_excel, anchor="center",compound="top")
        button_shogirdlar.place(x=770, y=580)

        # Papkaga o'quvchining barcha ma'lumotlarini chiqarish
        def gotodir():
            if idn_mur.cget("text") != "":
                dat = (stat.fromidmurabbiy(idn_mur.cget("text")))
                ex = Docs.todirectory(dat, 1)
                if ex:
                    mb.showerror("Xatolik", ex)
            else:
                mb.showerror("Xatolik", "Murabbiyning ma'lumotlarini toping!!!")

        button_word = customtkinter.CTkButton(self.murabbiy_frame, text="", image=self.icon_image_dir, width=35,
                                              height=35, fg_color="white", hover_color="silver", command=gotodir)
        button_word.place(x=830, y=580)








