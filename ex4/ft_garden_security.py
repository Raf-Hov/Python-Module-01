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
        print("Plant created:", end=" ")
        print(f"{self._plant}: {round(self._cm, 2)}cm, {self._days} days old")

    def current(self) -> None:
        print("Current state: ", end="")
        print(f"{self._plant}: {round(self._cm, 2)}cm, {self._days} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15.0, 10)
    plant.show()
    print("")
    plant.set_height(25.0)
    plant.set_age(30)
    print("")
    plant.set_height(-5)
    plant.set_age(-5)
    print("")
    plant.current()
