class Sun:
    def __init__(self):
        self.shine = True

    def is_shine(self, light):
        if light:
            return "Արևը շողում է"
        return "Արևը չի շողում, գիշեր է"


class Tree:
    def __init__(self):
        self.name = "Ծառ"

    def photosynthesis(self, light):
        if light:
            return "Ծառը արտադրում է թթվածին"
        return "Ծառը չի արտադրում թթվածին, գիշեր է"


class Grass:
    def __init__(self):
        self.name = "Խոտ"

    def to_be_eaten(self):
        return("Գորտը կերավ խոտը")


class Frog:
    def __init__(self):
        self.name = "Գորտ"
        self.awake = True
        self.stomach = 0

    def is_awake(self, light):
        if not light:
            self.awake = False


    def walk(self):
        if self.awake:
            return "Գորտը քայլում է"
        return "Գորտը չի քայլում, քնած է"

    def breathe(self):
        if self.awake:
            return "Գորտը շնչում է"
        return "Գորտը չի շնչում, քնած է"

    def eat(self):
        if self.awake:
            if self.stomach != 3:
                self.stomach += 1
                print(Grass.to_be_eaten(Grass))
                return "Գորտը ուտում է "
            return "Գորտը կուշտ է"
        return "Գորտը չի ուտում, քնած է"





