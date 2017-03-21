# coding: utf-8
# © LeoGSA - Sergey Grigoriev (leogsa@gmail.com)

import sys, os, time, requests, datetime
import re

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QCoreApplication, QTimer
from PyQt5.QtWidgets import QShortcut

from base import *
from pips3_interface7 import Ui_Form

cookies_gl = {}
timer_seconds = 1200
timer_seconds_etalon = 1200

class MyWindow(Ui_Form):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.download_enter_btn.clicked.connect(self.choice)
        self.clear_btn.clicked.connect(self.clear)
        self.base_radio_btn.clicked.connect(self.print_user_base)
        self.help_radio_btn.clicked.connect(self.help_info)
        self.info_radio_btn.clicked.connect(self.info)
        self.upate_base_btn.clicked.connect(self.upd_bu)
        self.downl_fotorating_btn.clicked.connect(self.download_fotorating)
        self.downl_favor_btn.clicked.connect(self.favor_download)
        self.fotorate_folder_btn.clicked.connect(self.fotorate_folder)
        QtWidgets.QShortcut(QtCore.Qt.Key_Enter, self.download_enter_btn, self.download_enter_btn.animateClick)
        QtWidgets.QShortcut(QtCore.Qt.Key_Return, self.download_enter_btn, self.download_enter_btn.animateClick)

    def timeit(method):
        """функция для замера времени выполнения других функций"""

        def timed(*args, **kw):
            ts = time.time()
            result = method(*args, **kw)
            te = time.time()

            print ('%r, %2.2f sec' % (method.__name__, te-ts))
            return result

        return timed

    def dis_buttons(self):
        self.downl_fotorating_btn.setEnabled(False)
        self.downl_favor_btn.setEnabled(False)
        self.fotorate_folder_btn.setEnabled(False)
        self.download_enter_btn.setEnabled(False)
        self.upate_base_btn.setEnabled(False)
        self.base_radio_btn.setEnabled(False)
        self.help_radio_btn.setEnabled(False)
        self.info_radio_btn.setEnabled(False)

    def en_buttons(self):
        self.downl_fotorating_btn.setEnabled(True)
        self.downl_favor_btn.setEnabled(True)
        self.fotorate_folder_btn.setEnabled(True)
        self.download_enter_btn.setEnabled(True)
        self.upate_base_btn.setEnabled(True)
        self.base_radio_btn.setEnabled(True)
        self.help_radio_btn.setEnabled(True)
        self.info_radio_btn.setEnabled(True)

    # @timeit
    def downl_page(self, addr, errmess):
        """ загружает страницу """

        cook = self.get_cookies()

        while True:
            try:
                result = requests.get(addr, cookies=cook)
                return result
            except:
                self.main_text_window.append(errmess)
                QCoreApplication.processEvents()
                time.sleep(2)

    # @timeit
    def fotorate_folder(self):
        """Скачать все фото тех авторов, фото которых находятся в папке фоторейтинга.
        смотрит в папку фоторейтинга за сегодня, ИЗ ФАЙЛОВ собирает ID авторов и отправляет на закачку"""

        self.main_text_window.clear()
        self.dis_buttons()

        # формируем имена папок, основываясь на датах
        dt = "!_"+str(time.strftime('%Y')+"_"+time.strftime('%m')+"_"+time.strftime('%d'))
        dest2 = str(self.download_folder_edit_line.text())
        dest = dest2+"/"+dt+"_Fotorating"

        # проверка, существует ли папка фоторейтинга
        if os.path.isdir (dest) == False:
            self.main_text_window.append("\nНет папки фоторейтинга за сегодня. Сначала скачайте фоторейтинг.")
            self.en_buttons()
            return

        # проверка, есть ли в папке файлы
        list_d = os.listdir(str(dest))
        if list_d == []:
            self.main_text_window.append("\nВ ПАПКЕ фоторейтинга нет фотографий")
            self.en_buttons()
            return

        # сбор уникальных ID пользователей из папки фоторейтинга
        list_of_id = []
        for i in list_d:
            user_id = i.split('--')[0]
            if user_id not in list_of_id:
                list_of_id.append(user_id)
        self.main_text_window.append("\nВ ПАПКЕ Фоторейтинга найдено "+str(len(list_of_id))+" пользователей.\nНачинаем загрузку новых фото.")
        self.main_text_window.append("")

        # отправка этих ID на закачку
        for a, b in enumerate(list_of_id):
            self.main_text_window.append("Загружаются фото "+str(a+1)+"-го пользователя из "+str(len(list_of_id)))
            QCoreApplication.processEvents()
            self.por_i(b)

        os.rename(dest, dest+"--")

        self.main_text_window.append("Фотографии пользователей из ПАПКИ Фоторейтинга были загружены!\nПапка фоторейтинга переименована.")
        self.en_buttons()
        QCoreApplication.processEvents()

    def clear(self):
        """очищает окно сообщений, уведомлений и поле картинки"""

        self.main_text_window.clear()
        self.main_pic_window.setPixmap(QtGui.QPixmap(":/images/Logo32.jpg"))
        self.small_text_line.setText("")

    # @timeit
    def user_pass(self):
        """проверяет поля логин и пароль в форме + выводит значение папки назначения"""

        #вывод папки назначения
        self.download_folder_edit_line.setText(Base.get_path_gl())

        #проверка логина-пароля
        log_par = Base.is_lp()
        if str(self.login_edit_line.text()) == "" or str(self.password_edit_line.text()) == "":
            if log_par == False:
                # тот случай, когда поля логина пароля пустые и в базе их тоже нет
                self.main_text_window.clear()
                self.main_text_window.append("\nЗаполните поля Логин и Пароль!")
                self.main_text_window.append("\n\nКликните на кружок 'БАЗА' и перезапустите программу")
                return
            else:
                (x,y) = log_par
                self.login_edit_line.setText(x)
                self.password_edit_line.setText(y)
        else:
            Base.add_lp(self.login_edit_line.text(), self.password_edit_line.text())

    # @timeit
    def print_user_base(self):
        """Выводит на экран алфавитн. список пользователей с количеством фото, общее кол-во пользователей и общее кол-во фото в базе"""

        #отправляет на проверку папки в базе и папки в поле, если не совпадает - то из поля записывает в базу
        Base.add_dir(self.download_folder_edit_line.text())
        self.download_folder_edit_line.setText(Base.get_dir())
        QCoreApplication.processEvents()

        # тот случай, когда на эту кнопку нажали по инструкции из user_pass
        if Base.is_lp() == False:
            self.main_text_window.append("\n\nТеперь перезапустите программу!!!")
            self.user_pass()
            return

        # эта инструкция для изменения логина-пароля. Способ: введите новые логин-пароль. После этого нажмите кружок БАЗА.
        self.user_pass()

        self.dis_buttons()
        QCoreApplication.processEvents()

        self.main_text_window.clear()

        dic, user, pic_all = Base.list_usernames()

        if dic == {}:
            self.main_text_window.append("У вас пока нет базы пользователей.\n\nСкачайте фоторейтинг или фото какого-нибудь пользователя.")
            self.en_buttons()
            return

        self.main_text_window.append("Список пользоваталей в Базе:\n")

        for i in sorted(dic):
            self.main_text_window.append(i+" => "+dic[i]+" фото.")

        self.en_buttons()
        self.main_text_window.append("\nВ базе "+str(user)+" пользователей. Суммарно "+str(pic_all)+" фотографий.")

    def help_info(self):
        """Выводит сообщение о помощи авторам программы"""

        self.main_text_window.clear()
        aa = '''Если вам понравилась программа, и вы хотите отблагодарить авторов,\
        \nили хотите помочь им с выпуском новых более функциональных версий, вы можете перечислить деньги на счета Webmoney:\
        \n\n Z290589591532 - доллары США\
        \n R312162815961 - рубли России\
        \n U127679426502 - гривны Украины\
        \n E557466583200 - Евро\
        \n\n Рекомендуемая сумма: 5$-20$\
        \n После отправки помощи напишите нам на e-mail:\
        \n                       pips@saveall.info
        \nВ письме укажите кошелек или терминал, с которого вы оказали помощь,\
        \nсвой логин на сайте, и вы получите именную версию программы. (в ней \
        \nуже не нужно будет вводить логин, и будут убраны тестовые ограничения на 80 фото.)\
        \nПАРОЛЬ ПРИСЫЛАТЬ НЕ НУЖНО (его вы будете сами вводить в полученной программе)\
        \nПо всем остальным вопросам также обращайтесь на e-mail:\
        \n                       pips@saveall.info
        '''
        self.main_text_window.append(aa)
        QCoreApplication.processEvents()

    def info(self):
        self.main_text_window.clear()
        self.main_text_window.append("Информация о программе:\n")
        bb = """Тут будет информация о программе и авторе.\nПока что этот функционал не реализован. Ожидайте в будущих версиях программы.
        \nПока что смотрите руководство на сайте pips.saveall.info в разделе "о программе"
        """
        self.main_text_window.append(bb)
        QCoreApplication.processEvents()

    def upd_bu(self):
        """Получает список ВСЕХ ID пользователей и отправляет его на закачку"""

        self.main_text_window.clear()
        self.dis_buttons()

        # проверяем, заполнены ли поля логин-пароль
        # self.user_pass()

        # получаем из базы список ID пользоателей
        ID_list = Base.list_all_users_ID()

        # проверяем, есть ли пользователи в базе
        if ID_list == []:
            self.main_text_window.append("У вас еще нет пользователей в базе.\nСначала скачайте фото нескольких пользователей.")
            self.en_buttons()
            return

        self.main_text_window.append("В базе найдено "+str(len(ID_list))+" пользователей.\nНачинаем загрузку новых фото.")

        # берем из файла-базы ID пользователей и отправляем их на закачку в por_i
        for a, user_id in enumerate(ID_list):
            self.main_text_window.append("Загружаются фото "+str(a+1)+"-го пользователя из "+str(len(ID_list)))
            QCoreApplication.processEvents()
            self.por_i(user_id)

        self.main_text_window.append("\nФотографии пользователей из базы были обновлены!")
        self.en_buttons()
        QCoreApplication.processEvents()

    # @timeit
    def eval_cookie_expiration_date(self):
        """Проверяет, не истекла ли дата, до которой действительны куки"""

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

    # @timeit
    def get_cookies_from_site(self):
        """Получает кукисы с сайта"""

        # проверка логина-пароля, если их нет, то выход
        self.user_pass()
        if Base.is_lp() == False:
            return False

        payload = {
        'f_login': '1',
        'login': str(self.login_edit_line.text()),
        'pass': str(self.password_edit_line.text())
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
                    por_cookies = v.cookies
                    break
                except:
                    self.main_text_window.append("Error: while getting cookies. Retrying...")
                    QCoreApplication.processEvents()
                    time.sleep(2)

        return por_cookies

    # @timeit
    def get_cookies(self):
        """получаем кукисы с файла или с сайта"""

        global cookies_gl

        ppp = False
        if cookies_gl:
            ppp = self.eval_cookie_expiration_date()
            if ppp:
                return cookies_gl

        cookies_gl = self.get_cookies_from_site()
        return cookies_gl

    # @timeit
    def get_pic_id_name_lists(self, s):
        """вытаскиваем из страницы фоторейтинга 3 списка: список ID фоток, список id авторов, список имен авторов.
        перед внесением в список фотки ПРОВЕРЯЮТСЯ на наличие в общей базе."""

        self.main_text_window.append("Сравниваем фоторейтинг с базами...")
        QCoreApplication.processEvents()

        page = re.sub(r'[\t\r\n\s]','',s) # убираем пробелы, табуляции, отступы и прочее

        re.DOTALL # флаг того, что . является любым символом, в т.ч. новой строкой

        # result = re.findall(r'view\.php\?item=(\d+).{,600}user&id=(\d+).{,50}>(\w+)', page)
        # 600 и 50 - это расстояния в символах, в пределах которых нужно искать следующие паттерны

        result = re.findall(r'view\.php\?item=(\d+).*?user&id=(\d+).*?>(\w+)', page)
        # b.*?a - обозначает: найти после b СЛЕДУЮЩУЮ БЛИЖАЙШУЮ a (а между a и b могут быть любые символы)

        result = set(result) # убираем дубликаты

        pic_list = []
        spisok_u_id = []
        spisok_u_name = []

        # Проверяем, нет ли фоток уже среди закачанных и не находялся ли
        # пользователи в блэклисте, если нет и нет, то добавляем в 3 списка
        for i in result:
            if Base.if_pics(i[1], i[0]) == False and Base.if_userid_in_BL(i[1]) == False:
                pic_list.append(i[0])               # ph_id
                spisok_u_id.append(i[1])            # u_id
                spisok_u_name.append(i[2].lower())  # u_nick

        return pic_list, spisok_u_id, spisok_u_name

    # @timeit
    def download_pic(self, ph_id, file_name, folder_name, copy_folder_name="",if_list=()):
        """ Получает ID фото, имя для сохранения файла и имя папки - куда сохранять.
            Скачивает фото с данным ID. Сохраняет его с указанным именем в указанной папке.
            Папку при необходимости создает."""

        file_name = str(file_name)
        folder_name = str(folder_name)

        # проверяем наличие папки КУДА скачивать, если нет - то создаем папку.
        if os.path.isdir (folder_name) == False:
            os.makedirs (folder_name)
            self.main_text_window.append("\nПапка "+folder_name+" создана.\n")

        # проверяем наличие папки КУДА скачивать КОПИИ, если нет - то создаем папку.
        if copy_folder_name and not os.path.isdir(copy_folder_name) and self.copy_folder_chkbx.isChecked():
            os.makedirs (copy_folder_name)
            self.main_text_window.append('Создана папка: '+copy_folder_name)
            QCoreApplication.processEvents()

        # скачиваем страницу с фото
        addr = 'http://p.info'+'/'+'view.php?item='+ph_id
        errmess = "Error getting page for "+str(ph_id)+". Retrying..."
        page = self.downl_page(addr, errmess)

        temp = page.text
        page = re.sub(r'[\t\r\n\s]', '', temp)

        # на странице находим ссылку на фото - pic_link
        raw_link = re.search(r'(..p\.info/pics\.php.*?)[)"]', page) # ссылка 1 типа

        if raw_link:
            pic_link = raw_link.group(1)
        else:
            raw_link = re.search('(/pic.php\?id='+ph_id+')', page)       # индикатор ссылки 2 типа
            if raw_link:
                print('Ссылка 2-го типа. Ph_id = ', ph_id)
                pic_link = 'p.info'+'/'+'pic.php?id='+ph_id
            else:
                self.main_text_window.append("\nНа странице нет фотографии с ID "+str(ph_id)+".")
                QCoreApplication.processEvents()
                return False

        # если ссылка начинается на s. - то оставляем, если нет - обрезаем первые 2 символа \\
        if not re.match(r's\.', pic_link):
            pic_link = pic_link[2:]

        if if_list:
            self.small_text_line.setText("Загружается "+if_list[0]+" из "+if_list[1]+" файлов")
            QCoreApplication.processEvents()

        # скачиваем фото и сохраняем на диск
        addr = 'http:'+'/'+'/'+pic_link
        errmess = "Error getting pic "+str(ph_id)+". Retrying..."
        pic = self.downl_page(addr, errmess)

        file = open (folder_name+'/'+file_name+'.jpg', "wb")
        file.write(pic.content)
        file.close()
        self.main_text_window.append("Файл "+file_name+" сохранен.")

        if self.copy_folder_chkbx.isChecked():
            file = open (copy_folder_name+'/'+file_name+'.jpg', "wb")
            file.write(pic.content)
            file.close()

        # вывод скачанного изображения на экран
        if self.show_photo_chkbx.isChecked():
            self.main_pic_window.setPixmap(QtGui.QPixmap(folder_name+'/'+file_name+'.jpg').scaled(self.main_pic_window.width(),self.main_pic_window.height(),QtCore.Qt.KeepAspectRatio))
        QCoreApplication.processEvents()

        return True  # не трогать TRUE - он используется при посылании с фоторейтинга

    # @timeit
    def download_fotorating(self):
        """ Скачиваем все фото из фоторейтинга, проверив их на наличие в базе"""

        self.dis_buttons()
        # проверка логина-пароля, если их нет, то выход
        # self.user_pass()
        # if Base.is_lp() == False:
        #     return

        dest = str(self.download_folder_edit_line.text())
        folder_name = dest+'/'+"!_"+str(time.strftime('%Y')+"_"+time.strftime('%m')+"_"+time.strftime('%d')+"_Fotorating")

        # проверяем, есть ли папка DEST, если нет - создаем
        if os.path.isdir(dest) == False:
            os.makedirs(dest)

        # self.main_text_window.clear()
        self.main_text_window.append("Просматриваем страницу фоторейтинга...\n")
        QCoreApplication.processEvents()

        # скачиваем страницу фоторейтинга
        addr = 'http://p.info/index.php?action=fotorate'
        errmess = "Error getting FotoRate page. Retrying..."
        page = self.downl_page(addr, errmess)
        text_page = page.text

        # получаем 3 списка из страницы фоторейтинга (уже проверенные на наличие в базах)
        pic_list, spisok_u_id, spisok_u_name = self.get_pic_id_name_lists(text_page)

        if len(pic_list) == 0:
            self.main_text_window.append("\nВсе фото, что на данный момент находятся в фоторейтиге, у вас уже есть. (В папках пользователей или в предыдущих фоторейтингах)")
            self.en_buttons()
            QCoreApplication.processEvents()
            return

        self.main_text_window.append("\nНачинаем загрузку фотографий...")
        QCoreApplication.processEvents()

        # отправляем id фото по одному на закачку, формируя имя
        for k, i in enumerate(pic_list):
            # if Base.if_userid_in_BL(spisok_u_id[kk])==True:
            #     self.main_text_window.append("Пользователь "+str(spisok_u_name[kk])+", id: "+str(spisok_u_id[kk])+" в блэклисте!!!")
            #     QCoreApplication.processEvents()
            #     kk+=1
            #     continue

            self.small_text_line.setText("Загружается "+str(k+1)+" из "+str(len(pic_list))+" файлов")
            QCoreApplication.processEvents()
            file_name = str(spisok_u_id[k])+"--"+str(spisok_u_name[k])+"--"+str(pic_list[k])

            # добываем имя для сохранения фото в папку юзера
            copy_folder_name = self.get_folder_name(spisok_u_name[k])

            # скачиваем фото
            res = self.download_pic(pic_list[k], file_name, folder_name, copy_folder_name)

            # если файл был скачан, то добавляем запись о файле в БД
            if res:
                Base.add_user_and_pics_to_base(spisok_u_id[k], spisok_u_name[k], pic_list[k])

        self.main_text_window.append("\nФоторейтинг загружен!")
        self.small_text_line.setText("")
        self.en_buttons()
        QCoreApplication.processEvents()

    # @timeit
    def thumb_page_to_many_big_pages(self, thumb_page):
        """функция получает r.text содержимое страницы с 40 миниатюрами,
        и отдает список с 40 или меньше (если повторяются) photo_id"""

        temp = re.sub(r'[\t\r\n\s]', '', thumb_page)
        ph_id_list = re.findall(r'view\.php\?item=(\d+)"', temp)
        # ph_id_list = list(set(ph_id_list))  # убираем дубликаты и обратно делаем списком

        return ph_id_list

    # @timeit
    def get_folder_name(self, user_name):
        """формирует правильное имя папки, исходя из имени пользователя"""

        dest = str(self.download_folder_edit_line.text())
        user_name = user_name.lower()

        dic = {
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
            folder = dic[user_name[0]]
        except:
            folder = "!_0-9"

        folder_name = dest+'/'+folder+'/'+user_name

        return folder_name

    # @timeit
    def download_one_user_pic_list(self, ph_id_list, nick, user_id):
        """эта функция получает список ссылок на страницы с большими фотками, и destination (куда сохранять)
        скачивает фотки и сохраняет их на диск"""

        dt = time.strftime('%Y')+"_"+time.strftime('%m')+"_"+time.strftime('%d')

        dest = str(self.download_folder_edit_line.text())

        folder_name = self.get_folder_name(nick)
        copy_folder_name = dest+'/'+"!_"+dt+"_New_in_Base"

        self.main_text_window.append('Начинаем загрузку '+str(len(ph_id_list))+' файлов')
        QCoreApplication.processEvents()

        for number, ph_id in enumerate(ph_id_list):
            if_list = (str(number+1), str(len(ph_id_list)))
            file_name = user_id+"--"+nick+"--"+ph_id
            self.download_pic(ph_id, file_name, folder_name, copy_folder_name, if_list)

        # вносим запись о скачанных фотках в базу
        Base.add_user_and_pics_to_base(user_id, nick, ph_id_list)

    # @timeit
    def add_user_note(self, user_id, number_of_pics):
        """добаляет отметку о количестве скачанных фотографий"""

        cookies = self.get_cookies()
        payload = {
            'mod': 'edit_note',
            'userid': user_id,
            'value': str(number_of_pics)+"-p",
            'id':'user_note_text'
        }
        head = {
            'Host':'p.info',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:37.0) Gecko/20100101 Firefox/37.0',
            'X-Requested-With':'XMLHttpRequest',
            'Referer':'http://p.info/index.php?action=user&id='+user_id,
            'Connection':'keep-alive'
        }
        while True:
            try:
                requests.post('http://p.info/ajaxdata.php?mod=edit_note&userid='+user_id, cookies=cookies, data=payload, headers=head)
                break
            except:
                self.main_text_window.append("Error: writing a user_note. Retrying...")
                QCoreApplication.processEvents()
                time.sleep(2)

    # @timeit
    def base_check_of_piclist(self, pic_list, u_id):
        """ функция принимает список файлов ОДНОГО пользователя.
            сравниваем список с базой, удаляем из списка то, что в базе есть.
            функция возвращает список."""

        pic_list_final = []

        # проверяем, есть ли такой пользователь в базе,
        # если пользователя нет - то возвращаем оригинальный список
        if Base.if_userid_in_users(str(u_id)) == False:
            return (pic_list)
        # если пользователь есть, то получаем список его фото из базы
        else:
            base_list = Base.get_all_pics_from_user(u_id)

        # от изначального списка отнимаем список базы
        final_list = list(set(pic_list) - set(base_list))

        # возвращаем то, что осталось
        return final_list

    # @timeit
    def profile_parsing_name_and_number_of_pages(self, userid, profile):
        """парсим страницу профайла пользователя:
            добываем user_nick и его количество страниц с миниатюрами
            и общее количество фотографий пользователя"""

        page = re.sub(r'[\t\r\n\s]', '', profile)
        re.DOTALL

        # ищем ник пользователя в коде страницы = nick
        nick = re.search(r'data-nick="(\w+)"', page).group(1).lower()

        # ищем общее количество фоток в коде страницы = number_of_pics
        fotki = re.search(r'\d+&album=all.*?\((\d+)', page)

        if fotki:
            number_of_pics = int(fotki.group(1))    # .group(1) - извлечение из RE объекта fotki
        else:
            self.main_text_window.append("Ошибка! У пользователя "+nick+" нет фотографий")
            QCoreApplication.processEvents()
            return nick, 0, 0

        # вычисляем количество страниц с миниатютами = number_of_pages
        if number_of_pics <= 40:
            number_of_pages = 1

        s = number_of_pics%40

        if s == 0:
            number_of_pages = int(number_of_pics/40)
        if s > 0:
            number_of_pages = (number_of_pics//40)+1

        return nick, number_of_pages, number_of_pics

    # @timeit
    def por_i(self, userid, one_user=False):
        """Загружает все новые фото пользователя по USER_ID, проверив по базам какие уже скачаны, а какие надо качать"""

        # проверка логина-пароля, если их нет, то выход
        # self.user_pass()
        # if Base.is_lp() == False:
        #     return

        # очищаем поле формы
        self.other_id_edit_line.setText("")

        # ПРОВЕРКА НА BLACKLIST
        if Base.if_userid_in_BL(userid) == True:
            username = str(Base.get_name_from_id(userid))
            self.main_text_window.append("Пользователь "+username+", id: "+str(userid)+" в блэклисте!!!")
            QCoreApplication.processEvents()
            return

        # проверяем, как сюда попали, по введенному в поле ID или просто из другой части программы
        if one_user:
            self.dis_buttons()
            QCoreApplication.processEvents()

        # Получаем страницу пользователя
        addr = 'http://p.info/index.php?action=user&id='+userid
        errmess = "Error: scanning profile. Retrying..."
        temp = self.downl_page(addr, errmess)
        profile = temp.text

        # отправляем страницу на парсинг
        nick, number_of_pages, number_of_pics = self.profile_parsing_name_and_number_of_pages(userid, profile)

        # скачиваем страницы с миниатюрами, отправляем на функцию
        # thumb_page_to_many_big_pages, ответы собираем в список ph_id_list
        ph_id_list = []
        for i in range(1, number_of_pages+1):
            # скачиваем страницы с миниатюрами
            addr = 'http:'+'/'+'/'+'p.info/index.php?action=photos&p='+str(i)+'&filter=user&id='+userid+'&album=all'
            errmess = "Error: collecting links from thumbnails. Retrying..."
            result = self.downl_page(addr,errmess)

            page = result.text
            ph_id_list.extend(self.thumb_page_to_many_big_pages(page))

        # # проверяем на кол-во фоток
        # if len(ph_id_list)>(60+20):
        #   ph_id_list=ph_id_list[len(ph_id_list)-(40+40):]
        #   self.main_text_window.append("\nУ пользователя больше "+str(50+30)+" фото. Скачиваем первые "+str(45+35)+".")

        # удаляем из списка то, что уже есть в базе
        final_list = self.base_check_of_piclist(ph_id_list, userid)

        # если финальный список > 0, то отправляем его на закачку
        # и потом отправляем список на внесение в базу
        list_of_downloaded_pics = []
        if len(final_list) > 0:
            self.download_one_user_pic_list(final_list, nick, userid)
            self.add_user_note(userid, number_of_pics)

        # выводим текстовые сообщения о количестве файлов на диске и количестве скачанных файлов
        list_of_files = []
        folder_name = self.get_folder_name(nick)
        if os.path.isdir (folder_name): list_of_files = os.listdir(folder_name)
        self.main_text_window.append('\nВ папке находится '+str(len(list_of_files))+' файлов')
        self.main_text_window.append("Done! Было загружено "+str(len(list_of_downloaded_pics))+" файлов пользователя "+nick+"\n")
        self.small_text_line.setText("Готово!")
        if one_user:
            self.en_buttons()
        QCoreApplication.processEvents()

# блок функций для работы с блэклистом

    def bl_info(self):
        """Выводит справочную Информацию по блэклисту"""

        self.main_text_window.append("""Для добавления пользователя в блэклист, введите b+ XXXXXX, где XXXXXX - ID пользователя и нажмите Enter (или кнопку 'Скачать')\
            \nДля удаления пользователя из блэклиста, введите b- XXXXXX, где XXXXXX - ID пользователя и нажмите Enter (или кнопку 'Скачать')\
            \nФотографии пользователя в блэклисте не будут скачиваться программой, пока вы не удалите пользователя из блэклиста.\n""")

    def bl_show(self):
        """Показывает блэклист"""

        self.main_text_window.append("На данный момент ваш блэклист содержит следующих пользователей:\n")
        QCoreApplication.processEvents()

        dic = Base.get_blacklist()

        for i in sorted(dic):
            self.main_text_window.append("ID: "+dic[i]+" ----- UserName: "+i)
        self.main_text_window.append("")

    def bl_add(self, u_id):
        """ Добавляет пользователя в Блэклист.
            Выводит соотв. сообщение"""

        # очищаем поля сообщений и уведомлений
        self.main_text_window.clear()
        self.small_text_line.clear()
        QCoreApplication.processEvents()

        # получаем имя пользователя из базы
        u_name = Base.get_name_from_id(u_id)

        # проверка, есть ли такой пользователь в базе, если нет - выход
        if not u_name:
            self.main_text_window.append("\nВ базе нет пользователя с id: "+u_id+"\n Попробуйте снова.")
            QCoreApplication.processEvents()
            return

        Base.add_to_blacklist(u_id)
        self.main_text_window.append("Пользователь "+u_name+" добавлен в блэклист.")
        QCoreApplication.processEvents()

        self.bl_show()
        self.bl_info()
        self.favor_info()

    def bl_del(self, u_id):
        """ Удаляет пользователя из блэклиста.
            Выводит соотв. сообщение"""

        # очищаем поля сообщений и уведомлений
        self.main_text_window.clear()
        self.small_text_line.clear()
        QCoreApplication.processEvents()

        # получаем имя пользователя из базы
        u_name = Base.get_name_from_id(u_id)

        # проверка, есть ли такой пользователь в базе, если нет - выход
        if not u_name:
            self.main_text_window.append("\nВ базе нет пользователя с id: "+u_id+"\nПопробуйте снова.")
            QCoreApplication.processEvents()
            return

        Base.remove_from_blacklist(u_id)
        self.main_text_window.append("Пользователь "+u_name+" удален из блэклиста.")
        QCoreApplication.processEvents()

        self.bl_show()
        self.bl_info()
        self.favor_info()

# блок функций для работы с листом фаворитов

    def favor_info(self):
        """Выводит справочную Информацию по фаворитам"""

        self.main_text_window.append("""Фавориты - список любимых авторов.\nДля добавления пользователя в фавориты, введите f+ XXXXXX, где XXXXXX - ID пользователя, и нажмите Enter (или кнопку 'Скачать')\
            \nДля удаления пользователя из фаворитов: Введите f- XXXXXX, где XXXXXX - ID пользователя и нажмите Enter (или кнопку 'Скачать'). Все новые фотографии всех фаворитов можно скачать одной кнопкой.\n""")

    def favor_show(self):
        """Показывает фаворитов"""

        self.main_text_window.append("На данный момент у вас в фаворитах следующие пользователи:\n")
        QCoreApplication.processEvents()

        dic = Base.get_favorlist()

        for i in sorted(dic):
            self.main_text_window.append("ID: "+dic[i]+" ----- UserName: "+i)
        self.main_text_window.append("")

    def favor_add(self, u_id):
        """ Добавляет пользователя в фавориты.
            Выводит соотв. сообщения"""

        # очищаем поля сообщений и уведомлений
        self.main_text_window.clear()
        self.small_text_line.clear()
        QCoreApplication.processEvents()

        # получаем имя пользователя из базы
        u_name = Base.get_name_from_id(u_id)

        # проверка, есть ли такой пользователь в базе, если нет - выход
        if not u_name:
            self.main_text_window.append("\nВ базе нет пользователя с id: "+u_id+"\n Попробуйте снова.")
            QCoreApplication.processEvents()
            return

        Base.add_to_favorlist(u_id)
        self.main_text_window.append("Пользователь "+u_name+" добавлен в фавориты.")
        QCoreApplication.processEvents()

        self.favor_show()
        self.favor_info()
        self.bl_info()

    def favor_del(self, u_id):
        """ Удаляет пользователя из фаворитов.
            Выводит соотв. сообщения"""

        # очищаем поля сообщений и уведомлений
        self.main_text_window.clear()
        self.small_text_line.clear()
        QCoreApplication.processEvents()

        # получаем имя пользователя из базы
        u_name = Base.get_name_from_id(u_id)

        # проверка, есть ли такой пользователь в базе, если нет - выход
        if not u_name:
            self.main_text_window.append("\nВ базе нет пользователя с id: "+u_id+"\n Попробуйте снова.")
            QCoreApplication.processEvents()
            return

        Base.remove_from_favorlist(u_id)
        self.main_text_window.append("Пользователь "+u_name+" удален из фаворитов.")
        QCoreApplication.processEvents()

        self.favor_show()
        self.favor_info()
        self.bl_info()

    def favor_download(self):
        """Загружает все фотки всех фаворитов"""

        self.dis_buttons()
        self.main_text_window.clear()
        self.main_text_window.append("Загружаем все новые фото фаворитов:\n")
        QCoreApplication.processEvents()

        dic = Base.get_favorlist()

        for i in dic:
            self.main_text_window.append("Загружаем фото пользователя "+i)
            QCoreApplication.processEvents()
            self.por_i(dic[i])
        self.main_text_window.append("Все новые фото фаворитов загружены")
        self.en_buttons()
        QCoreApplication.processEvents()


    # @timeit
    def choice(self):
        """анализирует, что было введено в поле 'ID другого пользователя',
        запускает соответствующий модуль"""

        vvod = str(self.other_id_edit_line.text())
        vvod = vvod.lower().strip()

        if vvod.isdigit():
            self.por_i(vvod, one_user=True)

        elif vvod == ("f"):
            self.main_text_window.clear()
            self.favor_show()
            self.favor_info()
            self.bl_info()

        elif vvod.startswith("f+"):
            vvod = vvod[2:].strip()
            self.favor_add(vvod)

        elif vvod.startswith("f-"):
            vvod = vvod[2:].strip()
            self.favor_del(vvod)

        elif vvod == ("b"):
            self.main_text_window.clear()
            self.bl_show()
            self.bl_info()
            self.favor_info()

        elif vvod.startswith("b+"):
            vvod = vvod[2:].strip()
            self.bl_add(vvod)

        elif vvod.startswith("b-"):
            vvod = vvod[2:].strip()
            self.bl_del(vvod)

        elif vvod == "fd":
            self.favor_download()

        else:
            self.main_text_window.clear()
            self.main_text_window.append("\nНеверный ввод. Попробуйте снова.")
        return

    # def my_timer(self):

    #     if self.timer_chkbx.isChecked():
    #         cur_time = str(time.strftime('%H')+":"+time.strftime('%M')+":"+time.strftime('%S'))
    #         self.main_text_window.append("\n"+cur_time)
    #         self.download_fotorating()

    def timer_prepare(self, seconds):

        global timer_seconds
        global timer_seconds_etalon

        timer_seconds = seconds
        timer_seconds_etalon = seconds

    def my_timer2(self):

        global timer_seconds

        minutes = timer_seconds//60
        # seconds = timer_seconds - minutes*60
        seconds = timer_seconds%60

        if self.timer_chkbx.isChecked():
            timer_seconds -= 1
            self.timer_label.setText(str(minutes)+" m "+str(seconds)+" s")
            if timer_seconds <= 0:
                timer_seconds = timer_seconds_etalon
                cur_time = str(time.strftime('%H')+":"+time.strftime('%M')+":"+time.strftime('%S'))
                self.main_text_window.append("\n"+cur_time)
                self.download_fotorating()
        else:
            timer_seconds = timer_seconds_etalon
            self.timer_label.setText(str(minutes)+" m "+str(seconds)+" s")


if __name__ == '__main__':
    Base.start_base()
    app = QApplication(sys.argv)
    form = MyWindow()
    form.user_pass()
    # timer = QTimer()
    # timer.timeout.connect(form.my_timer)
    # timer.start(1000*60*20)
    form.timer_prepare(1200) # тут задаем время таймера в секундах
    timer2 = QTimer()
    timer2.timeout.connect(form.my_timer2)
    timer2.start(1000)

    form.show()
    sys.exit(app.exec_())


