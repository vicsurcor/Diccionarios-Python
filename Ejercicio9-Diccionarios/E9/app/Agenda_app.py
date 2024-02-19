import E9.models.Agenda


class AgendaApp:
    def __init__(self):
        self.agenda = E9.models.Agenda.Agenda("{'Adela': '444444444', 'Pedro': '222222222', 'Bertoluchi': "
                                              "'777777777', 'Paco': '555555555', 'Berta': '666666666', "
                                              "'Alba': '333333333', 'Ana': '111111111'}")
        print(self.agenda, "\n")

    def iniciar_app(self):
        nombre = str(input("Introduzca el nombre a buscar: "))

        if self.agenda.buscar_agenda(nombre) is None:
            tel = int(input("Introduzca el telefono: "))
            self.agenda.telefonoCorrecto(tel)
        else:
            print(self.agenda.buscar_agenda(nombre))
            tel = str(input("Introduzca el telefono: "))
            self.agenda.anadir_telefono(nombre, tel)
            print(self.agenda, "\n")


app = AgendaApp()
app.iniciar_app()
print("Victor Suros")
