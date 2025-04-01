from draw_dungeon_script import Dungeon

import pickle


class SaveableDungeon(Dungeon):
    
    def save(self, filename="saveable_dungeon.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load(filename="saveable_dungeon.pkl"):
        with open(filename, "rb") as f:
            return pickle.load(f)

    def dump(self, filename="saveable_dungeon.txt"):
        with open(filename, "w") as f:
            f.write(self.display())


if __name__ == "__main__":
    s_dungeon = SaveableDungeon(row = 3, col = 4, init = Dungeon.CONNECTED)

    s_dungeon.horizontal_walls[-1, :] = Dungeon.DISCONNECTED
    s_dungeon.horizontal_walls[0, 1:] = Dungeon.DISCONNECTED
    s_dungeon.horizontal_walls[1, 2] = Dungeon.DISCONNECTED
    s_dungeon.horizontal_walls[2, 1:3] = Dungeon.DISCONNECTED

    s_dungeon.vertical_walls[:, 0] = Dungeon.DISCONNECTED
    s_dungeon.vertical_walls[:, -1] = Dungeon.DISCONNECTED
    s_dungeon.vertical_walls[:2, 1] = Dungeon.DISCONNECTED
    s_dungeon.vertical_walls[1, 3] = Dungeon.DISCONNECTED

    s_dungeon.save()
    s_dungeon.dump()

    l_dungeon = SaveableDungeon.load()
    print(l_dungeon.display())
