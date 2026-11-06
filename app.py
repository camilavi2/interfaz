
import sys

from PySide6.QtWidgets import QApplication, QFrame, QMessageBox
from principal import Ui_Frame


class Window(QFrame, Ui_Frame):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("Registro de alumnos")

        self.btnRegistrar.clicked.connect(self.registrar)

    def registrar(self):

        nombre = self.txtNombre.text()
        apellido = self.txtApellido.text()
        matricula = self.txtMatricula.text()
        telefono = self.txtTelefono.text()

        if nombre == "" or apellido == "" or matricula == "" or telefono == "":
            QMessageBox.warning(self, "Aviso", "Todos los campos son obligatorios")
            return

        # Guardar los datos en el archivo de texto
        with open("registros.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre}|{apellido}|{matricula}|{telefono}\n")

        # Mostrar los datos en consola
        print("REGISTRO GUARDADO")
        print("Nombre:", nombre)
        print("Apellido:", apellido)
        print("Matricula:", matricula)
        print("Telefono:", telefono)
        print("---------------------------")

        QMessageBox.information(self, "Registro", "Alumno registrado correctamente")

        # Limpiar los campos
        self.txtNombre.clear()
        self.txtApellido.clear()
        self.txtMatricula.clear()
        self.txtTelefono.clear()


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
