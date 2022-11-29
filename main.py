import gi
import os
import subprocess
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf

inf=Gtk.Window() #Окно с информацией
todel=[] #Список для удаления

#Класс который обрабатывает сигналы из Глайда====================================
class Handler:
    def onDestroy(self,*args): # (clicked для exitbutton) Выход из программы
        Gtk.main_quit()
    def infoQuit(self,*args): #Закрытие окна информации (Костыль)
        inf.destroy()
    def clear(self,button): # (clicked для updatebutton) Выход из программы
        store.clear()
    def appear(self,*args): #(visibility-notify-event) Загрузка списка программ
        update()
    def sel(self,*args): # (cursor-changed и button-release-event) Обработчик выбора комманд
        todel.clear()
        textbuffer = appprop.get_buffer()
        select = applist.get_selection()
        Gtk.TreeSelection.set_mode(select, Gtk.SelectionMode.MULTIPLE)
        model, treeiter = select.get_selected_rows()
        global ti
        global mod
        ti=treeiter
        mod=model
        i=0
        print("Выбрано: ")
        while (i<len(treeiter)):
            todel.append(model[treeiter[i]][1])
            i=i+1
        print(todel)
        if len(todel)==1:
            appname.set_markup(model[treeiter][0])
            imgupdate()
        else:
            if len(todel)!=0:
                appname.set_markup("Multiple apps are selected:")
                imgupdate()
        if treeiter is not None:
            if len(todel)==1:
                textbuffer.set_text("App ID: " + todel[0] + "\nType: Flatpak")
            else:
                i=0
                textbuffer.set_text("")
                for app in todel:
                    txtiter=textbuffer.get_end_iter();
                    textbuffer.insert(txtiter,">"+model[treeiter[i]][0]+"\n")
                    i=i+1
    def dir(self, *args):
        if len(todel)==1:
            os.system('xdg-open ~/.var/app/'+mod[ti][1])

    def delete(deletion,*args):#(clicked для deletebutton) Удаление программ
        for app in todel:
            os.system('flatpak uninstall -y '+ app)
        update()
    def info(self,btn):#(clicked для infobutton) Формирование окна с информацией
        global inf
        inf.set_border_width(20)  # размер рамки окна
        inf.set_decorated(0)
        label=Gtk.Label()
        label.set_markup("PHLÆTPÆK DELETER\nv.0.3_py\nconvinient tool to manage your Flatpaks\nNinMan(c) - 2022")
        label.set_justify(Gtk.Justification.CENTER)
        box = Gtk.Grid()
        box.attach(label,1,0,2,1)
        btn=Gtk.Button('Close')
        btn.connect('clicked',self.infoQuit)
        box.attach(btn, 1, 2, 2 ,1)
        inf.set_title("Info")
        inf.add(box)
        inf.show_all()
#Подпрограммки нужные внеклассовой части программы====================================
def update(): #Обновление списка программ
    store.clear()
    buff = ''
    i = 0
    bashc = str(subprocess.check_output('flatpak list --columns=name,application', shell=True).decode())
    for c in bashc:
        buff += str(c)
        if c == "\t":
            iter = store.append([buff, 'b'])
            buff = ''
        if c == "\n":
            buff = buff[:-1]
            store[iter][1] = buff
            buff = ''
def imgupdate(): #Обновление списка программ
    if len(todel) == 1:
        if os.path.exists("/var/lib/flatpak/exports/share/icons/hicolor/scalable/apps/"+todel[0]+".svg"):
            pixbuf = Pixbuf.new_from_file("/var/lib/flatpak/exports/share/icons/hicolor/scalable/apps/"+todel[0]+".svg")
            appimg.set_from_pixbuf(pixbuf)
        else:
            appimg.set_from_pixbuf()
    else:
        appimg.set_from_pixbuf()
#Основная часть программы===========================================================
#Подключаемся к Глайду==============================================================
builder = Gtk.Builder()
builder.add_from_file("phlat.glade")
builder.connect_signals(Handler())

#Получаем названия объектов из Глайда================================================
window=builder.get_object("MainWindow")
window.set_border_width(20) #размер рамки окна
window.set_default_size(500,500) #размер окна
window.set_title("PHLÆTPÆK DELETER")
applist=builder.get_object("applist")
applist.set_size_request(100,100) #размер виджета списка
appprop=builder.get_object("appprop")
appprop.set_size_request(200,300) #размер виджета списка
appimg=builder.get_object("appimg")
appname=builder.get_object("appname")

#Настраиваем отображение контента в ListView=========================================
store = Gtk.ListStore(str,str) #Инициализируем хранилище для списка
renderer = Gtk.CellRendererText()#Задаём тип отображения колонок
column = Gtk.TreeViewColumn(title="Flatpak apps", cell_renderer=renderer, text=0)#Создаём колонку и задаём для неё рендерер
idcolumn = Gtk.TreeViewColumn(title="id's", cell_renderer=renderer, text=0)#Создаём колонку и задаём для неё рендерер
applist.append_column(column)# добавляем колонку в объект
applist.set_model(store)#Задаём модель для объекта (привязываем хранилище к объекту)

window.show_all()
Gtk.main()