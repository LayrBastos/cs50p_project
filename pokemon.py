class Pokemon:
    def __init__(self, name, color, height, weight, type_):
        self.name = name.capitalize()
        self.color = color
        self.color_revealed = False
        self.height = height
        self.weight = weight
        self.type_ = type_
        self.type_revealed = False

    def check_guess(self, other):
        return self.name == other.name

    def is_taller_than(self, other):
        return self.height > other.height

    def is_heavier_than(self, other):
        return self.weight > other.weight

    def compare_types(self, other):
        if self.type_ == other.type_:
            print(f"I'm not {other.name}, but we are from the same pokemon type...\nYou're getting closer!!\n")
            self.type_revealed = True

    def compare_colors(self, other):
        if self.color == other.color:
            print(f"Me and {other.name} have the same color... I'd say we are kinda {self.color}")
            self.color_revealed = True




