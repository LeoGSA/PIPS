import sys, pickle, os, time, requests
# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QShortcut
import pics
from base import *

cookies_gl={}

class Ui_Form(QWidget):
    def __init__(self, parent=None):
        super(Ui_Form, self).__init__(parent)
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 475)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setMinimumSize(QtCore.QSize(100, 0))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.Sh_pic = QtWidgets.QCheckBox(self.groupBox_2)
        self.Sh_pic.setGeometry(QtCore.QRect(10, 130, 91, 20))
        self.Sh_pic.setObjectName("Sh_pic")
        self.Sh_pic.setChecked(True)
        self.radioStandard = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioStandard.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.radioStandard.setChecked(True)
        self.radioStandard.setObjectName("radioStandard")
        self.radio_print_user_base = QtWidgets.QRadioButton(self.groupBox_2)
        self.radio_print_user_base.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.radio_print_user_base.setObjectName("radio_print_user_base")
        self.radioHelp = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioHelp.setGeometry(QtCore.QRect(10, 70, 82, 17))
        self.radioHelp.setObjectName("radioHelp")
        self.radioInfo = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioInfo.setGeometry(QtCore.QRect(10, 100, 82, 17))
        self.radioInfo.setObjectName("radioInfo")
        self.gridLayout.addWidget(self.groupBox_2, 0, 4, 9, 4)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.Favorite = QtWidgets.QPushButton(self.groupBox)
        self.Favorite.setGeometry(QtCore.QRect(0, 13, 151, 23))
        self.Favorite.setObjectName("Favorite")
        self.Begin = QtWidgets.QPushButton(self.groupBox)
        self.Begin.setGeometry(QtCore.QRect(0, 43, 300, 50))
        self.Begin.setMinimumSize(QtCore.QSize(0, 50))
        self.Begin.setObjectName("Begin")
        self.Foto_Rate = QtWidgets.QPushButton(self.groupBox)
        self.Foto_Rate.setGeometry(QtCore.QRect(0, 101, 151, 23))
        self.Foto_Rate.setObjectName("Foto_Rate")
        self.UpdBU_btn = QtWidgets.QPushButton(self.groupBox)
        self.UpdBU_btn.setGeometry(QtCore.QRect(150, 101, 151, 23))
        self.UpdBU_btn.setObjectName("UpdBU_btn")
        self.Fotorate_folder_btn = QtWidgets.QPushButton(self.groupBox)
        self.Fotorate_folder_btn.setGeometry(QtCore.QRect(150, 13, 151, 23))
        self.Fotorate_folder_btn.setObjectName("Fotorate_folder_btn")
        self.sep_fol_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.sep_fol_checkBox.setGeometry(QtCore.QRect(189, 129, 81, 17))
        self.sep_fol_checkBox.setChecked(True)
        self.sep_fol_checkBox.setObjectName("sep_fol_checkBox")
        self.gridLayout.addWidget(self.groupBox, 0, 8, 9, 1)
        self.Zagruzka = QtWidgets.QLabel(Form)
        self.Zagruzka.setText("")
        self.Zagruzka.setObjectName("Zagruzka")
        self.gridLayout.addWidget(self.Zagruzka, 8, 1, 1, 3)
        self.lineEditLogin = QtWidgets.QLineEdit(Form)
        self.lineEditLogin.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEditLogin.setText("")
        # self.lineEditLogin.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEditLogin.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEditLogin.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEditLogin.setClearButtonEnabled(True)
        self.lineEditLogin.setObjectName("lineEditLogin")
        self.gridLayout.addWidget(self.lineEditLogin, 0, 0, 1, 2)
        self.lineEditPass = QtWidgets.QLineEdit(Form)
        self.lineEditPass.setInputMask("")
        self.lineEditPass.setText("")
        self.lineEditPass.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEditPass.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEditPass.setClearButtonEnabled(True)
        self.lineEditPass.setObjectName("lineEditPass")
        self.gridLayout.addWidget(self.lineEditPass, 1, 0, 1, 2)
        self.Clr_mes = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Clr_mes.sizePolicy().hasHeightForWidth())
        self.Clr_mes.setSizePolicy(sizePolicy)
        self.Clr_mes.setObjectName("Clr_mes")
        self.gridLayout.addWidget(self.Clr_mes, 8, 0, 1, 1)
        self.lineEditUserID = QtWidgets.QLineEdit(Form)
        self.lineEditUserID.setText("")
        self.lineEditUserID.setDragEnabled(True)
        self.lineEditUserID.setPlaceholderText("")
        self.lineEditUserID.setClearButtonEnabled(True)
        self.lineEditUserID.setObjectName("lineEditUserID")
        self.gridLayout.addWidget(self.lineEditUserID, 3, 0, 1, 2)
        self.lineEditDest = QtWidgets.QLineEdit(Form)
        self.lineEditDest.setClearButtonEnabled(True)
        self.lineEditDest.setObjectName("lineEdit")
        self.lineEditDest.setText("")
        self.gridLayout.addWidget(self.lineEditDest, 2, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setText('''Доброго времени суток!\
        \nПрограмма PIPS предназначена для экономии времени, здоровья и для\
        \nудобства просмотра фото на сайте ...
        \n1) Введите в первое сверху поле свой логин с сайта ...\
        \n2) Введите во второе сверху поле свой пароль с сайта ...\
        \n3) Нажмите на кружок "База" - это сохранит ваш логин/пароль в базе \
        \n4) Третье поле (Папка загрузки) рекомендуется не трогать (кроме случаев, когда у вас на компьютере НЕТ диска D)
        \nТеперь вы можете или скачать фото из фоторейтинга (кнопка "Скачать\
        \nФоторейтинг") или скачать фото интересующего вас пользователя \
        \n(вводите в самое нижнее поле ID польователя (не путать с его ником) \
        \nи нажимаете Enter на клавиатуре, или кнопку "Скачать" мышкой в программе).
        \nВот и всё. Остальной функционал и тонкости работы программы вы можете прочитать на сайте ... в разделе "о программе"''')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.textEdit.setMaximumSize(QtCore.QSize(405, 2000))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 10, 0, 1, 8)
        self.label_6 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(300, 300))
        self.label_6.setMaximumSize(QtCore.QSize(3000, 3000))
        self.label_6.setAutoFillBackground(False)
        self.label_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/images/Logo32.jpg"))
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setContentsMargins(0, 0, 0, 0)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 10, 8, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "P_info_pic_saver"))
        self.Sh_pic.setToolTip(_translate("Form", "Показывать фото во время загрузки"))
        self.Sh_pic.setText(_translate("Form", "Показ фото"))
        self.radioStandard.setToolTip(_translate("Form", "Обычный вывод"))
        self.radioStandard.setText(_translate("Form", "Стандарт"))
        self.radio_print_user_base.setToolTip(_translate("Form", "Показать базу пользователей"))
        self.radio_print_user_base.setText(_translate("Form", "База"))
        self.radioHelp.setToolTip(_translate("Form", "Информация для желающих помочь/отблагодарить"))
        self.radioHelp.setText(_translate("Form", "Помощь"))
        self.radioInfo.setToolTip(_translate("Form", "информация об авторе и программе"))
        self.radioInfo.setText(_translate("Form", "Инфо"))
        self.Favorite.setToolTip(_translate("Form", "Скачать новые фото фаворитов"))
        self.Favorite.setText(_translate("Form", "Скачать фаворитов"))
        self.Begin.setToolTip(_translate("Form", "Начать загрузку фото"))
        self.Begin.setText(_translate("Form", "Скачать (Enter)"))
        self.Foto_Rate.setToolTip(_translate("Form", "Скачать фото из Фоторейтинга"))
        self.Foto_Rate.setText(_translate("Form", "Скачать Фоторейтинг"))
        self.UpdBU_btn.setToolTip(_translate("Form", "Скачать новые фото пользователей в вашей базе "))
        self.UpdBU_btn.setText(_translate("Form", "Обновить Базу"))
        self.Fotorate_folder_btn.setToolTip(_translate("Form", "Скачать все фото авторов из ПАПКИ фоторейтинга"))
        self.Fotorate_folder_btn.setText(_translate("Form", "Фоторейтинг ПАПКА"))
        self.sep_fol_checkBox.setToolTip(_translate("Form", "Сделать КОПИЮ скачанных фото в отдельной папке"))
        self.sep_fol_checkBox.setText(_translate("Form", "Копия"))
        self.Clr_mes.setToolTip(_translate("Form", "Очистить область сообщений, уведомлений и область фото"))
        self.Clr_mes.setText(_translate("Form", "Очистить"))
        self.label_2.setText(_translate("Form", "Ваш Пароль на P.info"))
        self.label_2.setToolTip(_translate("Form", "Ваш Пароль на сайте P.info"))
        self.label_3.setText(_translate("Form", "ID другого пользователя"))
        self.label_3.setToolTip(_translate("Form", "ID пользователя, чьи фото вы хотите скачать"))
        self.label_4.setText(_translate("Form", "Папка загрузки"))
        self.label_4.setToolTip(_translate("Form", "Папка, куда будут загружены фото и где хранятся базы\nВводить БЕЗ '/' в конце"))
        self.label.setText(_translate("Form", "Ваш Логин на P.info"))
        self.label.setToolTip(_translate("Form", "Ваш Логин на сайте P.info"))
        QtWidgets.QShortcut(QtCore.Qt.Key_Enter, self.Begin, self.Begin.animateClick)
        QtWidgets.QShortcut(QtCore.Qt.Key_Return, self.Begin, self.Begin.animateClick)


        self.Begin.clicked.connect(self.choice)
        self.Clr_mes.clicked.connect(self.clear)
        self.radio_print_user_base.clicked.connect(self.print_user_base)
        self.radioHelp.clicked.connect(self.help_info)
        self.radioInfo.clicked.connect(self.info)
        self.UpdBU_btn.clicked.connect(self.upd_bu)
        self.Foto_Rate.clicked.connect(self.download_fotorating)
        self.Favorite.clicked.connect(self.favor_download)
        self.Fotorate_folder_btn.clicked.connect(self.fotorate_folder)

    def downl_page(self,addr,errmess):
        """ загружает страницу """

        cook=self.get_cookies()

        while True:
            try:
                result=requests.get(addr, cookies=cook)
                return result
            except:
                self.textEdit.append(errmess)
                QCoreApplication.processEvents()
                time.sleep(2)

    def fotorate_folder(self):
        # print ("fotorate_folder")
        """Скачать все фото тех авторов, фото которых находятся в папке фоторейтинга.
        смотрит в папку фоторейтинга за сегодня, ИЗ ФАЙЛОВ собирает ID авторов и отправляет на закачку"""

        self.textEdit.clear()

        dt="!_"+str(time.strftime('%Y')+"_"+time.strftime('%m')+"_"+time.strftime('%d'))
        dest2=str(self.lineEditDest.text())
        dest=dest2+"/"+dt+"_Fotorating"

        # проверка, существует ли папка фоторейтинга
        if os.path.isdir (dest)==False:
            self.textEdit.append("\nНет папки фоторейтинга за сегодня. Сначала скачайте фоторейтинг.")
            return True

        # проверка, есть ли в папке файлы
        list_d=os.listdir(str(dest))
        if list_d==[]:
            self.textEdit.append("\nВ ПАПКЕ фоторейтинга нет фотографий")
            return True

        # сбор уникальных ID пользователей из папки фоторейтинга
        list_of_id=[]
        for i in list_d:
            ii=i.find("-")
            if i[:int(ii)] not in list_of_id:
                list_of_id.append(i[:int(ii)])
        self.textEdit.append("\nВ ПАПКЕ Фоторейтинга найдено "+str(len(list_of_id))+" пользователей.\nНачинаем загрузку новых фото.")
        self.textEdit.append("")

        # отправка этих ID на закачку
        k=1

        for z in list_of_id:
            self.textEdit.append("Загружаются фото "+str(k)+"-го пользователя из "+str(len(list_of_id)))
            QCoreApplication.processEvents()
            self.por_i(z)
            k+=1

        self.textEdit.append("Фотографии пользователей из ПАПКИ Фоторейтинга были загружены!")
        QCoreApplication.processEvents()

    def clear(self):
        """очищает окно сообщений, уведомлений и поле картинки"""
        self.textEdit.clear()
        self.label_6.setPixmap(QtGui.QPixmap(":/images/Logo32.jpg"))
        self.Zagruzka.setText("")

    def user_pass(self):

        """проверяет поля логин и пароль в форме + выводит значение папки назначения"""

        #вывод папки назначения
        self.lineEditDest.setText(Base.get_path_gl())

        #проверка логина-пароля
        log_par=Base.is_lp()
        if str(self.lineEditLogin.text())=="" or str(self.lineEditPass.text())=="":
            if log_par==False:
                # тот случай, когда поля логина пароля пустые и в базе их тоже нет
                self.textEdit.clear()
                self.textEdit.append("\nЗаполните поля Логин и Пароль!")
                self.textEdit.append("\n\nКликните на кружок 'БАЗА' и перезапустите программу")
            else:
                (x,y)=log_par
                self.lineEditLogin.setText(x)
                self.lineEditPass.setText(y)
        else:
            Base.add_lp(self.lineEditLogin.text(),self.lineEditPass.text())

    def print_user_base(self):
        """Выводит на экран алфавитн. список пользователей с количеством фото, общее кол-во пользователей и общее кол-во фото в базе"""

        #отправляет на проверку папки в базе и папки в поле, если не совпадает - то из поля записывает в базу
        Base.add_dir(self.lineEditDest.text())
        self.lineEditDest.setText(Base.get_dir())
        QCoreApplication.processEvents()

        # тот случай, когда на эту кнопку нажали по инструкции из user_pass
        if Base.is_lp()==False:
            self.textEdit.append("\n\nТеперь перезапустите программу!!!")
            self.user_pass()
            return

        # эта инструкция для изменения логина-пароля. Способ: введите новые логин-пароль. После этого нажмите кружок БАЗА.
        self.user_pass()

        dest=str(self.lineEditDest.text())
        self.textEdit.clear()

        dic,user,pic_all=Base.list_usernames()

        if dic=={}:
        	self.textEdit.append("У вас пока нет базы пользователей.\n\nСкачайте фоторейтинг или фото какого-нибудь пользователя.")
        	return

        self.textEdit.append("Список пользоваталей в Базе:\n")

        dic,user,pic_all=Base.list_usernames()
        for i in sorted(dic):
            self.textEdit.append(i+" => "+dic[i]+" фото.")

        self.textEdit.append("\nВ базе "+str(user)+" пользователей. Суммарно "+str(pic_all)+" фотографий.")

    def help_info(self):
        """Выводит сообщение о помощи авторам программы"""

        self.textEdit.clear()
        aa='''Если вам понравилась программа,
        и вы хотите помочь, мы рады.
        '''
        self.textEdit.append(aa)
        QCoreApplication.processEvents()

    def info(self):
        self.textEdit.clear()
        self.textEdit.append("Информация о программе:\n")
        bb="""Тут будет информация о программе и авторе.\nПока что этот функционал не реализован. Ожидайте в будущих версиях программы.
        \nПока что смотрите руководство на сайте ... в разделе "о программе"
        """
        self.textEdit.append(bb)
        QCoreApplication.processEvents()

    def upd_bu(self):
        """Получает список ВСЕХ ID пользователей и отправляет его на закачку"""

        self.textEdit.clear()

        # проверяем, заполнены ли поля логин-пароль
        self.user_pass()

        # получаем из базы список ID пользоателей
        ID_list=Base.list_all_users_ID()

        # проверяем, есть ли пользователи в базе
        if ID_list==[]:
            self.textEdit.append("У вас еще нет пользователей в базе.\nСначала скачайте фото нескольких пользователей.")
            return

        # берем из файла-базы ID пользователей и отправляем их на закачку в por_i
        self.textEdit.append("В базе найдено "+str(len(ID_list))+" пользователей.\nНачинаем загрузку новых фото.")
        k6=1
        for z in ID_list:
            self.textEdit.append("Загружаются фото "+str(k6)+"-го пользователя из "+str(len(ID_list)))
            QCoreApplication.processEvents()
            self.por_i(z)
            k6+=1
        self.textEdit.append("\nФотографии пользователей из базы были обновлены!")
        QCoreApplication.processEvents()

    def eval_cookie_expiration_date(self):
        """Проверяет, не истекла ли дата, до которой действительны куки"""

        import datetime
        import time
        # from time import strftime

        global cookies_gl

        if cookies_gl:
            expires = None
            for cookie in cookies_gl:
                if cookie.name == 'Session':
                    expires = cookie.expires
                    expires -= 3600

            real_time = time.time()
            cookie_time = expires

            if cookie_time > real_time:
                return True

        return False


    def get_cookies_from_site(self):
        # print ("get_cookies_from_site")
        """Получает кукисы с сайта"""

        # проверка логина-пароля, если их нет, то выход
        self.user_pass()
        if Base.is_lp()==False:
            return False

        payload = {
        'f_login': '1',
        'login': str(self.lineEditLogin.text()),
        'pass': str(self.lineEditPass.text())
        }

        head = {
            'Host':'p.info',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:37.0) Gecko/20100101 Firefox/37.0',
            'Referer':'http://p.info/index.php',
            'Connection':'keep-alive'
        }
        # Получаем cookies с сайта
        # Use 'with' to ensure the session context is closed after use.
        with requests.Session() as v:
            while True:
                try:
                    p = v.post('http://p.info/index.php', data=payload, headers=head)
                    por_cookies=v.cookies
                    break
                except:
                    self.textEdit.append("Error: while getting cookies. Retrying...")
                    QCoreApplication.processEvents()
                    time.sleep(2)

        return por_cookies

    def get_cookies(self):
        """получаем кукисы с файла или с сайта"""

        global cookies_gl

        ppp=False

        if cookies_gl:
            ppp=self.eval_cookie_expiration_date()
            if ppp:
                return cookies_gl

        cookies_gl=self.get_cookies_from_site()
        return cookies_gl


    def get_pic_id_name_lists(self, s):
        # print ("get_pic_id_name_lists")
        """вытаскиваем из страницы фоторейтинга 3 списка: список ID фоток, список id авторов, список имен авторов.
        перед внесением в список фотки ПРОВЕРЯЮТСЯ на наличие в общей базе."""

        self.textEdit.append("Сравниваем фоторейтинг с базами...")
        QCoreApplication.processEvents()

        n=1
        pic_list=[]
        spisok_u_id=[]
        spisok_u_name=[]

        while n < len(s):
            n=s.find ("view.php?item=",int(n))
            m=s.find ('"',int (n))
            if n==-1:
                break
            s[int(n):int(m)]
            ph_id=s[int(n+14):int(m)]
            if ph_id not in pic_list:
                u=s.find ("usernick",int(n))
                u2=s.find ("user&id=",int(u))
                u3=s.find ('"',int(u2+8))
                u_id=s[int(u2+8):int(u3)]
                u4=s.find ("blank",int(u3))
                u4=int(u4)+7
                while True:
                    if s[int(u4):int(u4+1)]=="<":
                        u4=int(s.find(">",int(u4)))+1
                    else:
                        break
                u5=s.find ("<",int(u4))
                u_nick=s[int(u4):int(u5)]
                u_nick=u_nick.lower()

                # проверка по общей базе программы, если в общей базе нет - то добавляем в списки
                if Base.if_pics(u_id, ph_id)==False:
                    pic_list.append(ph_id)
                    spisok_u_id.append(u_id)
                    spisok_u_name.append(u_nick)
            n=m

        return pic_list, spisok_u_id, spisok_u_name

    def download_pic(self, ph_id, file_name, folder_name, copy_folder_name="",if_list=()):
        # print ("download_pic")
        """ Получает ID фото, имя для сохранения файла и имя папки - куда сохранять.
            Скачивает фото с данным ID. Сохраняет его с указанным именем в указанной папке.
            Папку при необходимости создает."""

        # делаем имена строковыми
        file_name=str(file_name)
        folder_name=str(folder_name)

        pp=False

        # проверяем наличие папки КУДА скачивать, если нет - то создаем папку.
        if os.path.isdir (folder_name)==False:
            os.makedirs (folder_name)
            self.textEdit.append("\nПапка "+folder_name+" создана.\n")

        # проверяем наличие папки КУДА скачивать КОПИИ, если нет - то создаем папку.
        if copy_folder_name and not os.path.isdir(copy_folder_name) and self.sep_fol_checkBox.isChecked():
            os.makedirs (copy_folder_name)
            self.textEdit.append('Создана папка: '+copy_folder_name)
            QCoreApplication.processEvents()

        # скачиваем страницу с фото
        addr='http://p.info'+'/'+'view.php?item='+ph_id
        errmess="Error getting page for "+str(ph_id)+". Retrying..."
        page=self.downl_page(addr,errmess)

        # на странице находим ссылку на фото - pic_link
        s2=page.text
        # n=s2.find ('p.info/pics.php',1) это было изначально

        try:
            n=s2.rindex('p.info/pics.php')
        except:
            n=-1
        if n!=-1:
            if s2[n-2:n]=="s.":
                n=n-2

        if n==-1:
            n=s2.find ('/pic.php?id='+ph_id)
            # print ('Ссылка 2 типа')
            pp=True
            if n==-1:
                self.textEdit.append("\nНа странице нет фотографии с ID "+str(ph_id)+".")
                QCoreApplication.processEvents()
                return False
        m=s2.find (')',int(n+5))
        m2=s2.find ('"',int(n+5))
        if m2<m:
            m=m2
        pic_link=s2[int(n):int(m)]
        if pp:
            pic_link='p.info'+'/'+'pic.php?id='+ph_id

        if if_list:
            self.Zagruzka.setText("Загружается "+if_list[0]+" из "+if_list[1]+" файлов")
            QCoreApplication.processEvents()

        # скачиваем фото и сохраняем на диск
        addr='http:'+'/'+'/'+pic_link
        errmess="Error getting pic "+str(ph_id)+". Retrying..."
        pic=self.downl_page(addr,errmess)

        file=open (folder_name+'/'+file_name+'.jpg', "wb")
        file.write(pic.content)
        file.close()
        self.textEdit.append("Файл "+file_name+" сохранен.")

        if self.sep_fol_checkBox.isChecked():
            file=open (copy_folder_name+'/'+file_name+'.jpg', "wb")
            file.write(pic.content)
            file.close()

        # вывод скачанного изображения на экран
        if self.Sh_pic.isChecked():
            self.label_6.setPixmap(QtGui.QPixmap(folder_name+'/'+file_name+'.jpg').scaled(self.label_6.width(),self.label_6.height(),QtCore.Qt.KeepAspectRatio))
        QCoreApplication.processEvents()

        # не трогать TRUE - он используется при посылании с фоторейтинга
        return True

    def download_fotorating(self):
        # print ("download_fotorating")
        """ Скачиваем все фото из фоторейтинга, проверив их на наличие в базе"""

        # проверка логина-пароля, если их нет, то выход
        self.user_pass()
        if Base.is_lp()==False:
            return

        dest=str(self.lineEditDest.text())
        folder_name=dest+'/'+"!_"+str(time.strftime('%Y')+"_"+time.strftime('%m')+"_"+time.strftime('%d')+"_Fotorating")

        # проверяем, есть ли папка DEST, если нет - создаем
        if os.path.isdir (dest)==False:
            os.makedirs (dest)

        self.textEdit.clear()
        self.textEdit.append("Просматриваем страницу фоторейтинга...\n")
        QCoreApplication.processEvents()

        # скачиваем страницу фоторейтинга
        addr='http://p.info/index.php?action=fotorate'
        errmess="Error getting FotoRate page. Retrying..."
        r=self.downl_page(addr,errmess)
        s=r.text

        # получаем 3 списка из страницы фоторейтинга (уже проверенные на наличие в базах)
        pic_list, spisok_u_id, spisok_u_name = self.get_pic_id_name_lists(s)

        if len(pic_list)==0:
            self.textEdit.append("\nВсе фото, что на данный момент находятся в фоторейтиге, у вас уже есть. (В папках пользователей или в предыдущих фоторейтингах)")
            QCoreApplication.processEvents()
            return

        self.textEdit.append("\nНачинаем загрузку фотографий...")
        QCoreApplication.processEvents()

        # отправляем id фото по одному на закачку, формируя имя
        kk=0

        for i in pic_list:

            if Base.if_userid_in_BL(spisok_u_id[kk])==True:
                self.textEdit.append("Пользователь "+str(spisok_u_name[kk])+", id: "+str(spisok_u_id[kk])+" в блэклисте!!!")
                QCoreApplication.processEvents()
                kk+=1
                continue

            self.Zagruzka.setText("Загружается "+str(kk+1)+" из "+str(len(pic_list))+" файлов")
            QCoreApplication.processEvents()

            # формируем правильное имя файла
            file_name=str(spisok_u_id[kk])+"--"+str(spisok_u_name[kk])+"--"+str(pic_list[kk])

            # добываем имя для сохранения фото в папку юзера
            copy_folder_name=self.get_folder_name(spisok_u_name[kk])

            # скачиваем фото
            res=self.download_pic(pic_list[kk], file_name, folder_name, copy_folder_name)

            # если файл был скачан, то добавляем запись о файле в базу фоторейтинга и общую базу
            if res:
                # запись в общую базу
                Base.add_user_and_pics_to_base(spisok_u_id[kk], spisok_u_name[kk], pic_list[kk])

            kk+=1

        self.textEdit.append("\nФоторейтинг загружен!")
        self.Zagruzka.setText("")
        QCoreApplication.processEvents()

    def thumb_page_to_many_big_pages(self, a):
        # print ("thumb_page_to_many_big_pages")
        """функция получает содержимое страницы с 40 миниатюрами, например
        r = requests.get('http://p.info/index.php?action=photos&filter=user&id='+userid+'&album=all', cookies=pk)
        lf=r.text
        отдает список со ссылками на 40 страниц с большими фотками"""

        n=1
        spisok=[]
        while n < len(a):
            n=a.find ("view.php?item=",int(n))
            m=a.find ('"',int (n))
            if n==-1:
                break
            if a[int(n):int(m)] not in spisok:
                spisok.append(a[int(n+14):int(m)])
            n=m
        return spisok

    def get_folder_name(self, u_name):
        """формирует правильное имя папки, исходя из имени пользователя"""

        dest=str(self.lineEditDest.text())
        u_name=u_name.lower()

        dic={
        "a":"!_A",
        "b":"!_BC",
        "c":"!_BC",
        "d":"!_DE",
        "e":"!_DE",
        "f":"!_FGH",
        "g":"!_FGH",
        "h":"!_FGH",
        "i":"!_IJ",
        "j":"!_IJ",
        "k":"!_K",
        "l":"!_L",
        "m":"!_M",
        "n":"!_NO",
        "o":"!_NO",
        "p":"!_P",
        "q":"!_QR",
        "r":"!_QR",
        "s":"!_S",
        "t":"!_TU",
        "u":"!_TU",
        "v":"!_VW",
        "w":"!_VW",
        "x":"!_XYZ",
        "y":"!_XYZ",
        "z":"!_XYZ"
        }

        try:
            folder=dic[u_name[0]]
        except:
            folder="!_0-9"

        folder_name=dest+'/'+folder+'/'+u_name

        return folder_name

    def download_list(self, final_list, dest, nick, userid, number_of_pics):
        # print ("download_list")
        """эта функция получает список ссылок на страницы с большими фотками, и destination (куда сохранять)
        скачивает фотки и сохраняет их на диск"""

        dt=time.strftime('%Y')+"_"+time.strftime('%m')+"_"+time.strftime('%d')

        dest=str(self.lineEditDest.text())

        folder_name=self.get_folder_name(nick)
        copy_folder_name=dest+'/'+"!_"+dt+"_New_in_Base"

        self.textEdit.append('Начинаем загрузку '+str(len(final_list))+' файлов')
        QCoreApplication.processEvents()

        m1=1
        for i in final_list:
            ph_id=i
            if_list=(str(m1),str(len(final_list)))
            file_name=userid+"--"+nick+"--"+i

            self.download_pic(ph_id, file_name, folder_name, copy_folder_name,if_list)
            m1=m1+1

        pk=self.get_cookies()

        payload2 = {
            'mod': 'edit_note',
            'userid': userid,
            'value': str(number_of_pics)+"-p",
            'id':'user_note_text'
        }
        head3 = {
            'Host':'p.info',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:37.0) Gecko/20100101 Firefox/37.0',
            'X-Requested-With':'XMLHttpRequest',
            'Referer':'http://p.info/index.php?action=user&id='+userid,
            'Connection':'keep-alive'
        }
        while True:
            try:
                requests.post('http://p.info/ajaxdata.php?mod=edit_note&userid='+userid, cookies=pk, data=payload2, headers=head3)
                break
            except:
                self.textEdit.append("Error: writing a user_note. Retrying...")
                QCoreApplication.processEvents()
                time.sleep(2)

        return final_list

    def base_check_of_piclist(self, pic_list, u_id):
        # print ("base_check_of_piclist")
        """ функция принимает список файлов ОДНОГО пользователя.
            сравниваем список с базой,
            удаляем из списка то, что в базе есть.
            функция возвращает список."""

        pic_list_final=[]

        # проверяем, есть ли такой пользователь в базе,
        # если пользователя нет - то возвращаем оригинальный список
        if Base.if_userid_in_users(str(u_id))==False:
            return (pic_list)
        # если пользователь есть, то получаем список его фото из базы
        else:
            base_list=Base.get_all_pics_from_user(u_id)

        # от изначального списка отнимаем список базы
        final_list=list(set(pic_list) - set(base_list))

        # возвращаем то, что осталось
        return final_list

    def profile_parsing_name_and_number_of_pages(self, userid, profile):
        # print ("profile_parsing_name_and_number_of_pages")
        """парсим страницу профайла пользователя:
            добываем user_nick и его количество страниц с миниатюрами
            и общее количество фотографий пользователя"""

        # ищем ник пользователя = nick
        n1=profile.find('data-nick="')
        n2=profile.find('"',int(n1+11))
        nick=profile[int(n1+11):int(n2)]
        nick=str(nick.lower())

        # ищем общее количество фоток = number_of_pics
        number_of_pics=0
        n=profile.find (userid+'&album=all')
        if n==-1:
            self.textEdit.append("Ошибка! У пользователя "+nick+" нет фотографий")
            QCoreApplication.processEvents()
        else:
            m=profile.find("(",int(n))
            p=profile.find(" ",m)
            number_of_pics=int(profile[int(m+1):int(p)])

        # вычисляем количество страниц с миниатютами = number_of_pages
        if number_of_pics <= 40: number_of_pages=1
        s=number_of_pics%40
        if s==0: number_of_pages=number_of_pics/40
        if s>0: number_of_pages=(number_of_pics//40)+1

        return nick, number_of_pages, number_of_pics

    def por_i(self, user_id):
        # print ("por_i")
        """Загружает все новые фото пользователя по USER_ID, проверив по базам какие уже скачаны, а какие надо качать"""

        # проверка логина-пароля, если их нет, то выход
        self.user_pass()
        if Base.is_lp()==False:
            return

        # если нас послали в эту функцию с ID польз., то используем его,
        # если послали без ID польз., то берем из поля формы,
        # если в поле формы тоже пусто - то выход

        if not user_id:
            if str(self.lineEditUserID.text())=="":
                self.textEdit.append("Введите ID пользователя")
                QCoreApplication.processEvents()
                return
            userid=str(self.lineEditUserID.text())
        else:
            userid=user_id

        # очищаем поле формы
        self.lineEditUserID.setText("")

        # ПРОВЕРКА НА BLACKLIST
        if Base.if_userid_in_BL(userid)==True:
            username=str(Base.get_name_from_id(userid))
            self.textEdit.append("Пользователь "+username+", id: "+str(userid)+" в блэклисте!!!")
            QCoreApplication.processEvents()
            return

        dest=str(self.lineEditDest.text())
        log1=str(self.lineEditLogin.text())
        pas1=str(self.lineEditPass.text())

        # Получаем страницу пользователя
        addr='http://p.info/index.php?action=user&id='+userid
        errmess="Error: scanning profile. Retrying..."
        r2=self.downl_page(addr,errmess)
        profile=r2.text

        # отправляем страницу на парсинг
        nick, number_of_pages, number_of_pics=self.profile_parsing_name_and_number_of_pages(userid, profile)

        # скачиваем страницы с миниатюрами,
        # отправляем на функцию thumb_page_to_many_big_pages,
        # ответы собираем в единый список = pic_list
        i=1
        pic_list=[]
        while i <= number_of_pages:
            # скачиваем страницы с миниатюрами
            addr='http:'+'/'+'/'+'p.info/index.php?action=photos&p='+str(i)+'&filter=user&id='+userid+'&album=all'
            errmess="Error: collecting links from thumbnails. Retrying..."
            result=self.downl_page(addr,errmess)

            page=result.text
            pic_list.extend(self.thumb_page_to_many_big_pages(page))
            i+=1

        # удаляем из списка то, что уже есть в базе
        final_list=self.base_check_of_piclist(pic_list,userid)

        # если финальный список > 0, то отправляем его на закачку
        # и потом отправляем список на внесение в базу
        list_of_downloaded_pics=[]
        if len(final_list)>0:
            list_of_downloaded_pics=self.download_list(final_list,dest,nick,userid,number_of_pics)
            Base.add_user_and_pics_to_base(userid, nick, list_of_downloaded_pics)

        # выводим текстовые сообщения о количестве файлов на диске и количестве скачанных файлов
        list_of_files=[]
        folder_name=self.get_folder_name(nick)
        if os.path.isdir (folder_name): list_of_files=os.listdir(folder_name)
        self.textEdit.append('\nВ папке находится '+str(len(list_of_files))+' файлов')
        self.textEdit.append("Done! Было загружено "+str(len(list_of_downloaded_pics))+" файлов пользователя "+nick+"\n")
        self.Zagruzka.setText("Готово!")
        QCoreApplication.processEvents()

# блок функций для работы с блэклистом

    def bl_info(self):
        """Выводит справочную Информацию по блэклисту"""

        self.textEdit.append("""Для добавления пользователя в блэклист, введите b+ XXXXXX, где XXXXXX - ID пользователя и нажмите Enter (или кнопку 'Скачать')\
            \nДля удаления пользователя из блэклиста, введите b- XXXXXX, где XXXXXX - ID пользователя и нажмите Enter (или кнопку 'Скачать')\
            \nФотографии пользователя в блэклисте не будут скачиваться программой, пока вы не удалите пользователя из блэклиста.\n""")

    def bl_show(self):
        """Показывает блэклист"""

        self.textEdit.append("На данный момент ваш блэклист содержит следующих пользователей:\n")
        QCoreApplication.processEvents()

        dic=Base.get_blacklist()

        for i in sorted(dic):
            self.textEdit.append("ID: "+dic[i]+" ----- UserName: "+i)
        self.textEdit.append("")

    def bl_add(self, u_id):
        """ Добавляет пользователя в Блэклист.
            Выводит соотв. сообщения"""

        # очищаем поля сообщений и уведомлений
        self.textEdit.clear()
        self.Zagruzka.clear()
        QCoreApplication.processEvents()

        # получаем имя пользователя из базы
        u_name=Base.get_name_from_id(u_id)

        # проверка, есть ли такой пользователь в базе, если нет - выход
        if not u_name:
            self.textEdit.append("\nВ базе нет пользователя с id: "+u_id+"\n Попробуйте снова.")
            QCoreApplication.processEvents()
            return

        Base.add_to_blacklist(u_id)
        self.textEdit.append("Пользователь "+u_name+" добавлен в блэклист.")
        QCoreApplication.processEvents()

        self.bl_show()
        self.bl_info()
        self.favor_info()

    def bl_del(self, u_id):
        """ Удаляет пользователя из блэклиста.
            Выводит соотв. сообщения"""

        # очищаем поля сообщений и уведомлений
        self.textEdit.clear()
        self.Zagruzka.clear()
        QCoreApplication.processEvents()

        # получаем имя пользователя из базы
        u_name=Base.get_name_from_id(u_id)

        # проверка, есть ли такой пользователь в базе, если нет - выход
        if not u_name:
            self.textEdit.append("\nВ базе нет пользователя с id: "+u_id+"\nПопробуйте снова.")
            QCoreApplication.processEvents()
            return

        Base.remove_from_blacklist(u_id)
        self.textEdit.append("Пользователь "+u_name+" удален из блэклиста.")
        QCoreApplication.processEvents()

        self.bl_show()
        self.bl_info()
        self.favor_info()

# блок функций для работы с листом фаворитов

    def favor_info(self):
        """Выводит справочную Информацию по фаворитам"""

        self.textEdit.append("""Фавориты - список любимых авторов.\nДля добавления пользователя в фавориты, введите f+ XXXXXX, где XXXXXX - ID пользователя, и нажмите Enter (или кнопку 'Скачать')\
            \nДля удаления пользователя из фаворитов: Введите f- XXXXXX, где XXXXXX - ID пользователя и нажмите Enter (или кнопку 'Скачать'). Все новые фотографии всех фаворитов можно скачать одной кнопкой.\n""")

    def favor_show(self):
        """Показывает фаворитов"""

        self.textEdit.append("На данный момент у вас в фаворитах следующие пользователи:\n")
        QCoreApplication.processEvents()

        dic=Base.get_favorlist()

        for i in sorted(dic):
            self.textEdit.append("ID: "+dic[i]+" ----- UserName: "+i)
        self.textEdit.append("")

    def favor_add(self, u_id):
        """ Добавляет пользователя в фавориты.
            Выводит соотв. сообщения"""

        # очищаем поля сообщений и уведомлений
        self.textEdit.clear()
        self.Zagruzka.clear()
        QCoreApplication.processEvents()

        # получаем имя пользователя из базы
        u_name=Base.get_name_from_id(u_id)

        # проверка, есть ли такой пользователь в базе, если нет - выход
        if not u_name:
            self.textEdit.append("\nВ базе нет пользователя с id: "+u_id+"\n Попробуйте снова.")
            QCoreApplication.processEvents()
            return

        Base.add_to_favorlist(u_id)
        self.textEdit.append("Пользователь "+u_name+" добавлен в фавориты.")
        QCoreApplication.processEvents()

        self.favor_show()
        self.favor_info()
        self.bl_info()

    def favor_del(self, u_id):
        """ Удаляет пользователя из фаворитов.
            Выводит соотв. сообщения"""

        # очищаем поля сообщений и уведомлений
        self.textEdit.clear()
        self.Zagruzka.clear()
        QCoreApplication.processEvents()

        # получаем имя пользователя из базы
        u_name=Base.get_name_from_id(u_id)

        # проверка, есть ли такой пользователь в базе, если нет - выход
        if not u_name:
            self.textEdit.append("\nВ базе нет пользователя с id: "+u_id+"\n Попробуйте снова.")
            QCoreApplication.processEvents()
            return

        Base.remove_from_favorlist(u_id)
        self.textEdit.append("Пользователь "+u_name+" удален из фаворитов.")
        QCoreApplication.processEvents()

        self.favor_show()
        self.favor_info()
        self.bl_info()

    def favor_download(self):
        """Загружает все фотки всех фаворитов"""

        self.textEdit.clear()
        self.textEdit.append("Загружаем все новые фото фаворитов:\n")
        QCoreApplication.processEvents()

        dic=Base.get_favorlist()

        for i in dic:
            self.textEdit.append("Загружаем фото пользователя "+i)
            QCoreApplication.processEvents()
            self.por_i(dic[i])
        self.textEdit.append("Все новые фото фаворитов загружены")

        pass


    def choice(self):
        """анализирует, что было введено в поле 'ID другого пользователя',
        запускает соответствующий модуль"""

        vvod=str(self.lineEditUserID.text())
        vvod=vvod.lower().strip()

        if vvod.isdigit():
            self.por_i(vvod)

        elif vvod==("f"):
            self.textEdit.clear()
            self.favor_show()
            self.favor_info()
            self.bl_info()

        elif vvod.startswith("f+"):
            vvod=vvod[2:].strip()
            self.favor_add(vvod)

        elif vvod.startswith("f-"):
            vvod=vvod[2:].strip()
            self.favor_del(vvod)

        elif vvod==("b"):
            self.textEdit.clear()
            self.bl_show()
            self.bl_info()
            self.favor_info()

        elif vvod.startswith("b+"):
            vvod=vvod[2:].strip()
            self.bl_add(vvod)

        elif vvod.startswith("b-"):
            vvod=vvod[2:].strip()
            self.bl_del(vvod)

        elif vvod=="fd":
            self.favor_download()

        else:
            self.textEdit.clear()
            self.textEdit.append("\nНеверный ввод. Попробуйте снова.")
        return

if __name__ == '__main__':
    Base.start_base()
    app = QApplication(sys.argv)
    form = Ui_Form()
    Ui_Form.user_pass(form)
    form.show()
    sys.exit(app.exec_())


