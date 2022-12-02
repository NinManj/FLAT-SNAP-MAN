import subprocess
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf
import os

def update(store):
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

def imgupdate(todel,appimg):
    if len(todel) == 1:
        if os.path.exists("/var/lib/flatpak/exports/share/icons/hicolor/scalable/apps/"+todel[0]+".svg"):
            pixbuf = Pixbuf.new_from_file("/var/lib/flatpak/exports/share/icons/hicolor/scalable/apps/"+todel[0]+".svg")
            appimg.set_from_pixbuf(pixbuf)
        else:
            appimg.set_from_pixbuf()
    else:
        appimg.set_from_pixbuf()

def message(inf,Handler,Text):
    inf.set_border_width(20)  # размер рамки окна
    inf.set_resizable(0)
    label = Gtk.Label()
    label.set_markup(Text)
    label.set_justify(Gtk.Justification.CENTER)
    box = Gtk.Grid()
    box.attach(label, 1, 0, 2, 1)
    btn = Gtk.Button('Close')
    btn.connect('clicked', Handler.infoQuit)
    box.attach(btn, 1, 2, 2, 1)
    inf.set_title("Info")
    inf.add(box)
    inf.show_all()