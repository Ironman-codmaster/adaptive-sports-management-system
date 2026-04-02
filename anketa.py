from tobaseoz import *
from todox import *
from oquvchi_qoshish import Oquvchi
from korsatkich_qoshish import Korsatkich
import customtkinter
from tkinter import ttk
from tkinter import messagebox as mb # Xatoliklarda va ogohlantirishlarda ma'lumot chiqarish uchun
from PIL import Image, ImageTk, ImageGrab
from tkinter import Label, filedialog
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import sys
import shutil

from datetime import date, datetime


class Anketa:

    def anketa(self):

        stat = Stat()

        ft = customtkinter.CTkFont("",size=14, weight="bold")

        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        # Yangi ma'lumot qoshilgandan keyin asosiy oyna ma'lumotlarini kiritish

        def clear_tree_and_data():
            for row in my_tree.get_children():
                my_tree.delete(row)

        def clear_entries():
            oquvchi_combo.set("")  # Komboboxdagi ma'lumotlarni o'chiradi
            idn.configure(text="")
            fam.delete(0, "end");
            ism.delete(0, "end");
            sharif.delete(0, "end");
            tugyil.delete(0, "end");
            yoshi.configure(text="")
            tel1.delete(0, "end");
            tel2.delete(0, "end");
            pasmet.delete(0, "end");
            resp.delete(0, "end");
            vil.delete(0, "end");
            tum.delete(0, "end");
            mfy.delete(0, "end");
            kocha.delete(0, "end");
            jshshr.delete(0, "end");
            nogirg.delete(0, "end");
            status.delete(0, "end");
            murabbiy.set("");
            qabul(self)


        # Comboboxga kiritgan ma'lumotni harfini boshqa sozlarda qatnashganligiga qarab saralab beradi
        def searchtv(event):
            value = event.widget.get()
            oqch = stat.famcombo()
            data = []
            for item in oqch:
                find_txt = item[0].lower()
                value_lower = value.lower()
                if find_txt.find(value_lower) >= 0:
                    data.append(item[0])
            oquvchi_combo['value'] = data

        # O'quvchi kiritilsa shunga qarab ma'lumotlar o'zgaradi
        def callbackFuncShtr(event):
            oqch_fam = oquvchi_combo.get()
            r = stat.fambase(oqch_fam)
            print_to_dashboard(r)

        def print_to_dashboard(r):
            # O'quvchi kodini chiqarish
            try:
                idn.configure(text=r[0])
            except Exception:
                pass
                #return mb.showinfo("Diqqat!!!", "Malumot yo'q!!!")

            ids = r[0]
            fam.delete(0, "end");
            fam.insert(0, r[1])
            ism.delete(0, "end");
            ism.insert(0, r[2])
            sharif.delete(0, "end");
            sharif.insert(0, r[3])
            tugyil.delete(0, "end");
            tugyil.insert(0, r[4])

            curr = date.today()
            try:
                yo=int(str(curr)[0:4]) - int(str(r[4])[-4:])
                if int(str(curr)[5:7]) < int(str(r[4][3:5])):
                    yo = yo - 1
            except Exception:
                yo = 0

            yoshi.configure(text=str(yo))
            oquvchi_combo.set('') # Komboboxdagi ma'lumotlarni o'chiradi
            tel1.delete(0, "end");
            tel1.insert(0, r[5])
            tel2.delete(0, "end");
            tel2.insert(0, r[6])
            pasmet.delete(0, "end");
            pasmet.insert(0, r[7])
            resp.delete(0, "end");
            resp.insert(0, r[8])
            vil.delete(0, "end");
            vil.insert(0, r[9])
            tum.delete(0, "end");
            tum.insert(0, r[10])
            mfy.delete(0, "end");
            mfy.insert(0, r[11])
            kocha.delete(0, "end");
            kocha.insert(0, r[12])
            jshshr.delete(0, "end");
            jshshr.insert(0, r[13])
            nogirg.delete(0, "end");
            nogirg.insert(0, r[14])
            status.delete(0, "end");
            status.insert(0, r[15])
            # Murabbiyni id bo'yicha topish
            idmur = stat.fromidmurabbiy(int(r[19]))
            zn = str(idmur[0])+" "+idmur[1]+" "+idmur[2]
            murabbiy.set(zn)

            # Функция для безопасной загрузки ресурсов (работает и в .py, и в .exe)
            def resource_path(relative_path):
                try:
                    base_path = sys._MEIPASS  # путь при запуске .exe
                except AttributeError:
                    base_path = os.path.abspath(".")  # путь при запуске .py
                return os.path.join(base_path, relative_path)

            try:
                # oquvchining fotosurati
                if r[16] == "":
                    ph = "ft.png"
                else:
                    ph = r[16]
                try:
                    img = Image.open("fotopath/" + ph)
                except Exception:
                    img = Image.open(resource_path("test_images/ft.png"))

                img = img.resize((150, 200), Image.LANCZOS)
                img = ImageTk.PhotoImage(img)
                panel = Label(self.home_frame, image=img)
                panel.image = img
                panel.place(x=320, y=5, width=150, height=200)
            except Exception:
                pass

            # oquvchining pasporti_uzb
            if r[17] == "":
                pas_uz = "psuz.jpg"
            else:
                pas_uz  = r[17]
            try:
                img = Image.open("pasport_uz/" + pas_uz)
            except Exception:
                img = Image.open(resource_path("test_images/kyoq.png"))

            img = img.resize((65, 65), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            panel = Label(self.home_frame, image=img, bg="green")
            panel.image = img
            panel.place(x=320, y=215, width=70, height=70)

            # oquvchining pasporti_zagran
            if r[18] == "":
                pas_uz = "psza.jpg"
            else:
                pas_uz = r[18]
            try:
                img = Image.open("pasport_zagran/" + pas_uz)
            except Exception:
                img = Image.open(resource_path("test_images/qyoq.png"))

            img = img.resize((65, 65), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            panel = Label(self.home_frame, image=img, bg="red")
            panel.image = img
            panel.place(x=400, y=215, width=70, height=70)

            # -----------------O'quvchining Mukofot1-------------------
            if r[20] == "":
                pas_uz = "psza.jpg"
            else:
                pas_uz = r[20]
            try:
                img = Image.open("mukofot1/" + pas_uz)
            except Exception:
                img = Image.open(resource_path("test_images/qyoq.png"))

            img = img.resize((65, 65), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            panel = Label(self.home_frame, image=img, bg="blue")
            panel.image = img
            panel.place(x=320, y=295, width=70, height=70)
            #______________________________________________________

            # ----------------O'quvchining Mukofot2-----------------
            if r[21] == "":
                pas_uz = "psza.jpg"
            else:
                pas_uz = r[21]
            try:
                img = Image.open("mukofot2/" + pas_uz)
            except Exception:
                img = Image.open(resource_path("test_images/qyoq.png"))

            img = img.resize((65, 65), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            panel = Label(self.home_frame, image=img, bg="blue")
            panel.image = img
            panel.place(x=400, y=295, width=70, height=70)
            # _____________________________________________________

            # ---------------O'quvchining Mukofot3-----------------
            if r[22] == "":
                pas_uz = "psza.jpg"
            else:
                pas_uz = r[22]
            try:
                img = Image.open("mukofot3/" + pas_uz)
            except Exception:
                img = Image.open(resource_path("test_images/qyoq.png"))

            img = img.resize((65, 65), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            panel = Label(self.home_frame, image=img, bg="blue")
            panel.image = img
            panel.place(x=320, y=375, width=70, height=70)
            # _______________________________________________________________________

        # O'quvchini combo yozuvi
        oquvchi_top = customtkinter.CTkLabel(self.home_frame, text="O'quvchini qidirish: ", font=("",13,'bold'), anchor='w', width=200, height=30)
        oquvchi_top.place(y=5, x=20)
        # Sportsmenlarni Combo orqali kiritish
        oquvchi_combo = ttk.Combobox(self.home_frame, font=('',10, 'bold'), value=stat.famcombo())
        oquvchi_combo.set('')
        oquvchi_combo.bind('<KeyRelease>', searchtv)
        oquvchi_combo.bind("<<ComboboxSelected>>", callbackFuncShtr)
        oquvchi_combo.place(y=5, x=150, width=150, height=25)

        # EndCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCComboBox

        idn_label = customtkinter.CTkLabel(self.home_frame, text="ID: ", font=ft)
        idn_label.place(x=20, y=40)

        fam_label = customtkinter.CTkLabel(self.home_frame, text="Familiyasi: ", font=ft)
        fam_label.place(x=20, y=70)

        ism_label = customtkinter.CTkLabel(self.home_frame, text="Ismi: ", font=ft)
        ism_label.place(x=20, y=100)

        sharif_label = customtkinter.CTkLabel(self.home_frame, text="Otasining ismi: ", font=ft)
        sharif_label.place(x=20, y=130)

        tugyil_label = customtkinter.CTkLabel(self.home_frame, text="Tug'ulgan sanasi: ", font=ft)
        tugyil_label.place(x=20, y=160)

        yoshi_label = customtkinter.CTkLabel(self.home_frame, text="Yosh:", font=("",12))
        yoshi_label.place(x=240, y=160)

        tel1_label = customtkinter.CTkLabel(self.home_frame, text="Telefon raqami: ", font=ft)
        tel1_label.place(x=20, y=190)

        tel2_label = customtkinter.CTkLabel(self.home_frame, text="Telefon raqami: ", font=ft)
        tel2_label.place(x=20, y=220)

        pasmet_label = customtkinter.CTkLabel(self.home_frame, text="Pasport/Metrika: ", font=ft)
        pasmet_label.place(x=20, y=250)

        resp_label = customtkinter.CTkLabel(self.home_frame, text="Respublika: ", font=ft)
        resp_label.place(x=20, y=280)

        vil_label = customtkinter.CTkLabel(self.home_frame, text="Viloyati: ", font=ft)
        vil_label.place(x=20, y=310)

        tum_label = customtkinter.CTkLabel(self.home_frame, text="Tumani:", font=ft)
        tum_label.place(x=20, y=340)

        mfy_label = customtkinter.CTkLabel(self.home_frame, text="MFY: ", font=ft)
        mfy_label.place(x=20, y=370)

        kocha_label = customtkinter.CTkLabel(self.home_frame, text="Ko'chasi uyi: ", font=ft)
        kocha_label.place(x=20, y=400)

        jshshr_label = customtkinter.CTkLabel(self.home_frame, text="JSHSHR: ", font=ft)
        jshshr_label.place(x=20, y=430)

        nogrg_label = customtkinter.CTkLabel(self.home_frame, text="Nogironlik guv: ", font=ft)
        nogrg_label.place(x=20, y=460)

        status_label = customtkinter.CTkLabel(self.home_frame, text="Status: ", font=ft)
        status_label.place(x=20, y=490)

        murabbiy_label = customtkinter.CTkLabel(self.home_frame, text="Murabbiy: ", font=ft)
        murabbiy_label.place(x=20, y=520)

        # ---------------------------------------

        idn = customtkinter.CTkLabel(self.home_frame, text="",font=ft, width=150, fg_color=("white","silwer"))
        idn.place(x=150, y=40)

        fam = customtkinter.CTkEntry(self.home_frame, font=ft, width=150, border_width=0)
        fam.place(x=150, y=70)

        ism = customtkinter.CTkEntry(self.home_frame, font=ft, width=150, border_width=0)
        ism.place(x=150, y=100)

        sharif = customtkinter.CTkEntry(self.home_frame, font=ft, width=150, border_width=0)
        sharif.place(x=150, y=130)

        tugyil = customtkinter.CTkEntry(self.home_frame, font=ft, width=85, border_width=0)
        tugyil.place(x=150, y=160)

        yoshi = customtkinter.CTkLabel(self.home_frame, text="", font=ft)
        yoshi.place(x=280, y=160)

        tel1 = customtkinter.CTkEntry(self.home_frame, font=ft, width=150, border_width=0)
        tel1.place(x=150, y=190)

        tel2 = customtkinter.CTkEntry(self.home_frame, font=ft, width=150, border_width=0)
        tel2.place(x=150, y=220)

        pasmet = customtkinter.CTkEntry(self.home_frame, font=ft, width=150, border_width=0)
        pasmet.place(x=150, y=250)

        resp = customtkinter.CTkEntry(self.home_frame, font=ft, width=150, border_width=0)
        resp.place(x=150, y=280)

        vil = customtkinter.CTkEntry(self.home_frame, font=ft, width=150, border_width=0)
        vil.place(x=150, y=310)

        tum = customtkinter.CTkEntry(self.home_frame, font=ft, width=150, border_width=0)
        tum.place(x=150, y=340)

        mfy = customtkinter.CTkEntry(self.home_frame, font=ft, width=150, border_width=0)
        mfy.place(x=150, y=370)

        kocha = customtkinter.CTkEntry(self.home_frame, font=ft, width=150, border_width=0)
        kocha.place(x=150, y=400)

        jshshr = customtkinter.CTkEntry(self.home_frame, font=ft, width=150, border_width=0)
        jshshr.place(x=150, y=430)

        nogirg = customtkinter.CTkEntry(self.home_frame, font=ft, width=150, border_width=0)
        nogirg.place(x=150, y=460)

        status = customtkinter.CTkEntry(self.home_frame, font=ft, width=150, border_width=0)
        status.place(x=150, y=490)

        r1 = []
        for ifi in stat.fam_ism_mur_combo():
            r1.append(str(ifi[0]) + " " + ifi[1] + " " + ifi[2])

        murabbiy = customtkinter.CTkComboBox(
            self.home_frame, font=ft, width=150, border_width=0,
            values=r1, state="readonly")

        murabbiy.place(x=150, y=520)

        bt = ("", 13, "bold")

        # O'quvchi qoshish funktsiyasi
        def oquvchi_qoshish_event():
            if stat.allmurabbiy() != []:
                Oquvchi.oquvchi_qosh(self)
            else:
                ask2 = mb.showinfo("Diqqat!!!", "Murabbiy kiriting!!!")


        # Yangi o'quvchi qoshish tugmasi
        button = customtkinter.CTkButton(self.home_frame, text="Qoshish", font=bt, width=60, fg_color="green",command=oquvchi_qoshish_event)
        button.place(x=20, y=580)


        # ma'lumotlarni o'chirishga yonaltirish funktsiyasi
        def delete_oquvchi():
            ask = mb.askyesno("OGOHLANTIRISH!!!", "Ogohlantirish. Ushbu o'quvchi ma'lumotlari o'chiriladi. O'chirilgandan so'ng qaytarib bo'lmaydi\n SIZ ROSTDAN HAM O'CHIRMOQCHIMISIZ!!!")
            if ask:
                id = idn.cget("text")
                if id != '':
                    stat.oqchi_bazadan_ochirish(id)
                    mb.showinfo("Ma'lumot", '{}'.format("O'quvchi ma'lumotlar omboridan muvaffaqiyatli o'chirildi!!!"))
                    clear_tree_and_data()
                    clear_entries()
                    qabul(self)
                else:
                    mb.showinfo("Ma'lumot", '{}'.format("O'quvchini tanlang va keyin o'chiring !!!"))

        # O'chirish tugmasi
        button = customtkinter.CTkButton(self.home_frame, text="O'chirish", font=bt, width=60, fg_color="red", command=delete_oquvchi)
        button.place(x=90, y=580)

        # Tahrirlash funktsiyasi
        def tahrirlash():
            ask = mb.askyesno("Diqqat!!!", "Siz ushbu o'quvchi ma'lumotlarini o'zgartirmoqchimisiz???")
            if ask:
                id_murabbiy = murabbiy.get().split(" ")[0]
                tah = (fam.get(),ism.get(),sharif.get(),tugyil.get(),tel1.get(),tel2.get(),pasmet.get(),resp.get(),vil.get(),
                tum.get(),mfy.get(),kocha.get(),jshshr.get(),nogirg.get(),status.get(),id_murabbiy)
                j = 0
                for i in tah:
                    if i == "":
                        j+=1
                if j == 0:
                    stat.ozgartirish(idn.cget("text"),tah)
                    ask1 = mb.showinfo("Diqqat!!!", f"Ma'lumotlar O'zgartirildi!!!")
                    clear_tree_and_data()
                    qabul(self)
                else:
                    ask2 = mb.showinfo("Diqqat!!!", f"Ma'lumotlarni to'liq kiriting. Siz {j} ta bo'sh joy qoldirdingiz!!!")

        # Tahrirlash tugmasi
        button = customtkinter.CTkButton(self.home_frame, text="Tahrirlash", font=bt, width=60, command=tahrirlash)
        button.place(x=165, y=580)

        # Anketani fotosi bilan excel fayliga chiqarish
        def gotoexcel():
            if idn.cget("text") !="":
                dat = (stat.fromid(idn.cget("text")))
                ex = Docs.docs_excell(dat)
                if ex:
                    mb.showerror("Xatolik",ex)
            else:
                mb.showerror("Xatolik", "O'quvchining ma'lumotlarini toping!!!")

        # Anketani Excelga chiqarib berish tugmasi
        button_exc = customtkinter.CTkButton(self.home_frame, text="Excel",image=self.icon_image_excell, width=35, height=35, fg_color="white", hover_color="silver",command=gotoexcel , anchor="center",compound="top")
        button_exc.place(x=250, y=580)

        # Anketani fotolari bilan word fayliga chiqarish
        def gotoword():
            if idn.cget("text") !="":
                dat = (stat.fromid(idn.cget("text")))
                ex = Docs.docs_word(dat, 0)
                if ex:
                    mb.showerror("Xatolik",ex)
            else:
                mb.showerror("Xatolik", "O'quvchining ma'lumotlarini toping!!!")


        button_word = customtkinter.CTkButton(self.home_frame, text="Word", image=self.icon_image_word, width=35,
                                             height=35, fg_color="white", hover_color="silver", command=gotoword, anchor="center",compound="top")
        button_word.place(x=300, y=580)

        # Anketani fotosini pechatga berish
        def gotoprint():
            # Получаем координаты точек формы x и y
            x = self.winfo_x()+150
            y = self.winfo_y()+35
            # Получаем высоту и ширину формы
            height = self.home_frame.winfo_height()-120
            width = self.home_frame.winfo_width()/2+15
            # Делаем снимок, сохраняем, печатаем
            image = ImageGrab.grab((x, y, x + width, y + height))
            image.save("screen.bmp", "BMP")
            os.startfile("screen.bmp", "print")

        # Anketa oynasini fotoga chiqarib beruvchi tugma
        button_print = customtkinter.CTkButton(self.home_frame, text="", image=self.icon_image_printer, width=35,
                                             height=35, fg_color="white", hover_color="silver", command=gotoprint)
        button_print.place(x=350, y=580)

        # Foto qoshish funktsiyasi
        def savefoto(path):
            if idn.cget('text'):
                destination_folder = path
                os.makedirs(destination_folder, exist_ok=True)
                file_path = filedialog.askopenfilename(
                    title="Fotosuratni tanlang",
                    filetypes=[("Faqat fotosuratlar turi", "*.png *.jpg *.jpeg *.bmp")]
                )

                if file_path:
                    fn = os.path.basename(file_path)
                    filename = "o"+str(idn.cget('text'))+fn[fn.rfind("."):]
                    destination_path = os.path.join(destination_folder, filename)
                    shutil.copy(file_path, destination_path)
                    # if path == "photo":
                    #     base_table_name = "fotopath"
                    # elif path == "pasport_uz":
                    #     base_table_name = "pasport_uz"
                    # elif path == "pasport_zagran":
                    #     base_table_name = "pasport_zagran"
                    tobd = (path,filename, idn.cget('text'))
                    stat.bazaga_foto_qoshish(tobd)
                    mb.showinfo("Xabar",f"Fotosurat: {destination_path} papkasiga ko'chirildi")
                    rr = stat.fromid(idn.cget('text'))
                    print_to_dashboard(rr)
                else:
                    mb.showinfo("Diqqat","Fayl tanlanmadi")
            else:
                mb.showinfo("Diqqat", "O'quvchi tanlanmadi. Yangi o'quvchi kiriting yoki tanlang")


        # Fotosurat qoshish yoki o'zgartirish tugmasi
        button_foto_save = customtkinter.CTkButton(self.home_frame, text="", image=self.icon_image_icfoto, width=35,
                                             height=35, fg_color="white", hover_color="silver", command=lambda:savefoto("fotopath"))
        button_foto_save.place(x=400, y=580)
        #lambda: my_function(var1, var2)

        # Pasport_skaneri qoshish yoki o'zgartirish tugmasi
        button_pasport_save = customtkinter.CTkButton(self.home_frame, text="", image=self.icon_image_greenpasport, width=20,
                                                   height=35, fg_color="white", hover_color="silver", command=lambda:savefoto("pasport_uz"))
        button_pasport_save.place(x=450, y=580)

        # Zagran Pasport_skaneri qoshish yoki o'zgartirish tugmasi
        button_zagran_pasport_save = customtkinter.CTkButton(self.home_frame, text="", image=self.icon_image_redpasport,
                                                      width=35,
                                                      height=35, fg_color="white", hover_color="silver",
                                                      command=lambda:savefoto("pasport_zagran"))
        button_zagran_pasport_save.place(x=500, y=580)

        # Mukofot1 qoshish yoki o'zgartirish tugmasi
        button_mukofot1_save = customtkinter.CTkButton(self.home_frame, text="", image=self.icon_image_m1,
                                                             width=35,
                                                             height=35, fg_color="white", hover_color="silver",
                                                             command=lambda: savefoto("mukofot1"))
        button_mukofot1_save.place(x=550, y=580)

        # Mukofot2 qoshish yoki o'zgartirish tugmasi
        button_mukofot2_save = customtkinter.CTkButton(self.home_frame, text="", image=self.icon_image_m2,
                                                       width=35,
                                                       height=35, fg_color="white", hover_color="silver",
                                                       command=lambda: savefoto("mukofot2"))
        button_mukofot2_save.place(x=600, y=580)

        # Mukofot3 qoshish yoki o'zgartirish tugmasi
        button_mukofot3_save = customtkinter.CTkButton(self.home_frame, text="", image=self.icon_image_m3,
                                                       width=35,
                                                       height=35, fg_color="white", hover_color="silver",
                                                       command=lambda: savefoto("mukofot3"))
        button_mukofot3_save.place(x=650, y=580)


        # Treevew O'quvchilarni ko'rsatib turuvchi oyna

        self.tree_oqu_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=0, fg_color="transparent", width=430, height=560, border_width=1, border_color=("black","white"))
        self.tree_oqu_frame.place(x=490, y=5)

        # Scrollar
        scrollbarx = ttk.Scrollbar(self.tree_oqu_frame, orient="horizontal")
        scrollbary = ttk.Scrollbar(self.tree_oqu_frame, orient="vertical")

        # Trevewning ko'rinishi
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 10),
                        rowheght=25)  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 12, 'bold'))  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        # Treevew
        my_tree = ttk.Treeview(self.tree_oqu_frame, style="mystyle.Treeview")
        my_tree.place(x=5, y=5, width=400, height=530)
        my_tree.configure(yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        my_tree.configure(selectmode="extended")
        # scrollbar larning korinishi va joylashgan joyi
        scrollbary.configure(command=my_tree.yview)
        scrollbarx.configure(command=my_tree.xview)

        scrollbary.place(x=405, y=5, width=15, height=530)
        scrollbarx.place(x=5, y=536, width=400, height=15)

        my_tree.configure(
            columns=(
                "ID",
                "Familiyasi",
                "Ismi",
                "Sharifi",
                "Tug'ulgan yili"
            )
        )

        # Headings
        my_tree.heading("#0", text="N")
        my_tree.heading("ID", text="ID")
        my_tree.heading("Familiyasi", text="Familiyasi")
        my_tree.heading("Ismi", text="Ismi")
        my_tree.heading("Sharifi", text="Sharifi")
        my_tree.heading("Tug'ulgan yili", text="Tug'ulgan yili")
        # Colums
        my_tree.column("#0", minwidth=0, width=5)  # Tartib raqami
        my_tree.column("#1", minwidth=0, width=7)  # ID
        my_tree.column("#2", minwidth=0, width=50)  # Familiyasi
        my_tree.column("#3", minwidth=0, width=50)  # Ismi
        my_tree.column("#4", minwidth=0, width=50)  # Sharifi
        my_tree.column("#5", minwidth=0, width=50)  # Tug'ulgan yili
        #Treewevga ma'lumotlarni kirituvchi funktsiya

        def qabul(self):
            # o'quvchilar treevewda zebra bo'lib kornshi
            tr = 1
            my_tree.tag_configure('oddrow', background="white")
            my_tree.tag_configure('evenrow', background="#ecf8fe")
            result = stat.allbase()
            # treewevga ma'lumotlarni kiritish
            for record in result:
                if tr % 2 == 0:
                    my_tree.insert(parent='', index='end', text=str(tr), values=(
                    record[0], record[1], record[2], record[3], record[4]),
                                   tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', text=str(tr), values=(
                    record[0], record[1], record[2], record[3], record[4]),
                                   tags=('oddrow',))
                tr += 1

        qabul(self)

        # Treewevni malumottini sichqonchani ikki marotaba bossa ma'lumot ko'rinadi
        def OnDoubleClick1(event):
            # Ustun raqamini olamiz
            selected = my_tree.focus()
            # Boshqa malumotlarini olamiz
            values = my_tree.item(selected, 'values')
            try:
                r = values[0]
            except Exception:
                r = 1
            rr = stat.fromid(r)
            print_to_dashboard(rr)

        my_tree.bind("<Double-1>", OnDoubleClick1)

        # O'quvchini ko'rsatkichlar grafigini ekranga chiqarish funktsiyasi
        def to_grafik():
            sana = []
            yuzm = []
            totryuzm = []
            birmingbeshm = []
            club = []
            arava = []
            balandlik = []
            disk = []
            nayza = []
            uzunlik = []
            yadro = []
            if idn.cget("text"):
                kors = stat.korsatkich_grafik_baza(idn.cget("text"))
                for iil in kors:
                    sana.append(iil[2])
                    yuzm.append(iil[3])
                    totryuzm.append(iil[4])
                    birmingbeshm.append(iil[5])
                    club.append(iil[6])
                    arava.append(iil[7])
                    balandlik.append(iil[8])
                    disk.append(iil[9])
                    nayza.append(iil[10])
                    uzunlik.append(iil[11])
                    yadro.append(iil[12])

            f = fam.get()
            i_s = ism.get()
            sh = sharif.get()

            x = [datetime.strptime(date_str, "%d.%m.%Y") for date_str in sana]
            y = [float(value) for value in yuzm]
            y1 = [float(value) for value in totryuzm]
            y2 = [float(value) for value in birmingbeshm]
            y3 = [float(value) for value in club]
            y4 = [float(value) for value in arava]
            y5 = [float(value) for value in balandlik]
            y6 = [float(value) for value in disk]
            y7 = [float(value) for value in nayza]
            y8 = [float(value) for value in uzunlik]
            y9 = [float(value) for value in yadro]

            # График
            plt.figure(figsize=(10, 5))
            plt.plot(x, y, marker='o', label='100 metr')
            plt.plot(x, y1, marker='s', label='400 metr')
            plt.plot(x, y2, marker='D', label='1500 metr')
            plt.plot(x, y3, marker='v', label='Club')
            plt.plot(x, y4, marker='*', label='Arava')
            plt.plot(x, y5, marker='P', label='Balandlik')
            plt.plot(x, y6, marker='X', label='Disk')
            plt.plot(x, y7, marker='h', label='Nayza')
            plt.plot(x, y8, marker='<', label='Uzunlik')
            plt.plot(x, y9, marker='>', label='Yadro')

            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d.%m'))
            plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator())

            plt.xlabel("Ko'rsatkich olingan sanalar")
            plt.ylabel("Korsatkich metr o'lchamida")
            plt.title(f"Sportchi {f} {i_s} {sh} ko'rsatkichlari. ID raqani: {idn.cget("text")} ")

            plt.grid(True)
            plt.gcf().autofmt_xdate()  # красиво повернёт даты
            plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Sport turi", fontsize='small')
            plt.tight_layout()

            plt.show()

        # O'quvchini grafigini chiqarib beruvchi knopka
        button_grafik = customtkinter.CTkButton(self.home_frame, text="Grafik", image=self.icon_image_grafik, width=35,
                                             height=35, fg_color="white", hover_color="silver", command=to_grafik, anchor="center",compound="top")
        button_grafik.place(x=700, y=580)

        def korsatkich():
            if idn.cget('text'):
                Korsatkich.korsatkich_qosh(self, idn.cget('text'), fam.get(), ism.get(), sharif.get())
            else:
                mb.showinfo("Diqqat!!!", "O'quvchi tanlanmadi. Yangi o'quvchi kiriting yoki tanlang!!!")


        # Ko'rsatkichlarni kiritish knopka
        button_korsatkich_kiritish = customtkinter.CTkButton(self.home_frame, text="Ko'rsatkich\nkiritish", image=self.icon_image_grafik, width=35,
                                                height=35, fg_color="white", hover_color="silver", command=korsatkich, anchor="center",compound="top")
        button_korsatkich_kiritish.place(x=753, y=580)


        def all_pupill_to_excel():
            dat = stat.allbase()
            ex = Docs.allpupilexcel(dat,0)
            if ex:
                mb.showerror("Xatolik", ex)



        # O'quvchini grafigini chiqarib beruvchi knopka
        button_oquvchilar = customtkinter.CTkButton(self.home_frame, text="Jami", image=self.icon_image_excell, width=35,
                                                height=35, fg_color="white", hover_color="silver", command=all_pupill_to_excel, anchor="center",compound="top")
        button_oquvchilar.place(x=835, y=580)


        # Papkaga o'quvchining barcha ma'lumotlarini chiqarish
        def gotodir():
            if idn.cget("text") !="":
                dat = (stat.fromid(idn.cget("text")))
                ex = Docs.todirectory(dat, 0)
                if ex:
                    mb.showerror("Xatolik",ex)
            else:
                mb.showerror("Xatolik", "O'quvchining ma'lumotlarini toping!!!")


        button_dir = customtkinter.CTkButton(self.home_frame, text="", image=self.icon_image_dir, width=35,
                                             height=35, fg_color="white", hover_color="silver", command=gotodir)
        button_dir.place(x=885, y=580)





