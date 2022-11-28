using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Linq;
using Gtk;

public partial class MainWindow : Gtk.Window
{
    object sel;
    ListStore ls;

    //Инициализация окна==============================================
    public MainWindow() : base(Gtk.WindowType.Toplevel)
    {
        Build();
        applist.WidthRequest = 200;
        appprop.WidthRequest = 200;
    }

    //Обработчик выхода из приложения==================================
    protected void OnDeleteEvent(object sender, DeleteEventArgs a)
    {
        Application.Quit();
        a.RetVal = true;
    }

    protected void pressexit(object sender, EventArgs e)
    {
        Application.Quit();
    }

    //Вывод команд терминала======================================
    static string Bash(string command)
    {
        command = command.Replace("\"", "\"\"");
        var proc = new Process
        {
            StartInfo = new ProcessStartInfo
            {
                FileName = "/bin/bash",
                Arguments = "-c \"" + command + "\"",
                UseShellExecute = false,
                RedirectStandardOutput = true,
                CreateNoWindow = true
            }
        };
        proc.Start();
        proc.WaitForExit();
        return proc.StandardOutput.ReadToEnd();
    }
    //Обработчик команд терминала======================================
    public void BashExeq(string command)
    {
        command = command.Replace("\"", "\"\"");
        var proc = new Process
        {
            StartInfo = new ProcessStartInfo
            {
                FileName = "/bin/bash",
                Arguments = "-c \"" + command + "\"",
                UseShellExecute = false,
                RedirectStandardOutput = true,
                CreateNoWindow = true
            }
        };
        proc.Start();
        proc.WaitForExit();
        RemoveSelectedRows(applist, ls);
    }

    private void RemoveSelectedRows(TreeView treeView, ListStore listStore)
    {
        TreeIter iter;

        TreePath[] treePath = treeView.Selection.GetSelectedRows();

        for (int i = treePath.Length; i > 0; i--)
        {
            listStore.GetIter(out iter, treePath[(i - 1)]);

            string value = (string)listStore.GetValue(iter, 0);
            Console.WriteLine("Removing: " + value);

            listStore.Remove(ref iter);
        }
    }

    //Вывод списка программ===============================================
    protected void appear(object sender, EventArgs e)
    {
        int id = 0;
        List<(string N, string I)> appsStore = new List<(string N, string I)>();
        string buff = "";
        string names = Bash("flatpak list --columns=name,application");
        TreeViewColumn name = new TreeViewColumn();
        TreeViewColumn type = new TreeViewColumn();
        applist.AppendColumn(name);
        applist.AppendColumn(type);
        name.Title = "Flatpak Apps";
        ListStore store = new ListStore(typeof(string), typeof(string));
        ls = store;
        applist.Model = store;
        //ахахаха Оформляем список программ >:D
        for (int i = 0; i < names.Length; i++)
        {
            buff = buff + names[i];
            if (names[i].Equals(Convert.ToChar("\t")))
            {
                buff = buff.Remove(buff.Length - 1, 1);
                appsStore.Add((buff, ""));
                buff = "";

            }
            if (names[i].Equals(Convert.ToChar("\n")))
            {
                buff = buff.Remove(buff.Length - 1, 1);
                appsStore[id] = (appsStore[id].N, buff);
                buff = "";
                id = id + 1;
            }
        }
        foreach (var i in appsStore)
        {
            Console.WriteLine(i.N+i.I);
            store.AppendValues(i.N, i.I);
        }
        //Рендерим текст
        CellRendererText appnameCell = new CellRendererText();
        name.PackStart(appnameCell, false);
        //Располагаем в колонке как хотим
        name.AddAttribute(appnameCell, "text", 0);
    }
    //Выбор программы и вывод информации на экран
    protected void choose(object sender, RowActivatedArgs args)
    {
        var store = applist.Model;
        TreeIter b;
        store.GetIter(out b, args.Path);
        appname.Text = store.GetValue(b, 0).ToString();
        sel = store.GetValue(b, 1);
        appprop.Buffer.Text = "AppID: " + Convert.ToString(sel) + "\nType: Flatpak";
        if (System.IO.File.Exists("/var/lib/flatpak/exports/share/icons/hicolor/scalable/apps/" + sel + ".svg"))
        {
            var buffer = System.IO.File.ReadAllBytes("/var/lib/flatpak/exports/share/icons/hicolor/scalable/apps/" + sel + ".svg");
            Console.WriteLine(buffer);
            var pixbuf = new Gdk.Pixbuf(buffer);
            appimg.Pixbuf = pixbuf;
        }
        else
            appimg.File = "";
    }
    //Удаление программы
    protected void delete(object sender, EventArgs e)
    {
        BashExeq("flatpak uninstall -y " + Convert.ToString(sel));
    }

    protected void showInfo(object sender, EventArgs e)
    {
        Window info = new Window("");
        info.BorderWidth = 20;
        VBox Box = new VBox();
        Label tekst = new Label("PHLÆTPÆK DELETER\nconvinient tool to manage your Flatpak's\nNinMan(c) - 2022");
        tekst.Justify = Justification.Center;
        Button infoExit = new Button("Close");
        infoExit.Clicked += delegate { info.Destroy(); };
        Box.PackStart(tekst);
        Box.PackStart(infoExit);
        info.Title = "Info";
        info.Add(Box);
        info.ShowAll();
    }
}
