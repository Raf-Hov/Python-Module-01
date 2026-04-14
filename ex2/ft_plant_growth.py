#!/usr/bin/env python3

class Plant:
    def __init__(self, plant: str, cm: float, days: int, grow_rate: float):
        self.plant = plant
        self.cm = cm
        self.days = days
        self.grow_rate = grow_rate

    def show(self) -> None:
        print(f"{self.plant}: {round(self.cm, 2)}cm, {self.days} days old")

    def grow(self) -> None:
        self.cm += self.grow_rate

    def age(self) -> None:
        self.days += 1


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30, 0.8)
    start_hight = rose.cm
    print("=== Garden Plant Growth ===")
    rose.show()

    for i in range(7):
        rose.grow()
        rose.age()
        print(f"=== Day {rose.days} ===")
        rose.show()

    last_answer = rose.cm - start_hight
    print(f"Growth this week: {round(last_answer, 2)}")
