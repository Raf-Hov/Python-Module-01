#!/usr/bin/env python3

class Plant:
    plant = None
    cm = None
    days = None
    print("=== Garden Plant Registry ===")

    def __init__(self, plant: str, cm: int, days: int):
        self.plant = plant
        self.cm = cm
        self.days = days

    def show(self) -> None:
        print(f"{self.plant}: {self.cm}cm, {self.days} days old")


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)

    plant1.show()
    plant2.show()
    plant3.show()
