# -*- coding: <utf-8> -*-

import pickle
import sqlite3
import os, sys

path_gl=""
BaseName_gl="pinfo.db"

class Base:

	def create_sql():
		# print ("create_sql")
		"""Создает файл базы SQL с необходимыми таблицами"""

		conn = sqlite3.connect(path_gl+'/'+BaseName_gl)
		f = conn.cursor()

		# Create table Users
		f.execute('''CREATE TABLE Users
             (ID text NOT NULL PRIMARY KEY, UserName text, City text, BL INTEGER DEFAULT 0, FL INTEGER DEFAULT 0)''')

		# Create table Pics
		f.execute('''CREATE TABLE Pics
             (
             	ID text NOT NULL,
             	Pic text NOT NULL,
             	CONSTRAINT pk_Pic_ID PRIMARY KEY (ID,Pic)
             	)''')

		# Create table Login Password
		f.execute('''CREATE TABLE LP
             (
             	Login text,
             	Password text
             	)''')

		conn.commit()
		conn.close()

	def create_sql_dir_db():
		"""Создает файл dir.db для директории SQL в папке с прогой и записывает в него путь по умолчанию на D:/!!! P.Info'"""

		conn = sqlite3.connect(Base.module_path()+'/'+'dir.db')
		f = conn.cursor()

		# Create table Directory and write default way into it ('D:/!!! P.Info')
		f.execute('''CREATE TABLE Directory
             (
             	Dir text NOT NULL PRIMARY KEY
             	)''')

		temp=('D:'+'/'+'!!! P.Info',)
		f.execute("INSERT OR IGNORE INTO Directory(Dir) VALUES (?)", temp)

		conn.commit()
		conn.close()

	def convert_pinfo():
		"""Читает данные из файла старой базы и вносит их в новую базу SQL"""

		OldBaseName="p.info.bs"

		with open(path_gl+'/'+OldBaseName, 'rb') as ff:
			base1 = pickle.load(ff)

		conn = sqlite3.connect(path_gl+'/'+BaseName_gl)
		f = conn.cursor()

		for id1 in base1:
			usid=id1
			usname=list(base1[id1].keys())[0]
			piclist=base1[usid][usname]
			temp=(usid, usname)

			f.execute("INSERT OR IGNORE INTO Users(ID, UserName) VALUES (?, ?)", temp)

			for id2 in piclist:
				temp2=(usid, id2)

				# '''эта часть кода выводит те записи, которые уже есть в таблице'''
				# try:
				# 	f.execute("INSERT INTO Pics VALUES (?, ?)", temp2)
				# except sqlite3.IntegrityError as err:
				# 	print(temp2)

				f.execute("INSERT OR IGNORE INTO Pics VALUES (?, ?)", temp2)

		ff.close()
		conn.commit()
		conn.close()

	def convert_fotorate():
		"""Читает данные из файла старого фоторейтинга и вносит их в новую базу SQL"""

		FotoRateName="p.info.fotorate.bs"

		with open(path_gl+'/'+FotoRateName, 'rb') as ff:
			base1 = pickle.load(ff)

		conn = sqlite3.connect(path_gl+'/'+BaseName_gl)
		f = conn.cursor()

		for i in base1:
			usid=i
			piclist=base1[i]
			for pic in piclist:
				temp=(usid, pic)
				f.execute("INSERT OR IGNORE INTO Pics VALUES (?, ?)", temp)

		ff.close()
		conn.commit()
		conn.close()

	def convert_lp():
		"""Читает данные из старого файла логин-пароль и вносит их в новую базу SQL"""

		LogPassName="LP.bs"

		with open(path_gl+'/'+LogPassName, 'rb') as ff:
			base5 = pickle.load(ff)

		conn = sqlite3.connect(path_gl+'/'+BaseName_gl)
		f = conn.cursor()

		temp=(str(base5['log']), str(base5['pas']))

		f.execute("INSERT OR IGNORE INTO LP VALUES (?, ?)", temp)

		ff.close()
		conn.commit()
		conn.close()

	def convert_old_base():
		"""конвертация тех старых файлов базы, которые есть в папке"""

		OldBaseName="p.info.bs"
		FotoRateName="p.info.fotorate.bs"
		LogPassName="LP.bs"

		if os.path.isfile (path_gl+'/'+OldBaseName)==True:
			Base.convert_pinfo()
			print ("Pinfo Converted")

		if os.path.isfile (path_gl+'/'+FotoRateName)==True:
			Base.convert_fotorate()
			print ("Fotorate Converted")

		if os.path.isfile (path_gl+'/'+LogPassName)==True:
			Base.convert_lp()
			print ("LP Converted")

	def is_base():
		"""проверка, есть ли файл базы sql"""

		if os.path.isfile (path_gl+'/'+BaseName_gl)==True:
			return True
		else:
			return False

	def del_old_base():
		"""проверка, есть ли старые файлы и удаление тех, что есть"""

		OldBaseName="p.info.bs"
		FotoRateName="p.info.fotorate.bs"
		LogPassName="LP.bs"

		if os.path.isfile (path_gl+'/'+OldBaseName)==True:
			os.remove(path_gl+'/'+OldBaseName)
			print (OldBaseName+" successfully deleted.")

		if os.path.isfile (path_gl+'/'+FotoRateName)==True:
			os.remove(path_gl+'/'+FotoRateName)
			print (FotoRateName+" successfully deleted.")

		if os.path.isfile (path_gl+'/'+LogPassName)==True:
			os.remove(path_gl+'/'+LogPassName)
			print (LogPassName+" successfully deleted.")

	def start_base():
		"""алгоритм действий при старте базы"""
		global path_gl

		#проверяем есть ли файл dir.db в директории с прогой, если есть, читает из него path_gl, если нет - создает
		if os.path.isfile (Base.module_path()+'/'+'dir.db')==False:
			Base.create_sql_dir_db()

		path_gl=Base.get_dir()


		# проверяем, есть ли папка path_gl, если нет - создаем
		if os.path.isdir(path_gl)==False:
			os.makedirs(path_gl)

		# проверка - есть ли файл sql базы, если нет, то создание файла
		if Base.is_base()==False:
			Base.create_sql()

		# проверка есть ли старые файлы баз, и если они есть, то конвертация их в новую базу
		Base.convert_old_base()

		# проверка есть ли старые файлы баз, и если они есть, то удаление их
		Base.del_old_base()


	def get_path_gl():
		return path_gl

	def get_dir():
		"""проверяет папку назначения, и возвращает её, или False если в таблице пусто"""

		conn = sqlite3.connect(Base.module_path()+'/'+'dir.db')
		f = conn.cursor()

		f.execute('SELECT * FROM Directory')
		u=f.fetchone()
		conn.close()
		if u==None:
			return False
		else:
			return u[0]

	def is_lp():
		# print ("is_lp")
		"""проверяет таблицу логин-пароль, и возвращает их, или False если в таблице пусто"""

		conn = sqlite3.connect(path_gl+'/'+BaseName_gl)
		f = conn.cursor()

		f.execute('SELECT * FROM LP')
		u=f.fetchone()
		conn.close()
		if u==None:
			return False
		else:
			return u

	def add_lp(login, password):
		# print ("add_lp")
		"""вписывает логин пароль в таблицу LP, если в таблице были значения - удаляет их перед записью новых """

		conn = sqlite3.connect(path_gl+'/'+BaseName_gl)
		f = conn.cursor()

		temp=(login,password)
		if Base.is_lp()!=False:
			f.execute("DELETE FROM LP")
		f.execute("INSERT INTO LP VALUES (?, ?)", temp)
		conn.commit()
		conn.close()

	def add_dir(papka):
		"""Записывает новое значение в dir.db в папке с прогой"""

		if papka==Base.get_dir():
			return

		conn = sqlite3.connect(Base.module_path()+'/'+'dir.db')
		f = conn.cursor()

		f.execute("DELETE FROM Directory")
		temp=(papka,)
		f.execute("INSERT OR IGNORE INTO Directory(Dir) VALUES (?)", temp)

		conn.commit()
		conn.close()

		global path_gl
		path_gl=papka


	def module_path():
		if hasattr(sys, "frozen"):
			return os.path.dirname(str(sys.executable))
		return os.path.dirname(str(__file__))

	def list_usernames():
		# print ("list_usernames")
		"""Возвращает 3 переменных: 	1) словарь - user:кол-во фото,
										2) общее кол-во пользователей в базе sql
										3) общее кол-во фото в базе sql """

		conn = sqlite3.connect(path_gl+'/'+BaseName_gl)
		f = conn.cursor()
		photo=0
		user=0
		dic={}
		for i in f.execute ('SELECT UserName,(SELECT COUNT(ID) from Pics where Pics.ID=Users.ID) as cnt from Users ORDER BY UserName'):
			photo=photo+i[1]
			user+=1
			dic[str(i[0])]=str(i[1])
		return dic, user, photo

	def list_all_users_ID():
		# print ("list_all_users_ID")
		"""Возвращает ID всех пользователей в базе, которые НЕ в Блэклисте"""

		ID_list=[]
		conn = sqlite3.connect(path_gl+'/'+BaseName_gl)
		f = conn.cursor()
		for row in f.execute("SELECT ID FROM Users WHERE BL!=1"):
			ID_list.append(row[0])
		return ID_list



	def if_pics(u_id, ph_id):
		# print ("if_pics")
		"""проверяет, есть ли данная фотка в общей базе"""

		u_id=str(u_id)
		ph_id=str(ph_id)

		conn = sqlite3.connect(path_gl+'/'+BaseName_gl)
		f = conn.cursor()

		f.execute("SELECT ID FROM Pics WHERE Pic='%s'" % ph_id)
		u=f.fetchone()

		if u == None:
			return False
		return True

	def if_piclist(u_id, ph_id):
		# print ("if_pics")
		"""проверяет, есть ли данная фотка в общей базе"""

		u_id=str(u_id)
		ph_id=str(ph_id)

		conn = sqlite3.connect(path_gl+'/'+BaseName_gl)
		f = conn.cursor()

		f.execute("SELECT ID FROM Pics WHERE Pic='%s'" % ph_id)
		u=f.fetchone()

		if u == None:
			return False
		return True

	def if_userid_in_users(u_id):
		# print ("if_userid_in_users")
		"""проверяет, есть ли данный юзер в базе"""

		conn = sqlite3.connect(path_gl+'/'+BaseName_gl)
		f = conn.cursor()

		f.execute("SELECT * FROM Users WHERE ID='%s'" % u_id)
		u=f.fetchone()

		if u:
			return True
		else:
			return False




	def get_id_from_name(u_name):
		# print ("get_id_from_name")
		"""получает Имя польз. Возвращает ID польз"""

		conn = sqlite3.connect(path_gl+'/'+BaseName_gl)
		f = conn.cursor()

		u_name=str(u_name)
		u_name=u_name.lower()

		f.execute("SELECT ID FROM Users WHERE UserName='%s'" % u_name)
		u=f.fetchone()

		if u:
			return u[0]
		return False

	def get_name_from_id(u_id):
		# print ("get_name_from_id")
		"""получает ID польз. Возвращает ИМЯ польз"""

		conn = sqlite3.connect(path_gl+'/'+BaseName_gl)
		f = conn.cursor()

		u_id=str(u_id)

		f.execute("SELECT UserName FROM Users WHERE ID='%s'" % u_id)
		u=f.fetchone()

		if u:
			return u[0]
		return False

	def get_all_pics_from_user(u_id):
		# print ("get_all_pics_from_user")
		"""выводит все фото выбранного пользователя по ID"""

		conn = sqlite3.connect(path_gl+'/'+BaseName_gl)
		f = conn.cursor()

		u_id=str(u_id)
		u_id=u_id.lower()

		l=[]

		for row in f.execute("SELECT Pic FROM Pics WHERE ID='%s'" % u_id):
			l.append(row[0])
		return l

	def add_user_and_pics_to_base(u_id, u_name, pic_list_or_pic):
		# print ("add_user_and_pics_to_base")
		""" Добавляет запись о пользователе в базу данных
			также добавляет записи о фотках"""

		u_id=str(u_id)
		u_name=str(u_name)
		u_name=u_name.lower()

		conn = sqlite3.connect(path_gl+'/'+BaseName_gl)
		f = conn.cursor()

		temp=(u_id, u_name)
		f.execute("INSERT OR IGNORE INTO Users(ID, UserName) VALUES (?, ?)", temp)

		if type(pic_list_or_pic)==list:
			for i in pic_list_or_pic:
				temp2=(u_id, str(i))
				f.execute("INSERT OR IGNORE INTO Pics VALUES (?, ?)", temp2)
		else:
			temp2=(u_id, str(pic_list_or_pic))
			f.execute("INSERT OR IGNORE INTO Pics VALUES (?, ?)", temp2)


		conn.commit()
		conn.close()



	def get_blacklist():
		# print ("get_blacklist")
		"""возвращает словарь пользователь:ID , которые находятся в блэклисте"""

		dic={}
		conn = sqlite3.connect(path_gl+'/'+BaseName_gl)
		f = conn.cursor()

		for i in f.execute("SELECT UserName, ID FROM Users WHERE BL=1"):
			dic[i[0]]=i[1]

		return dic

	def add_to_blacklist(u_id):
		# print ("add_to_blacklist")
		"""добавляет пользователя в блэклист по ID"""

		u_id=str(u_id)

		conn = sqlite3.connect(path_gl+'/'+BaseName_gl)
		f = conn.cursor()

		f.execute("UPDATE Users SET BL=1 WHERE ID='{0}'".format(u_id))

		conn.commit()
		conn.close()

	def remove_from_blacklist(u_id):
		# print ("remove_from_blacklist")
		"""удаляет пользователя из блэклиста по ID"""

		u_id=str(u_id)

		conn = sqlite3.connect(path_gl+'/'+BaseName_gl)
		f = conn.cursor()

		f.execute("UPDATE Users SET BL=0 WHERE ID='{0}'".format(u_id))

		conn.commit()
		conn.close()

	def if_userid_in_BL(u_id):
		# print ("if_userid_in_BL")
		"""проверяет, есть ли данный юзер в блэклисте"""

		u_id=str(u_id)

		conn = sqlite3.connect(path_gl+'/'+BaseName_gl)
		f = conn.cursor()

		f.execute("SELECT BL FROM Users WHERE ID='%s'" % u_id)
		u=f.fetchone()

		try:
			if u[0]==1:
				return True
		except:
			return False



	def get_favorlist():
		# print ("get_favorlist")
		"""возвращает словарь пользователь:ID , которые находятся в фаворе"""

		dic={}
		conn = sqlite3.connect(path_gl+'/'+BaseName_gl)
		f = conn.cursor()

		for i in f.execute("SELECT UserName, ID FROM Users WHERE FL=1"):
			dic[i[0]]=i[1]

		return dic

	def add_to_favorlist(u_id):
		# print ("add_to_favorlist")
		"""добавляет пользователя в фавор по ID"""

		u_id=str(u_id)

		conn = sqlite3.connect(path_gl+'/'+BaseName_gl)
		f = conn.cursor()

		f.execute("UPDATE Users SET FL=1 WHERE ID='{0}'".format(u_id))

		conn.commit()
		conn.close()

	def remove_from_favorlist(u_id):
		# print ("remove_from_favorlist")
		"""удаляет пользователя из фавора по ID"""

		u_id=str(u_id)

		conn = sqlite3.connect(path_gl+'/'+BaseName_gl)
		f = conn.cursor()

		f.execute("UPDATE Users SET FL=0 WHERE ID='{0}'".format(u_id))

		conn.commit()
		conn.close()

if __name__ == '__main__':
	# Base.start_base()
	pass



