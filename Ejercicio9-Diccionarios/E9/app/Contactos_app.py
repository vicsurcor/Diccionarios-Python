import E9.models.Contactos


class ContactosApp:

    def __init__(self):

        self.contactos = E9.models.Contactos.Contactos([('Ana', 'correo1@ana.es', 'correo2@ana.es'), ('Maria',
                                                        'correo1@maria.es'), ('Iker', 'correo1@iker.es'),
                                                        ('Ana', 'correo3@ana.es', 'correo4@ana.es'),
                                                        ('Iker', 'correo2@iker.es'), ('Ana', 'correo5@ana.es')])

        for contacto, emails in self.contactos.agenda().items():
            print(contacto, ": ", emails)
        print("")


c1 = ContactosApp()
print("Victor Suros")
