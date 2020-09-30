class Animals:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight  # kg

    def feed(self):
        return f'Животное {self.name} покормлено'

    def get_voice(self):
        return f'{self.name} издаёт звук "{self.voice}"'

    def get_weight(self):
        return f'Вес {self.name} составляет {self.weight} кг'


class DairyCattle(Animals):

    def milk(self):
        return 'Животное подоено'


class Cows(DairyCattle):
    voice = 'Му-у-у'


class Goats(DairyCattle):
    voice = 'Ме-е-е'


class ShearAnimals(Animals):

    def shear_wool(self):
        return 'Животное подстрижено'


class Sheep(ShearAnimals):
    voice = 'Бе-е-е'


class Birds(Animals):

    def collect_eggs(self):
        return 'Яйца собраны'


class Gooses(Birds):
    voice = 'Га-га-га'


class Hens(Birds):
    voice = 'Ко-ко-ко'


class Ducks(Birds):
    voice = 'Кря-кря'


cow = Cows('Манька', 500)
goat_1 = Goats('Рога', 90)
goat_2 = Goats('Копыта', 110)
sheep_1 = Sheep('Барашек', 80)
sheep_2 = Sheep('Кудрявый', 105)
goose_1 = Gooses('Серый', 3)
goose_2 = Gooses('Белый', 2.5)
hen_1 = Hens('Ко-Ко', 1)
hen_2 = Hens('Кукареку', 0.8)
duck = Ducks('Кряква', 1.6)

farm = [cow, goat_1, goat_2, sheep_1, sheep_2, goose_1, goose_2, hen_1, hen_2, duck]

for animal in farm:
    print(animal.feed())
    print(animal.get_voice())
    print(animal.get_weight())