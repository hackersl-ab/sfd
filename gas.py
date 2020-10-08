class human:
    def __init__(self, fat):
        self.fat = fat + 10
        self.weight = self.fat * 69

    def heavy(self):
        print("He/she weighs", self.weight, "pounds")

Pranav = human(69)

Pranav.heavy()
