import os

class Consola:
    @staticmethod
    def limpiar_consola():
        if os.name == "posix":
            os.system("clear")
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system("cls")