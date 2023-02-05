import func
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def form(appprop, applist, appname, todel, appimg, mode):
    textbuffer = appprop.get_buffer()
    select = applist.get_selection()
    Gtk.TreeSelection.set_mode(select, Gtk.SelectionMode.MULTIPLE)
    model, treeiter = select.get_selected_rows()
    i=0
    print("Selected: ")
    while (i<len(treeiter)):
        if mode=='applist':
            todel.append(model[treeiter[i]][1])
        if mode=='snaplist':
            todel.append(model[treeiter[i]][0])
        i=i+1
    print(todel)
    if len(todel)==1:
        appname.set_markup(model[treeiter][0])
        func.imgupdate(todel, appimg, mode)
    else:
        if len(todel)!=0:
            appname.set_markup("Multiple apps are selected:")
            func.imgupdate(todel,appimg, mode)
    if treeiter is not None:
            if len(todel)==1:
                if mode=="applist":
                    textbuffer.set_text(
                        "App ID: " + model[treeiter][1] +
                        "\nVersion: " + model[treeiter][2] +
                        "\nBranch: " + model[treeiter][3] +
                        "\nInstallation: " + model[treeiter][4]
                    )
                if mode=="snaplist":
                    textbuffer.set_text(
                        "Version: " + model[treeiter][1] +
                        "\nRevision: " + model[treeiter][2] +
                        "\nTracking: " + model[treeiter][3] +
                        "\nPublisher: " + model[treeiter][4] +
                        "\nNotes: " + model[treeiter][5]
                    )
            else:
                i=0
                textbuffer.set_text("")
                for app in todel:
                    txtiter=textbuffer.get_end_iter();
                    textbuffer.insert(txtiter,">"+model[treeiter[i]][0]+"\n")
                    i=i+1