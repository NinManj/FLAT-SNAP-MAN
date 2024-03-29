import subprocess
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf
from gi.repository.GdkPixbuf import InterpType
import os

def update(store,mode):
    store.clear()
    buff = ''
    kek=[[], [], [], [], []]
    lol = [[], [], [], [], [], []]
    if (mode=='applist'):
        bashc = str(subprocess.check_output('flatpak list --columns=name,application,version,branch,installation', shell=True).decode())
        i = 0
        for c in bashc:
            buff += str(c)
            if c == "\t":
                kek[i].append(buff[:-1])
                buff = ''
                i = i + 1
            if c == "\n":
                kek[i].append(buff[:-1])
                buff = ''
                i=0
        for name,id,ver,branch,inst in zip(kek[0],kek[1],kek[2],kek[3],kek[4]):
            store.append([name,id,ver,branch,inst])
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
        snap=snap+"\n"
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
        for name,ver,rev,track,publ,notes in zip(lol[0],lol[1],lol[2],lol[3],lol[4],lol[5]):
            store.append([name,ver,rev,track,publ,notes])

def imgupdate(todel,appimg, mode):
    icontheme = Gtk.IconTheme.get_default()
    stock = icontheme.load_icon(Gtk.STOCK_ABOUT, 128, 0)
    if len(todel) == 1:
        flatdir = "/var/lib/flatpak/exports/share/icons/hicolor/scalable/apps/" + todel[0] + ".svg"
        snapdir = "/snap/" + todel[0][:-1] + "/current/meta/gui/icon.png"
        modedir = ""
        if mode=='applist':
            modedir=flatdir
        if mode == 'snaplist':
            modedir=snapdir
        if os.path.exists(modedir):
            pixbuf = Pixbuf.new_from_file(modedir)
        else:
            pixbuf = stock
        pixbuf = pixbuf.scale_simple(48, 48, InterpType.BILINEAR)
        appimg.set_from_pixbuf(pixbuf)
    else:
        appimg.set_from_pixbuf(stock)

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