import json


class ModelAI:
    liczba_modeli = 0

    def __init__(self, nazwa_modelu, wersja_modelu):
        self.nazwa_modelu=nazwa_modelu
        self.wersja_modelu=wersja_modelu

    @classmethod
    def nowy_model(cls):
        cls.liczba_modeli=+1

    @classmethod
    def ile_modeli(cls):
        return cls.liczba_modeli

    @classmethod
    def z_pliku(cls, nazwa_pliku):
        with open(nazwa_pliku, "r") as plik:
            dane = json.load(plik)
            model2 = ModelAI(dane["name"], dane["version"])
            cls.liczba_modeli=+1
            print(model2.nazwa_modelu)
            print(model2.wersja_modelu)


model = ModelAI("skib","8")

print(ModelAI.ile_modeli())

ModelAI.z_pliku("plik.json")

print(ModelAI.ile_modeli())

