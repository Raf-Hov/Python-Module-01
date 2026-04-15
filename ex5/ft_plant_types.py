#!/usr/bin/env python3

class Plant:
    def __init__(self, plant: str, cm: float, days: int):
        self._plant = plant
        if cm < 0:
            print(f"{self._plant} Error, height can't be negative")
            print("Height update rejected")
            return
        else:
            self._cm = cm

        if days < 0:
            print(f"{self._plant} Error, age can't be negative")
            print("Age update rejected")
            return
        else:
            self._days = days

    def set_height(self, cm: float) -> None:
        if cm < 0:
            print(f"{self._plant}: Error, height can't be negative")
            print("Height update rejected")
            return
        else:
            self._cm = cm
            print(f"Height updated: {round(self._cm)}cm")

    def set_age(self, days: int) -> None:
        if days < 0:
            print(f"{self._plant}: Error, age can't be negative")
            print("Age update rejected")
            return
        else:
            self._days = days
            print(f"Age updated: {self._days} days")

    def get_height(self) -> float:
        return self._cm

    def get_age(self) -> float:
        return self._days

    def show(self) -> None:
        print(f"{self._plant}: {round(self._cm, 2)}cm, {self._days} days old")

    def current(self) -> None:
        print("Current state: ", end="")
        print(f"{self._plant}: {round(self._cm, 2)}cm, {self._days} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int, color: str):
        self._color = color
        super().__init__(name, height, days)
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._is_blooming:
            print(f" {self._plant} is blooming beautifully!")
        else:
            print(f" {self._plant} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, days: int, trunk: float):
        super().__init__(name, height, days)
        self._trunk_diameter = trunk
        print(f" Trunk diameter: {trunk}")

    def produce_shade(self) -> None:
        print(f"Tree {self._plant} now produces a shade of ", end="")
        print(f"{self.get_height()}cm ", end="")
        print(f"long and {self._trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, plant: str, cm: float, days: int, harv: str) -> None:
        super().__init__(plant, cm, days)
        self._harvest_season = harv
        self._nutritional_value: int = 0

    def grow(self, cm: float) -> None:
        super().set_height(self.get_height() + cm)
        self._nutritional_value += 10

    def age(self, days: int) -> None:
        super().set_age(int(self.get_age() + days))
        self._nutritional_value += 10

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(42.0)
    tomato.age(20)
    tomato.show()
