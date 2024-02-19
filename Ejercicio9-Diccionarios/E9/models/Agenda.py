from typing import re


class Agenda(object):

    def __init__(self, agenda):

        self.__agenda = {}
        self.__agenda.update(eval(agenda))

    def _getAgenda(self):

        return self.__agenda

    def buscar_agenda(self, nombre):

        if nombre in self.__agenda:
            return self.__agenda[nombre]

    def telefonoCorrecto(self, telefono):

        if telefono in self.__agenda and re.match(r"^\d{9}$", telefono):
            return True
        raise ValueError

    def anadir_telefono(self, nombre, telefono):

        self.__agenda[nombre] = telefono

    def __str__(self):
        agenda_str = ""
        for key, value in self.__agenda.items():
            agenda_str += f"{key}: {value}\n"
        return agenda_str
