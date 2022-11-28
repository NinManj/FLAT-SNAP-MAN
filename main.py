import gi
import os
import subprocess
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf

deleteItem=""
inf=Gtk.Window()

class Handler:
    def onDestroy(self,*args):
        Gtk.main_quit()
    def infoQuit(self,*args):
        inf.destroy()
    def click(self,button):
        print('Hello World!')
    def clear(self,button):
        store.clear()
    def appear(self,*args):
        update()
    def sel(selection,*args):
        textbuffer = appprop.get_buffer()
        select = applist.get_selection()
        model, treeiter = select.get_selected()
        global deleteItem
        deleteItem=str(model[treeiter][1])
        imgupdate()
        appname.set_markup(model[treeiter][0])
        if treeiter is not None:
            textbuffer.set_text("App ID: " + deleteItem + "\nType: Flatpak")
    def delete(deletion,*args):
        os.system('flatpak uninstall -y '+ str(deleteItem))
        update()
    def info(self,btn):
        global inf
        inf.set_border_width(20)  # размер рамки окна
        inf.set_decorated(0)
        label=Gtk.Label()
        label.set_markup("PHLÆTPÆK DELETER\nv.0.2_py\nconvinient tool to manage your Flatpak's\nNinMan(c) - 2022")
        label.set_justify(Gtk.Justification.CENTER)
        box = Gtk.Grid()
        box.attach(label,1,0,2,1)
        btn=Gtk.Button('Close')
        btn.connect('clicked',self.infoQuit)
        box.attach(btn, 1, 2, 2 ,1)
        inf.set_title("Info")
        inf.add(box)
        inf.show_all()

def appQuit(self,*args):
    Gtk.main_quit()
def update():
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
def imgupdate():
    if os.path.exists("/var/lib/flatpak/exports/share/icons/hicolor/scalable/apps/"+deleteItem+".svg"):
        pixbuf = Pixbuf.new_from_file("/var/lib/flatpak/exports/share/icons/hicolor/scalable/apps/"+deleteItem+".svg")
        appimg.set_from_pixbuf(pixbuf)
    else:
        appimg.set_from_pixbuf()
#Подключаемся к Глайду==============================================================
builder = Gtk.Builder()
builder.add_from_file("phlat.glade")
builder.connect_signals(Handler())

#Получаем названия объектов из Глайда================================================
window=builder.get_object("MainWindow")

window.set_border_width(20) #размер рамки окна
window.set_default_size(500,250) #размер окна
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

window.connect("destroy", appQuit)
window.show_all()
Gtk.main()
