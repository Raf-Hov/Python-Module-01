#!/usr/bin/env python3

class Plant:
    def __init__(self, plant: str, cm: float, days: int):
        self.plant = plant
        self.cm = cm
        self.days = days

    def show(self) -> None:
        print("Created:", end=" ")
        print(f"{self.plant}: {round(self.cm, 2)}cm, {self.days} days old")


if __name__ == "__main__":
    plant1 = Plant("Rose", 25.0, 30)
    plant2 = Plant("Oak", 200.0, 365)
    plant3 = Plant("Cactus", 5.0, 90)
    plant4 = Plant("Sunflower", 80.0, 45)
    plant5 = Plant("Fern", 15.0, 120)

    print("=== Plant Factory Output ===")
    plant1.show()
    plant2.show()
    plant3.show()
    plant4.show()
    plant5.show()
