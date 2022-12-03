import subprocess
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf
import os

def update(store,mode):
    store.clear()
    buff = ''
    lol = [[], [], [], [], [], []]
    i = 0
    if (mode=='applist'):
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
    if (mode=='snaplist'):
        bashc = str(subprocess.check_output('snap list', shell=True).decode())
        snap = ''
        for c, n in zip(bashc, bashc[1:]):
            if c == ' ' and n == ' ':
                snap = snap
            else:
                snap = snap + str(c)
        i = 0
        snap = snap[snap.find('Notes'):len(snap)][6:]
        for c in snap:
            buff += str(c)
            if c == " ":
                lol[i].append(buff)
                buff = ''
                i = i + 1
            if c == "\n":
                lol[i].append(buff[:-1])
                buff = ''
                i = 0
        for name,id in zip(lol[0],lol[1]):
            store.append([name,id])

def imgupdate(todel,appimg, mode):
    if len(todel) == 1:
        if mode=='applist':
            if os.path.exists("/var/lib/flatpak/exports/share/icons/hicolor/scalable/apps/"+todel[0]+".svg"):
                pixbuf = Pixbuf.new_from_file("/var/lib/flatpak/exports/share/icons/hicolor/scalable/apps/"+todel[0]+".svg")
                appimg.set_from_pixbuf(pixbuf)
            else:
                appimg.set_from_pixbuf()
        if mode=='snaplist':
            if os.path.exists("/snap/"+todel[0][:-1]+"/current/meta/gui/icon.png"):
                pixbuf = Pixbuf.new_from_file("/snap/"+todel[0][:-1]+"/current/meta/gui/icon.png")
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