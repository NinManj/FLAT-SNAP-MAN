
// This file has been generated by the GUI designer. Do not modify.

public partial class MainWindow
{
	private global::Gtk.HBox hbox1;

	private global::Gtk.VBox vbox1;

	private global::Gtk.ScrolledWindow GtkScrolledWindow;

	private global::Gtk.TreeView applist;

	private global::Gtk.HBox hbox3;

	private global::Gtk.Button del;

	private global::Gtk.HBox hbox5;

	private global::Gtk.Button infoButton;

	private global::Gtk.Button exit;

	private global::Gtk.VBox vbox2;

	private global::Gtk.HBox hbox2;

	private global::Gtk.Image appimg;

	private global::Gtk.Label appname;

	private global::Gtk.ScrolledWindow GtkScrolledWindow1;

	private global::Gtk.TextView appprop;

	protected virtual void Build()
	{
		global::Stetic.Gui.Initialize(this);
		// Widget MainWindow
		this.Name = "MainWindow";
		this.Title = global::Mono.Unix.Catalog.GetString("MainWindow");
		this.WindowPosition = ((global::Gtk.WindowPosition)(4));
		// Container child MainWindow.Gtk.Container+ContainerChild
		this.hbox1 = new global::Gtk.HBox();
		this.hbox1.Name = "hbox1";
		this.hbox1.Spacing = 6;
		// Container child hbox1.Gtk.Box+BoxChild
		this.vbox1 = new global::Gtk.VBox();
		this.vbox1.Name = "vbox1";
		this.vbox1.Spacing = 6;
		// Container child vbox1.Gtk.Box+BoxChild
		this.GtkScrolledWindow = new global::Gtk.ScrolledWindow();
		this.GtkScrolledWindow.Name = "GtkScrolledWindow";
		this.GtkScrolledWindow.ShadowType = ((global::Gtk.ShadowType)(1));
		// Container child GtkScrolledWindow.Gtk.Container+ContainerChild
		this.applist = new global::Gtk.TreeView();
		this.applist.CanFocus = true;
		this.applist.Name = "applist";
		this.GtkScrolledWindow.Add(this.applist);
		this.vbox1.Add(this.GtkScrolledWindow);
		global::Gtk.Box.BoxChild w2 = ((global::Gtk.Box.BoxChild)(this.vbox1[this.GtkScrolledWindow]));
		w2.Position = 0;
		// Container child vbox1.Gtk.Box+BoxChild
		this.hbox3 = new global::Gtk.HBox();
		this.hbox3.Name = "hbox3";
		this.hbox3.Spacing = 6;
		// Container child hbox3.Gtk.Box+BoxChild
		this.del = new global::Gtk.Button();
		this.del.CanFocus = true;
		this.del.Name = "del";
		this.del.UseUnderline = true;
		this.del.Label = global::Mono.Unix.Catalog.GetString("Delete");
		this.hbox3.Add(this.del);
		global::Gtk.Box.BoxChild w3 = ((global::Gtk.Box.BoxChild)(this.hbox3[this.del]));
		w3.Position = 0;
		w3.Expand = false;
		w3.Fill = false;
		// Container child hbox3.Gtk.Box+BoxChild
		this.hbox5 = new global::Gtk.HBox();
		this.hbox5.Name = "hbox5";
		this.hbox5.Spacing = 6;
		// Container child hbox5.Gtk.Box+BoxChild
		this.infoButton = new global::Gtk.Button();
		this.infoButton.CanFocus = true;
		this.infoButton.Name = "infoButton";
		this.infoButton.UseUnderline = true;
		this.infoButton.Label = global::Mono.Unix.Catalog.GetString("Info");
		this.hbox5.Add(this.infoButton);
		global::Gtk.Box.BoxChild w4 = ((global::Gtk.Box.BoxChild)(this.hbox5[this.infoButton]));
		w4.Position = 0;
		w4.Expand = false;
		w4.Fill = false;
		// Container child hbox5.Gtk.Box+BoxChild
		this.exit = new global::Gtk.Button();
		this.exit.CanFocus = true;
		this.exit.Name = "exit";
		this.exit.UseUnderline = true;
		this.exit.Label = global::Mono.Unix.Catalog.GetString("Exit");
		this.hbox5.Add(this.exit);
		global::Gtk.Box.BoxChild w5 = ((global::Gtk.Box.BoxChild)(this.hbox5[this.exit]));
		w5.Position = 1;
		w5.Expand = false;
		w5.Fill = false;
		this.hbox3.Add(this.hbox5);
		global::Gtk.Box.BoxChild w6 = ((global::Gtk.Box.BoxChild)(this.hbox3[this.hbox5]));
		w6.Position = 1;
		w6.Expand = false;
		w6.Fill = false;
		this.vbox1.Add(this.hbox3);
		global::Gtk.Box.BoxChild w7 = ((global::Gtk.Box.BoxChild)(this.vbox1[this.hbox3]));
		w7.Position = 1;
		w7.Expand = false;
		w7.Fill = false;
		this.hbox1.Add(this.vbox1);
		global::Gtk.Box.BoxChild w8 = ((global::Gtk.Box.BoxChild)(this.hbox1[this.vbox1]));
		w8.Position = 0;
		w8.Expand = false;
		w8.Fill = false;
		// Container child hbox1.Gtk.Box+BoxChild
		this.vbox2 = new global::Gtk.VBox();
		this.vbox2.Name = "vbox2";
		this.vbox2.Spacing = 6;
		// Container child vbox2.Gtk.Box+BoxChild
		this.hbox2 = new global::Gtk.HBox();
		this.hbox2.Name = "hbox2";
		this.hbox2.Spacing = 6;
		// Container child hbox2.Gtk.Box+BoxChild
		this.appimg = new global::Gtk.Image();
		this.appimg.Name = "appimg";
		this.hbox2.Add(this.appimg);
		global::Gtk.Box.BoxChild w9 = ((global::Gtk.Box.BoxChild)(this.hbox2[this.appimg]));
		w9.Position = 0;
		w9.Expand = false;
		w9.Fill = false;
		// Container child hbox2.Gtk.Box+BoxChild
		this.appname = new global::Gtk.Label();
		this.appname.Name = "appname";
		this.appname.LabelProp = global::Mono.Unix.Catalog.GetString("Choose a program");
		this.hbox2.Add(this.appname);
		global::Gtk.Box.BoxChild w10 = ((global::Gtk.Box.BoxChild)(this.hbox2[this.appname]));
		w10.Position = 1;
		w10.Expand = false;
		w10.Fill = false;
		this.vbox2.Add(this.hbox2);
		global::Gtk.Box.BoxChild w11 = ((global::Gtk.Box.BoxChild)(this.vbox2[this.hbox2]));
		w11.Position = 0;
		w11.Expand = false;
		w11.Fill = false;
		// Container child vbox2.Gtk.Box+BoxChild
		this.GtkScrolledWindow1 = new global::Gtk.ScrolledWindow();
		this.GtkScrolledWindow1.Name = "GtkScrolledWindow1";
		this.GtkScrolledWindow1.ShadowType = ((global::Gtk.ShadowType)(1));
		// Container child GtkScrolledWindow1.Gtk.Container+ContainerChild
		this.appprop = new global::Gtk.TextView();
		this.appprop.CanFocus = true;
		this.appprop.Name = "appprop";
		this.appprop.Editable = false;
		this.appprop.WrapMode = ((global::Gtk.WrapMode)(1));
		this.GtkScrolledWindow1.Add(this.appprop);
		this.vbox2.Add(this.GtkScrolledWindow1);
		global::Gtk.Box.BoxChild w13 = ((global::Gtk.Box.BoxChild)(this.vbox2[this.GtkScrolledWindow1]));
		w13.Position = 1;
		this.hbox1.Add(this.vbox2);
		global::Gtk.Box.BoxChild w14 = ((global::Gtk.Box.BoxChild)(this.hbox1[this.vbox2]));
		w14.Position = 1;
		w14.Expand = false;
		w14.Fill = false;
		this.Add(this.hbox1);
		if ((this.Child != null))
		{
			this.Child.ShowAll();
		}
		this.DefaultWidth = 369;
		this.DefaultHeight = 328;
		this.Show();
		this.DeleteEvent += new global::Gtk.DeleteEventHandler(this.OnDeleteEvent);
		this.VisibilityNotifyEvent += new global::Gtk.VisibilityNotifyEventHandler(this.appear);
		this.hbox1.VisibilityNotifyEvent += new global::Gtk.VisibilityNotifyEventHandler(this.appear);
		this.applist.RowActivated += new global::Gtk.RowActivatedHandler(this.choose);
		this.del.Clicked += new global::System.EventHandler(this.delete);
		this.infoButton.Clicked += new global::System.EventHandler(this.showInfo);
		this.exit.Clicked += new global::System.EventHandler(this.pressexit);
	}
}
