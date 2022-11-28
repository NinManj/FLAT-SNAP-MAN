using System;
using Gtk;

namespace FlatpackAppView
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Application.Init();
            MainWindow win = new MainWindow();
            win.BorderWidth = 20;
            win.HeightRequest = 500;
            win.Title= "PHLÆTPÆK DELETER";
            win.Show();
            Application.Run();
        }

    }
}
