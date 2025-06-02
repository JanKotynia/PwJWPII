from operator import truediv


class Student:
    def __init__(self,imie,wynik):
        self.imie=imie
        self.wynik=wynik

    def __str__(self):
        return f"Student:\n{self.imie}\n{self.wynik}"

    def __eq__(self, other):
        return self.wynik==other.wynik

    def __ne__(self, other):
        return not(self==other)

    def __lt__(self, other):
        return self.wynik<other.wynik

    def __gt__(self, other):
        return not(self<other)

    def __repr__(self):
        return f"Student:\n{self.imie}\n{self.wynik}"


s1 = Student("Bartello", 80)
s2 = Student("Halven", 99)

print(s1)
print(s1!=s2)
print(s1>s2)
print(s2)


