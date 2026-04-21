#!/usr/bin/env python3

class Plant:
    def __init__(self, plant: str, cm: float, days: int, grow_rate=1.0):
        self._plant = plant
        self._grow_rate = grow_rate
        self._cur = cm
        self._cura = days
        self._stats = self._Stats()
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

    def set_age(self, days: int) -> None:
        """Check for negative and print age"""
        if days < 0:
            print(f"{self._plant}: Error, age can't be negative")
            print("Age update rejected")
            return
        else:
            self._days = days

    def get_height(self) -> float:
        """Change height"""
        return self._cm

    def get_age(self) -> float:
        """Change age"""
        return self._days

    class _Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0
            self._shade_calls = 0

    def show(self) -> None:
        self._stats._show_calls += 1
        if self._plant == "Unknown":
            print(f"{self._plant} plant:", end=" ")
            print(f"{round(self._cur, 2)}cm, {self._cura} days old")
        else:
            print(f"{self._plant}:", end=" ")
            print(f"{round(self._cur, 2)}cm, {self._cura} days old")

    def past(self) -> None:
        print("Current state: ", end="")
        print(f"{self._plant}: {round(self._cm, 2)}cm, {self._days} days old")

    def display_stats(self) -> None:
        def print_stats_all(self):
            print(f"Stats: {self._stats._grow_calls} grow,", end=" ")
            print(f"{self._stats._age_calls} age, ", end="")
            print(f"{self._stats._show_calls} show")

        if self._plant == "Unknown":
            print(f"[statistics for {self._plant} plant]")
            print_stats_all(self)
        else:
            print(f"[statistics for {self._plant}]")
            print_stats_all(self)

    @staticmethod
    def stat_method(age: int) -> None:
        if age > 365:
            print(f"Is {age} days more than a year? -> True")
        else:
            print(f"Is {age} days more than a year? -> False")

    @classmethod
    def anonimous(cls) -> "Plant":
        return cls(plant="Unknown", cm=0.0, days=0)

    def age(self, age: int):
        self._stats._age_calls += 1
        self._cura = age

    def grow(self, days: float) -> None:
        self._stats._grow_calls += 1
        self._cur = days


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int, color: str):
        self._color = color
        super().__init__(name, height, days)
        self._is_blooming = False
        self._seeds = 0

    def bloom(self) -> None:
        self._seeds = 42
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._is_blooming:
            print(f" {self._plant}: is blooming beautifully!")
        else:
            print(f" {self._plant} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name, height, days, color):
        super().__init__(name, height, days, color)

    def show_for_seeds(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")


class Tree(Plant):
    def __init__(self, name: str, height: float, days: int, trunk: float):
        super().__init__(name, height, days)
        self._trunk_diameter = trunk

    def show_tree(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")

    def display_stats_for_tree(self) -> None:
        super().display_stats()
        print(f" {self._stats._shade_calls} shade")

    def produce_shade(self) -> None:
        self._stats._shade_calls += 1
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
        self._shade += 1
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old ")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.stat_method(30)
    rose.stat_method(400)
    print("\n=== Flower")
    rose.show()
    rose.display_stats()
    print("[asking the rose to grow and bloom]")
    rose.bloom()
    rose.grow(23.0)
    rose.show()
    rose.display_stats()
    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show_tree()
    oak.display_stats_for_tree()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    oak.display_stats_for_tree()
    print("\n=== Seed")
    sunf = Seed("Sunflower", 80.0, 45, "yellow")
    sunf.show_for_seeds()
    print("[make sunflower grow, age and bloom]")
    sunf.grow(110.0)
    sunf.age(65)
    sunf.bloom()
    sunf.show_for_seeds()
    sunf.display_stats()
    print("\n=== Anonymous")
    anonim = Plant.anonimous()
    anonim.show()
    anonim.display_stats()
