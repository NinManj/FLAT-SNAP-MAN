import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import func
import list

inf=Gtk.Window() #Окно с информацией
todel=[] #Список для удаления флатпаков

#Класс который обрабатывает сигналы из Глайда====================================
class Handler:
    def programStart(self,*args):
        updateMode()
    def onDestroy(self,*args): # (clicked для exitbutton) Выход из программы
        Gtk.main_quit()
    def infoQuit(self,*args): #Закрытие окна информации (Костыль)
        inf.destroy()
    def clear(self,button): # (clicked для updatebutton) Обновление списка
        store.clear()
        snapstore.clear()
        updateMode()
    def appear(self,*args): #(visibility-notify-event) Загрузка списка программ
        namebuffer = appname.get_buffer()
        namebuffer.set_text("Choose an app...")
    def switch(self,*args):
        global mode
        mode = stack.get_visible_child_name()
        print('List switched:'+mode)
        updateMode()

    def sel(self, *args): # (cursor-changed и button-release-event) Обработчик выбора комманд
        todel.clear()
        if (mode=='applist'):
            list.form(appprop, applist, appname, todel, appimg, mode)
        if (mode=='snaplist'):
            list.form(appprop, snaplist, appname, todel, appimg, mode)

    def dir(self, *args):
        if len(todel)==1:
            if (mode == 'applist'):
                os.system('xdg-open ~/.var/app/' + todel[0])
            if (mode == 'snaplist'):
                os.system('xdg-open /snap/' + todel[0][:-1] + '/current')

    def delete(deletion,*args):#(clicked для deletebutton) Удаление программ
        if mode == 'applist':
            for app in todel:
                os.system('flatpak uninstall -y '+ app)
        if mode == 'snaplist':
            snapdel=''
            for app in todel:
                snapdel=snapdel+str(app)
            os.system('pkexec snap remove ' + snapdel)

        updateMode()
    def info(self,btn):#(clicked для infobutton) Формирование окна с информацией
        func.message(inf,Handler,"PHLÆTMan\nv.0.4_py\nconvinient tool to manage your Flatpaks\nand Snaps\nNinMan(c) - 2022")

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
window.set_border_width(10)
window.set_default_size(250,500)
applist.set_size_request(100,100) #размер виджета списка
appprop=builder.get_object("appprop")
appprop.set_size_request(200,300) #размер виджета списка
appimg=builder.get_object("appimg")
appname=builder.get_object("appname")
delbutton=builder.get_object("delbutton")
headerbar = builder.get_object("headerbar")
headerbar.set_show_close_button(True)
window.set_titlebar(headerbar)
delbutton.get_style_context().add_class(Gtk.STYLE_CLASS_DESTRUCTIVE_ACTION)
stack = builder.get_object("stack")
mode = stack.get_visible_child_name()



#Настраиваем отображение контента в ListView=========================================
store = Gtk.ListStore(str,str) #Инициализируем хранилище для списка
snapstore = Gtk.ListStore(str,str) #Инициализируем хранилище для списка
renderer = Gtk.CellRendererText()#Задаём тип отображения колонок
column = Gtk.TreeViewColumn(title="Flatpak apps", cell_renderer=renderer, text=0)#Создаём колонку и задаём для неё рендерер
snapcolumn = Gtk.TreeViewColumn(title="Snap apps", cell_renderer=renderer, text=0)
applist.append_column(column)  # добавляем колонку в объект
applist.set_model(store)  # Задаём модель для объекта (привязываем хранилище к объекту)
snaplist.append_column(snapcolumn)  # добавляем колонку в объект
snaplist.set_model(snapstore)

window.show_all()
Gtk.main()