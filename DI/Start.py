# import gi
#
# gi.require_version('Gtk', '3.0')
# from gi.repository import Gtk
#
#
# class HeaderBarUI(Gtk.Window):
#     def __init__(self):
#         Gtk.Window.__init__(self)
#         self.set_default_size(400, 200)
#
#         self.vbox1 = Gtk.VBox()
#         self.add(self.vbox1)
#         self.vbox1.set_border_width(10)
#         self.vbox1.set_spacing(10)
#
#         self.tophbox = Gtk.HBox()
#         self.vbox1.add(self.tophbox)
#
#         self.dataGrid = Gtk.Grid()
#         self.dataGrid.set_column_spacing(75)
#         self.dataGrid.set_row_spacing(3)
#
#         self.dataGrid.attach(Gtk.Label("Data"), 0, 0, 1, 1)
#         self.data_field = Gtk.Entry()
#         self.dataGrid.attach(self.data_field, 1, 0, 1, 1)
#
#         self.dataGrid.attach(Gtk.Label("Desde"), 0, 1, 1, 1)
#         desdemodel = Gtk.ListStore(str)
#         desdelist = ['Madrid', 'Vigo', 'Valencia']
#         for row in desdelist:
#             desdemodel.append([row])
#         self.desdebox = Gtk.ComboBox.new_with_model(desdemodel)
#         self.desdebox.connect("changed", self.on_desde_combo_changed)
#         desdecell = Gtk.CellRendererText()
#         self.desdebox.pack_start(desdecell, True)
#         self.desdebox.add_attribute(desdecell, 'text', 0)
#         self.desdebox.set_active(0)
#
#         self.dataGrid.attach(self.desdebox, 1, 1, 1, 1)
#
#         self.dataGrid.attach(Gtk.Label("Hasta"), 0, 2, 1, 1)
#         hastamodel = Gtk.ListStore(str)
#         for row in desdelist:
#             hastamodel.append([row])
#
#         self.hastabox = Gtk.ComboBox.new_with_model(hastamodel)
#         self.hastabox.connect("changed", self.on_hasta_combo_changed)
#         hastacell = Gtk.CellRendererText()
#         self.hastabox.pack_start(hastacell, True)
#         self.hastabox.add_attribute(hastacell, 'text', 0)
#         self.hastabox.set_active(0)
#         self.dataGrid.attach(self.hastabox, 1, 2, 1, 1)
#
#         radiogrid = Gtk.Grid()
#         self.radio1 = Gtk.RadioButton.new_with_label(None, "Radio 1")
#
#         radiogrid.attach(self.radio1, 0, 1, 1, 1)
#         self.radio2 = Gtk.RadioButton.new_with_label_from_widget(self.radio1, "Radio 2")
#         radiogrid.attach(self.radio2, 0, 2, 1, 1)
#         self.radio3 = Gtk.RadioButton.new_with_label_from_widget(self.radio1, "Radio 3")
#         radiogrid.attach(self.radio3, 0, 3, 1, 1)
#         self.radio4 = Gtk.RadioButton.new_with_label_from_widget(self.radio1, "Radio 4")
#         radiogrid.attach(self.radio4, 0, 4, 1, 1)
#
#         radiosframe = Gtk.Frame()
#         radiosframe.set_label("Opciones")
#         radiosframe.add(radiogrid)
#         self.tophbox.add(self.dataGrid)
#         self.tophbox.add(radiosframe)
#
#         self.txtarea = Gtk.TextView()
#         self.txtarea.set_editable(False)
#         self.txtarea.set_margin_start(5)
#         self.txtarea.set_margin_end(5)
#         self.txtarea.set_margin_bottom(5)
#         self.txtarea.set_size_request(-1, 100)
#
#         checkframe = Gtk.Frame()
#         checkframe.set_label("Preferencia de Asiento")
#         checkhbox = Gtk.HBox()
#         checkframe.add(checkhbox)
#         self.check1 = Gtk.CheckButton("Ventana")
#         self.check2 = Gtk.CheckButton("Pasillo")
#         self.check3 = Gtk.CheckButton("Centro")
#         checkhbox.add(self.check1)
#         checkhbox.add(self.check2)
#         checkhbox.add(self.check3)
#         self.vbox1.add(checkframe)
#
#         textframe = Gtk.Frame()
#         textframe.set_label("Disponibles")
#
#         textframe.add(self.txtarea)
#
#         self.vbox1.add(textframe)
#
#         buttons = Gtk.HBox()
#         self.buscar = Gtk.Button("Buscar")
#         self.comprar = Gtk.Button("Comprar")
#         self.salir = Gtk.Button("Salir")
#         buttons.add(self.buscar)
#         buttons.add(self.comprar)
#         buttons.add(self.salir)
#         self.vbox1.add(buttons)
#
#         self.comprar.connect("clicked", self.on_comprar)
#
#         self.connect("destroy", Gtk.main_quit)
#         self.show_all()
#         Gtk.main()
#
#     def on_desde_combo_changed(self, combo):
#         tree_iter = combo.get_active_iter()
#         if tree_iter is not None:
#             model = combo.get_model()
#             desde = model[tree_iter][0]
#             print("Desde %s" % desde)
#
#     def on_hasta_combo_changed(self, combo):
#         print("Desde %s" % self.get_combo_text(combo))
#
#     def get_combo_text(self, combo):
#         tree_iter = combo.get_active_iter()
#         if tree_iter is not None:
#             model = combo.get_model()
#             return model[tree_iter][0]
#
#     def on_comprar(self, btn):
#         radioTxt = self.resolve_radio(self.radio1)
#         new_line = self.data_field.get_text() + " " + self.get_combo_text(self.desdebox) + " " + self.get_combo_text(
#             self.hastabox) + " " + radioTxt.get_label() + " Pref: " + "".join(self.get_preferencias())
#         buf = self.txtarea.get_buffer()
#         end_iter = buf.get_end_iter()
#         buf.insert(end_iter, new_line + "\n")
#
#     def resolve_radio(self, master_radio):
#         active = next((
#             radio for radio in
#             master_radio.get_group()
#             if radio.get_active()
#         ))
#         return active
#
#     def get_preferencias(self):
#         str = ""
#         num = 0
#         if self.check1.get_active():
#             num += 1
#             str += (" " + self.check1.get_label())
#         if self.check2.get_active():
#             num += 1
#             str += (" " + self.check2.get_label())
#         if self.check3.get_active():
#             num += 1
#             str += (" " + self.check3.get_label())
#         if num == 0 or num == 3:
#             return "N/A"
#         else:
#             return str
#
# head = HeaderBarUI()
