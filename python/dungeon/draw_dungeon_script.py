import numpy as np


class Dungeon:

    CONNECTED = 0
    DISCONNECTED = 1

    def __init__(self, row, col, init=DISCONNECTED):
        self.row = row
        self.col = col
        self.horizontal_walls = init * np.ones((row + 1, col), dtype=np.bool)
        self.vertical_walls = init * np.ones((row, col + 1), dtype=np.bool)

    def display(self):
        horizontal_display = [
            "+" + 
            "+".join(np.where(line, "-", " ")) +
            "+"
            for line in self.horizontal_walls
        ]

        vertical_display = [
            " ".join(np.where(line, "|", " "))
            for line in self.vertical_walls
        ]

        display = []
        for i in range(len(vertical_display)):
            display.append(horizontal_display[i])
            display.append(vertical_display[i])
        display.append(horizontal_display[-1])
        return "\n".join(display)


if __name__ == "__main__":
    dungeon1 = Dungeon(row = 4, col = 6)
    print(dungeon1.display())

    print()

    dungeon2 = Dungeon(row = 5, col = 5, init=Dungeon.CONNECTED)
    print(dungeon2.display())
