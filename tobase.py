import sqlite3 as sq


class Stat:

    def pupls123(self,s):
        """Bazadan barcha o'qiyotgan o'quvchilar sonini aniqlaydi"""
        with sq.connect("sb.db") as con:
            cur = con.cursor()
            cur.execute(f"SELECT COUNT(*) FROM user WHERE status = {s}")
            result = cur.fetchall()
            con.commit()
            r = result[0][0]
            return r

    # Bazadagi barcha ma'lumotlarni treewevda ko'rinishi uchun oladi
    def allbase():
        with sq.connect("sb.db") as con:
            cur = con.cursor()
            # tovar jadvaldan shtriix codi orqali ma'lumot olish
            cur.execute("SELECT * FROM user")
            result = cur.fetchall()
            con.commit()
            return result

    # o'quvchi familiyasiga qarab ma'lumotlarini oladi combodan Entrilarga
    def fambase(oqch_fam):
        with sq.connect("sb.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM user WHERE fam = ('%s')" % (oqch_fam))
            r = cur.fetchone()
            con.commit()
            return r

    def famcombo():
        """ Combobox qidiruvi uchun o'quvchilarni barcha familiyalarini olosh"""
        with sq.connect("sb.db") as con:
            cur = con.cursor()
            cur.execute("SELECT fam FROM user")
            oqch = cur.fetchall()
            con.commit()
            return oqch

    def fromid(oqch_id):
        """ O'quvchini id si bo'yicha ma'lumotlarini olish"""
        with sq.connect("sb.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM user WHERE id = ('%s')" % (oqch_id))
            r = cur.fetchone()
            con.commit()
            return r


    def oqchgruh(ids):
        # O'quvchi qaysi gruhda o'qigan ma'lumotlarni treewevda ko'rinishi
        with sq.connect("sb.db") as con:
            cur = con.cursor()
            cur.execute(f"SELECT * FROM darsjarayon WHERE iid = {ids}")
            result = cur.fetchall()
            con.commit()
            return result

    def oqchi_bazaga_qoshish(pupl):
        """ Yangi o'quvchini bazaga user jadvaliga qoshish """
        with sq.connect("sb.db") as con:
            cur = con.cursor()
            cur.execute(f"INSERT INTO user (fam, ism, sharif, tugyil, tel1, tel2, pasmet, resp, vil, tum, mfy, koch, jshshr, nogirg, status) VALUES {pupl}")
            con.commit()

    def korsatkich_kiritish(pupl):
        """ O'quvchining yangi ko'rsatkichlarini kiritish """
        with sq.connect("sb.db") as con:
            cur = con.cursor()
            cur.execute(f"INSERT INTO korsatkichlar (id_user, sana, yuzm, tortyuzm, birmingbeshm, club, arava, balandlik, disk, nayza, uzunlik, yadro) VALUES {pupl}")
            con.commit()
    def bazaga_foto_qoshish(file_path_name_id):
        """ O'quvchini id si bo'yicha bazagga fotosuratini qo'shadi """
        with sq.connect("sb.db") as con:
            cur = con.cursor()
            cur.execute(f"UPDATE user SET {file_path_name_id[0]} = ? WHERE id = ?",file_path_name_id[1: ])
            con.commit()

    def oqchi_bazadan_ochirish(pupl_id):
        """ O'quvchini bazadan user jadvalidan o'chirish """
        with sq.connect("sb.db") as con:
            cur = con.cursor()
            cur.execute(f"DELETE FROM user WHERE id = {pupl_id}")
            con.commit()

    def korsatkich_grafik_baza(pupl_id):
        """ O'quvchini grafigi uchun ko'rsatkich ma'lumotlarini olish """
        with sq.connect("sb.db") as con:
            cur = con.cursor()
            cur.execute(f"SELECT * FROM korsatkichlar WHERE id_user = {pupl_id}")
            result = cur.fetchall()
            con.commit()
            return result

    def ohirgi_oquvchini_olish():
        """ Bazaga ohirgi bo'lib yozilgan o'quvchini ma'lumotlarini olish """
        with sq.connect("sb.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM user ORDER BY id DESC LIMIT 1")
            result = cur.fetchall()
            con.commit()
            return result

    def ozgartirish(id, mal):
        """ Bazadagi o'quvchi ma'lumotlarini tahrirlash """
        with sq.connect("sb.db") as con:
            cur = con.cursor()
            cur.execute(f"UPDATE user SET fam=?,ism=?,sharif=?,tugyil=?,tel1=?,tel2=?,pasmet=?,resp=?,vil=?,tum=?,mfy=?,koch=?,jshshr=?,nogirg=?,status=?  WHERE id = {id}", mal)
            con.commit()


    def login_password():
        """Bazadan fotdalanuvchi login parolini oladi"""
        with sq.connect("sb.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM autoraize")
            result = cur.fetchall()
            con.commit()
            return result

    # Murabbiylar ma'lumotini bazadan olish
    def allmurabbiy():
        """Bazadan barcha murabbiylarni treewew uchun olish """
        with sq.connect("sb.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM murabbiy")
            result = cur.fetchall()
            con.commit()
            return result

    def from_mur_id(mur_id):
        """ Murabbiy id si bo'yicha ma'lumotlarini olish"""
        with sq.connect("sb.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM murabbiy WHERE idmurabbiy = ('%s')" % (mur_id))
            r = cur.fetchone()
            con.commit()
            return r



# sb jadvaldagi tartib va ustunlar

# id, fam, ism, sharif, tugyil, tel1, tel2, pas_met, resp, vil, tum, mfy, koch, jshshr, nogirg, status,
# jshshr -> integer
# Qogani hammasi -> text
#--------------
# Qosimov
# Dilshod
# Mahmudovich
# 11.07.2005
# 950050150
# 950110102
# AB1234567
# O'zbekiston
# Andijon
# Marhamat
# Navro'z
# Bilimdonlar
# 12345678912345
# AN123456
# o'qimoqda







# SQL to'g'risida ma'lumot oladigan joy
# https://space-base.ru/library/sql/


# id = 1 teng bo'lgan satrni oladi
# SELECT * FROM pupil WHERE id = 1

# Jadval ichiga yangi satr ma'lumotlarini qo'shadi
# pupl = ('Karimov',"Islom","Abduganievich","1936","+9981111111","Jannat MFY","Savob olish kursi")
# f"INSERT INTO pupil (fam, ism, shar, tug, tel, man, sin) VALUES {pupl}"
# INSERT INTO students (id, yosh, ismi, familiya, tel) VALUES (1,36,"Islom","Karimov","+9981111111")


# Jadval ichidagi id satr ma'lumotlarini o'chiradi
# f"DELETE FROM pupil WHERE id = {num}"

# Ustunni o'chirish
# ALTER TABLE students DROP COLUMN Email

# Jadval yaratish
# CREATE TABLE Customers (Id INT, Age INT, FirstName NVARCHAR(20), LastName NVARCHAR(20), Email VARCHAR(30), Phone VARCHAR(20))

# Jadvalga ma'lumot qoshish
# INSERT INTO students (id, yosh, ismi, familiya, tel) VALUES (5,41,"Bakirov","Sobir","+998950050150");
# INSERT INTO students (id, yosh, ismi, familiya, tel) VALUES (6,42,"Qobulov","Doston","+998950050150");
# INSERT INTO students (id, yosh, ismi, familiya, tel) VALUES (7,44,"Mamatov","Murod","+998950050150");
# INSERT INTO students (id, yosh, ismi, familiya, tel) VALUES (8,46,"Muhamadziyo","Marhamatov","+998950050150");
# INSERT INTO students (id, yosh, ismi, familiya, tel) VALUES (9,47,"Sodiqova","Mohigul","+998950050150");
# INSERT INTO students (id, yosh, ismi, familiya, tel) VALUES (4,40,"Teshaboev","Shukurullo","+998950050185");

# Jadvalga ma'lumot qoshish
# INSERT INTO students (
# id, yosh, ismi, familiya, tel
# )  VALUES
#	(10,41,"Bakirov","Sobir","+998950050150"),
#	(11,42,"Qobulov","Doston","+998950050150"),
#	(12,44,"Mamatov","Murod","+998950050150"),
#	(13,46,"Muhamadziyo","Marhamatov","+998950050150"),
#	(14,47,"Sodiqova","Mohigul","+998950050150"),
#	(15,40,"Teshaboev","Shukurullo","+998950050185")


# Satrlarni yangilash
# UPDATE students SET yosh=12, ismi="Muslima",familiya = "Boltaboeva", tel="+998912071515" WHERE id = 15
# UPDATE students SET tel="+998950050150"

# 45 dan kam yoki teng yoshlilarni hammasini 45 ga tenglaydi
# UPDATE students SET yosh = 45  WHERE yosh <= 45

# Ustun qoshish
# ALTER TABLE students ADD manzil TEXT