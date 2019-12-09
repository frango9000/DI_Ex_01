import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Exame(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exame 9-12-2019")
        self.set_border_width(10)

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(caixaV)

        lblNome = Gtk.Label("Nome:")
        lblApelido = Gtk.Label("Apelido:")
        lblTratamento = Gtk.Label("Tratamento:")
        lblNomeUsuario = Gtk.Label("Nome de Usuario:")
        lblFormato = Gtk.Label("Formato:")

        txtNome = Gtk.Entry()
        txtApelido = Gtk.Entry()
        txtTratamento = Gtk.Entry()
        txtNomeUsuario = Gtk.Entry()

        format_model = Gtk.ListStore(str)
        format_list = ['pdf', 'docx', 'odt', 'texto']
        for row in format_list:
            format_model.append([row])

        self.cmbFormato = Gtk.ComboBox.new_with_model(format_model)

        format_cell = Gtk.CellRendererText()
        self.cmbFormato.pack_start(format_cell, True)
        self.cmbFormato.add_attribute(format_cell, 'text', 0)
        self.cmbFormato.set_active(0)

        self.topGrid = Gtk.Grid()
        caixaV.pack_start(self.topGrid, True, True, 0)
        self.topGrid.attach(lblNome, 0, 0, 1, 1)
        self.topGrid.attach(txtNome, 1, 0, 1, 1)

        self.topGrid.attach(lblApelido, 2, 0, 1, 1)
        self.topGrid.attach(txtApelido, 3, 0, 1, 1)

        self.topGrid.attach(lblTratamento, 0, 1, 1, 1)
        self.topGrid.attach(txtTratamento, 1, 1, 1, 1)

        self.topGrid.attach(lblNomeUsuario, 2, 1, 1, 1)
        self.topGrid.attach(txtNomeUsuario, 3, 1, 1, 1)

        self.topGrid.attach(lblFormato, 0, 2, 1, 1)
        self.topGrid.attach(self.cmbFormato, 1, 2, 3, 1)

        builder = Gtk.Builder()
        builder.add_from_file("./cadroCorreoGlade.glade")
        self.txtCorreo = builder.get_object("txtDireccionCorreo")
        self.textArea = builder.get_object("txvListaCorreos")
        self.btnEngadir = builder.get_object("btnEngadir")
        self.btnEngadir.connect("clicked", self.on_engadir)
        caixaH2 = builder.get_object("box1")
        caixaV.pack_start(caixaH2, False, False, 0)

        caixaH3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.btnAceptar = Gtk.Button("Aceptar")
        self.btnCancelar = Gtk.Button("Cancelar")

        self.btnCancelar.connect("clicked", self.on_cancelar)

        caixaH3.pack_end(self.btnAceptar, False, False, 0)
        caixaH3.pack_end(self.btnCancelar, False, False, 0)

        caixaV.pack_start(caixaH3, True, False, 0)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_cancelar(self, btn):
        self.destroy()

    def on_engadir(self, btn):
        new_line = self.txtCorreo.get_text()
        buf = self.textArea.get_buffer()
        end_iter = buf.get_end_iter()
        buf.insert(end_iter, new_line + "\n")


if __name__ == "__main__":
    Exame()
    Gtk.main()
