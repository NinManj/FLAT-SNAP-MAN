import gi
import os
import func
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

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
        namebuffer = appname.get_buffer()
        namebuffer.set_text("Choose an app...")
        func.update(store)
    def sel(self,*args): # (cursor-changed и button-release-event) Обработчик выбора комманд
        todel.clear()
        textbuffer = appprop.get_buffer()
        namebuffer = appname.get_buffer()
        select = applist.get_selection()
        Gtk.TreeSelection.set_mode(select, Gtk.SelectionMode.MULTIPLE)
        model, treeiter = select.get_selected_rows()
        i=0
        print("Выбрано: ")
        while (i<len(treeiter)):
            todel.append(model[treeiter[i]][1])
            i=i+1
        print(todel)
        if len(todel)==1:
            namebuffer.set_text(model[treeiter][0])
            func.imgupdate(todel,appimg)
        else:
            if len(todel)!=0:
                namebuffer.set_text("Multiple apps are selected:")
                func.imgupdate(todel,appimg)
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
            os.system('xdg-open ~/.var/app/'+todel[0])

    def delete(deletion,*args):#(clicked для deletebutton) Удаление программ
        for app in todel:
            os.system('flatpak uninstall -y '+ app)
        func.update(store)
    def info(self,btn):#(clicked для infobutton) Формирование окна с информацией
        func.message(inf,Handler,"PHLÆTPÆK DELETER\nv.0.3_py\nconvinient tool to manage your Flatpaks\nNinMan(c) - 2022")
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
delbutton=builder.get_object("delbutton")
delbutton.get_style_context().add_class(Gtk.STYLE_CLASS_DESTRUCTIVE_ACTION)

#Настраиваем отображение контента в ListView=========================================
store = Gtk.ListStore(str,str) #Инициализируем хранилище для списка
renderer = Gtk.CellRendererText()#Задаём тип отображения колонок
column = Gtk.TreeViewColumn(title="Flatpak apps", cell_renderer=renderer, text=0)#Создаём колонку и задаём для неё рендерер
idcolumn = Gtk.TreeViewColumn(title="id's", cell_renderer=renderer, text=0)#Создаём колонку и задаём для неё рендерер
applist.append_column(column)# добавляем колонку в объект
applist.set_model(store)#Задаём модель для объекта (привязываем хранилище к объекту)

window.show_all()
Gtk.main()