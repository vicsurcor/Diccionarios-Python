class Contactos:
    def __init__(self, lista):
        self.__agenda = lista
        self.__agenda = self.unir_contactos()

    def agenda(self):
        return self.__agenda

    def unir_contactos(self):
        contactos = {}
        for contacto in self.__agenda:
            nombre = contacto[0]
            emails = contacto[1:]
            if nombre in contactos:
                contactos[nombre].extend(emails)

            else:
                contactos[nombre] = list(emails)

        return contactos









