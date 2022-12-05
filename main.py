import subprocess

import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import func
import list

inf=Gtk.Window() #Окно с информацией
todel=[] #Список для удаления пакетов

#Класс который обрабатывает сигналы из Глайда====================================
class Handler:
    #Хэндлеры для старта и финиша программы==================================================
    def programStart(self,*args):
        updateMode()
    def onDestroy(self,*args): # (clicked для exitbutton) Выход из программы
        Gtk.main_quit()
    def infoQuit(self,*args): #Закрытие окна информации (Костыль)
        inf.destroy()
    #Вызываемые процедуры====================================================================
    def appnameReset(self,*args): #(visibility-notify-event) Загрузка списка программ
        appname.set_markup("Choose an app...")
        func.imgupdate(todel, appimg, mode)
    def infoWindow(self,btn):#(clicked для infobutton) Формирование окна с информацией
        msg="PHLÆTMan\nv.0.4_py\nconvinient tool to manage your Flatpaks\nand Snaps\nNinMan(c) - 2022"
        func.message(inf,Handler,msg)
    # Хэндлеры программых событий=============================================================
    def onpageSwitch(self,*args):
        global mode
        mode = stack.get_visible_child_name()
        print('List switched:'+mode)
        updateMode()
        func.imgupdate(todel, appimg, mode)
    def onappSelection(self, *args): # (cursor-changed и button-release-event) Обработчик выбора комманд
        todel.clear()
        if (mode=='applist'):
            list.form(appprop, applist, appname, todel, appimg, mode)
        if (mode=='snaplist'):
            list.form(appprop, snaplist, appname, todel, appimg, mode)
    #Обработчики нажатий кнопок===============================================================
    def buttonUpdate(self,button): # (clicked для updatebutton) Обновление списка
        store.clear()
        snapstore.clear()
        updateMode()
    def buttonDir(self, *args):
        if len(todel)==1:
            if (mode == 'applist'):
                os.system('xdg-open ~/.var/app/' + todel[0])
            if (mode == 'snaplist'):
                os.system('xdg-open /snap/' + todel[0][:-1] + '/current')
    def buttonDelete(deletion,*args):#(clicked для deletebutton) Удаление программ
        if mode == 'applist':
            for app in todel:
                os.system('flatpak uninstall -y '+ app)
        if mode == 'snaplist':
            snapdel=''
            for app in todel:
                snapdel=snapdel+str(app)
            os.system('pkexec snap remove ' + snapdel)
        updateMode()
    def buttonLaunch(self,*args):
        if len(todel)==1:
            if mode == 'applist':
                os.system('flatpak run ' + todel[0])
            if mode == 'snaplist':
                os.system('snap run ' + todel[0])

def updateMode():
    if mode=='applist':
        func.update(store, mode)
    if mode=='snaplist':
        func.update(snapstore, mode)


#Основная часть программы===========================================================
#Подключаемся к Глайду==============================================================
builder = Gtk.Builder()
builder.add_from_file("phlat.glade")
builder.connect_signals(Handler())

#Получаем названия объектов из Глайда================================================
window=builder.get_object("MainWindow")
applist=builder.get_object("applist")
snaplist=builder.get_object("snaplist")
appprop=builder.get_object("appprop")
appimg=builder.get_object("appimg")
appname=builder.get_object("appnamelabel")
delbutton=builder.get_object("delbutton")
launchbutton=builder.get_object("launchbutton")
headerbar = builder.get_object("headerbar")
stack = builder.get_object("stack")
mode = stack.get_visible_child_name()


#Задаём параметры для объектов========================================================
appprop.set_size_request(200,300)
window.set_border_width(10)
window.set_default_size(250,500)
applist.set_size_request(100,100)
headerbar.set_show_close_button(True) #Символы закрыть/свернуть окно в хэдербаре
window.set_titlebar(headerbar) #Установка хэдербара в качестае тайтлбара
delbutton.get_style_context().add_class(Gtk.STYLE_CLASS_DESTRUCTIVE_ACTION) #Красим кнопку удалить в красный


#Настраиваем отображение контента в ListView=========================================
store = Gtk.ListStore(str,str,str,str,str) #Инициализируем хранилище для списка флатпаков
snapstore = Gtk.ListStore(str,str,str,str,str,str) #Инициализируем хранилище для списка снапов
renderer = Gtk.CellRendererText()#Задаём тип отображения колонок (общий для всех)
column = Gtk.TreeViewColumn(title="Flatpak apps", cell_renderer=renderer, text=0)# Создаём колонку и задаём для неё рендерер
snapcolumn = Gtk.TreeViewColumn(title="Snap apps", cell_renderer=renderer, text=0) #Тоже самое для снапов
applist.append_column(column)  # добавляем колонку в объект
applist.set_model(store)  # Задаём модель для объекта (привязываем хранилище к объекту)
snaplist.append_column(snapcolumn)  # добавляем колонку в объект
snaplist.set_model(snapstore)

#Показываем ВСЁ========================================================================
window.show_all()
Gtk.main()