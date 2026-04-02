import sqlite3 as sq
import atexit
import os

class Stat:
    def __init__(self, db_path="sb.db"):
        db_exists = os.path.exists(db_path) #
        self.con = sq.connect(db_path, check_same_thread=False)
        self.cur = self.con.cursor()

        if not db_exists: #--
            self._create_tables() #--

        atexit.register(self._close_connection)

    def _create_tables(self): #
        """Создаёт таблицу, если базы не было"""

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS autoraize (
            idau INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT,
        	password TEXT
        )
        """)
        # Login va parol yaratadi
        logpar=("Mavlonbek", "Grin_tay")
        self.cur.execute(f"INSERT INTO autoraize (login, password) VALUES {logpar}")

        self.cur.execute("""
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

        self.cur.execute("""
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

        self.cur.execute("""
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

        self.con.commit()#


    def _close_connection(self):
        """Автоматически вызывается при завершении программы"""
        if self.con:
            self.con.close()
            self.con = None

    def pupls123(self,s):
        """Bazadan barcha o'qiyotgan o'quvchilar sonini aniqlaydi"""
        self.cur.execute(f"SELECT COUNT(*) FROM user WHERE status = ?",(s,))
        return self.cur.fetchone()[0]

    def allbase(self):
        """Bazadagi barcha ma'lumotlarni treewevda ko'rinishi uchun oladi"""
        self.cur.execute("SELECT * FROM user")
        return self.cur.fetchall()

    def fambase(self,oqch_fam):
        """O'quvchi familiyasiga qarab ma'lumotlarini oladi combodan Entrilarga"""
        self.cur.execute("SELECT * FROM user WHERE fam = ?", (oqch_fam,))
        return self.cur.fetchone()

    def famcombo(self):
        """ Combobox qidiruvi uchun o'quvchilarni barcha familiyalarini olosh"""
        self.cur.execute("SELECT fam FROM user")
        return self.cur.fetchall()

    def fromid(self,oqch_id):
        """ O'quvchini id si bo'yicha ma'lumotlarini olish"""
        self.cur.execute("SELECT * FROM user WHERE id = ('%s')" % (oqch_id))
        return self.cur.fetchone()

    def oqchgruh(self,ids):
        """O'quvchi qaysi gruhda o'qigan ma'lumotlarni treewevda ko'rinishi"""
        self.cur.execute(f"SELECT * FROM darsjarayon WHERE iid = ?",(ids,))
        return self.cur.fetchall()

    def oqchi_bazaga_qoshish(self,pupl):
        """ Yangi o'quvchini bazaga user jadvaliga qoshish """
        self.cur.execute(
            "INSERT INTO user (fam, ism, sharif, tugyil, tel1, tel2, pasmet, resp, vil, tum, mfy, koch, jshshr, nogirg, status, murabbiy) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",pupl)
        self.con.commit()

    def korsatkich_kiritish(self,pupl):
        """ O'quvchining yangi ko'rsatkichlarini kiritish """
        self.cur.execute(f"INSERT INTO korsatkichlar (id_user, sana, yuzm, tortyuzm, birmingbeshm, club, arava, balandlik, disk, nayza, uzunlik, yadro) VALUES {pupl}")
        self.con.commit()
    def bazaga_foto_qoshish(self,file_path_name_id):
        """ O'quvchini id si bo'yicha bazagga fotosuratini qo'shadi """
        self.cur.execute(f"UPDATE user SET {file_path_name_id[0]} = ? WHERE id = ?",file_path_name_id[1: ])
        self.con.commit()
    def oqchi_bazadan_ochirish(self,pupl_id):
        """ O'quvchini bazadan user jadvalidan o'chirish """
        self.cur.execute(f"DELETE FROM user WHERE id = ?",(pupl_id,))
        self.con.commit()
    def korsatkich_grafik_baza(self,pupl_id):
        """ O'quvchini grafigi uchun ko'rsatkich ma'lumotlarini olish """
        self.cur.execute(f"SELECT * FROM korsatkichlar WHERE id_user = ?",(pupl_id,))
        return self.cur.fetchall()

    def ohirgi_oquvchini_olish(self):
        """ Bazaga ohirgi bo'lib yozilgan o'quvchini ma'lumotlarini olish """
        self.cur.execute("SELECT * FROM user ORDER BY id DESC LIMIT 1")
        return self.cur.fetchall()

    def ozgartirish(self,id,mal):
        """ Bazadagi o'quvchi ma'lumotlarini tahrirlash """
        self.cur.execute(f"UPDATE user SET fam=?,ism=?,sharif=?,tugyil=?,tel1=?,tel2=?,pasmet=?,resp=?,vil=?,tum=?,mfy=?,koch=?,jshshr=?,nogirg=?,status=?, murabbiy=? WHERE id = {id}", mal)
        self.con.commit()

    def login_password(self):
        """Bazadan fotdalanuvchi login parolini oladi"""
        self.cur.execute("SELECT * FROM autoraize")
        return self.cur.fetchall()

    # Murabbiylar ma'lumotini bazadan olish
    def allmurabbiy(self):
        """Bazadan barcha murabbiylarni treewew uchun olish """
        self.cur.execute("SELECT * FROM murabbiy")
        return self.cur.fetchall()

    def from_mur_id(self,mur_id):
        """ Murabbiy id si bo'yicha ma'lumotlarini olish"""
        self.cur.execute("SELECT * FROM murabbiy WHERE idmurabbiy = ('%s')" % (mur_id))
        return self.cur.fetchone()

    def fam_mur_base(self,mur_fam):
        """Murabbiy familiyasiga qarab ma'lumotlarini oladi combodan Entrilarga"""
        self.cur.execute(f"SELECT * FROM murabbiy WHERE fam = ?",(mur_fam,))
        return self.cur.fetchone()

    def fam_mur_combo(self):
        """ Combobox qidiruvi uchun Murabbiylarni barcha familiyalarini olosh"""
        self.cur.execute("SELECT fam FROM murabbiy")
        return self.cur.fetchall()

    def fam_ism_mur_combo(self):
        """ Combobox qidiruvi uchun Murabbiylarni barcha familiyalarini olosh"""
        self.cur.execute("SELECT idmurabbiy, fam, ism FROM murabbiy")
        return self.cur.fetchall()

    def fromidmurabbiy(self,mur_id):
        """ Murabbiyni id si bo'yicha ma'lumotlarini olish"""
        self.cur.execute("SELECT * FROM murabbiy WHERE idmurabbiy = ('%s')" % (mur_id))
        return self.cur.fetchone()

    def oquvchi_mur_id(self,mur_id):
        """ Murabbiylarning id si bo'yicha o'quvchilarni ma'lumotlarini olish (Murabbiylarning shogirdlarini saralash)"""
        self.cur.execute("SELECT * FROM user WHERE murabbiy = ('%s')" % (mur_id))
        return self.cur.fetchall()

    def murabbiy_bazaga_qoshish(self,murabbiy):
        """ Yangi o'quvchini bazaga user jadvaliga qoshish """
        self.cur.execute(
            "INSERT INTO murabbiy (fam, ism, sharif, tugyil, tel1, tel2, pasmet, resp, vil, tum, mfy, koch, jshshr, nogirg, status) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",murabbiy)
        self.con.commit()

    def murabbiy_bazaga_foto_qoshish(self,file_path_name_id):
        """ Murabbiyning id si bo'yicha bazaga fotosuratini qo'shadi """
        self.cur.execute(f"UPDATE murabbiy SET {file_path_name_id[0]} = ? WHERE idmurabbiy = ?",file_path_name_id[1: ])
        self.con.commit()

    def murabbiyni_bazadan_ochirish(self,mur_id):
        """ Murabbiyni bazadan user jadvalidan o'chirish """
        self.cur.execute(f"DELETE FROM murabbiy WHERE idmurabbiy = ?",(mur_id,))
        self.con.commit()

    def murabbiyniozgartirish(self,id,mal):
        """ Bazadagi murabbiy ma'lumotlarini tahrirlash """
        self.cur.execute(f"UPDATE murabbiy SET fam=?,ism=?,sharif=?,tugyil=?,tel1=?,tel2=?,pasmet=?,resp=?,vil=?,tum=?,mfy=?,koch=?,jshshr=?,nogirg=?,status=?  WHERE idmurabbiy = {id}", mal)
        self.con.commit()


    # Agar baza bolmasa baza yaratish funktsiyasi

    def create_tables_ifnot(self):
        """Создаёт таблицу, если базы неt"""

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS autoraize (
            idau INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT,
        	password TEXT
        )
        """)
        # Login va parol yaratadi
        logpar=("Mavlonbek", "Grin_tay")
        self.cur.execute(f"INSERT INTO autoraize (login, password) VALUES {logpar}")

        self.cur.execute("""
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

        self.cur.execute("""
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

        self.cur.execute("""
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

        self.con.commit()#
