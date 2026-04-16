#!/usr/bin/env python3

class Plant:

    _name: str
    _height: float
    _age: int

    def __init__(self, plant: str, cm: float, days: int, grow_rate=None):
        self._plant = plant
        self._grow_rate = grow_rate
        self._age_count = 0
        self._show_count = 0
        self._grow_count = 0
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
        """Check for negative and print height"""
        if cm < 0:
            print(f"{self._plant}: Error, height can't be negative")
            print("Height update rejected")
            return
        else:
            self._cm = cm
            print(f"Height updated: {round(self._cm)}cm")

    def set_age(self, days: int) -> None:
        """Check for negative and print age"""
        if days < 0:
            print(f"{self._plant}: Error, age can't be negative")
            print("Age update rejected")
            return
        else:
            self._days = days
            print(f"Age updated: {self._days} days")

    def get_height(self) -> float:
        """Change height"""
        return self._cm

    def get_age(self) -> float:
        """Change age"""
        return self._days

    def show(self) -> None:
        self._show_count += 1
        print(f"{self._plant}: {round(self._cm, 2)}cm, {self._days} days old")

    def current(self) -> None:
        print("Current state: ", end="")
        print(f"{self._plant}: {round(self._cm, 2)}cm, {self._days} days old")

    @staticmethod
    def stat_method(age: int) -> bool:
        return age > 356

    @classmethod
    def anonimus(cls) -> "Plant":
        return cls(_plant="Unknown", _cm=0.0, _days=0)

    def age(self):
        self._age_count += 1
        self._days += 1

    def grow(self) -> None:
        self._grow_count += 1
        self._cm += self.grow_rate


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
        self._shade = 0
        self._nutritional_value: int = 0

    def grow(self, cm: float) -> None:
        super().set_height(self.get_height() + cm)
        self._nutritional_value += 10

    def age(self, days: int) -> None:
        super().set_age(int(self.get_age() + days))
        self._nutritional_value += 10

    def show(self) -> None:
        super().show()
        super()._shade += 1
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


class _Stats(Plant):
    def show_days(self):
        if super().stat_method(super()._days):
            print(f"Is {super._days} days more than a year? -> True")
        else:
            print(f"Is {super._days} days more than a year? -> False")

    def show_stats(self):
        print(f"[statistics for {super()._name}]")
        print()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    stat = _Stats("Rose", 20.0, 10, "red")
    stat.show_stats()
