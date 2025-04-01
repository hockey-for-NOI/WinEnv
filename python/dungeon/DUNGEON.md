# Dungeon

## Display

- Download [`draw_dungeon_script.py`](./draw_dungeon_script.py)
- `python draw_dungeon_script.py`

## Modification

- A completely connected/disconnected dungeon is useless.
- We'd like to give it some modifications.
- `ipython`

```
In [1]: from draw_dungeon_script import Dungeon

In [2]: dungeon1 = Dungeon(3, 4)

In [3]: dungeon1.horizontal_walls[1, 0] = Dungeon.CONNECTED

In [4]: dungeon1.vertical_walls[1, 1] = Dungeon.CONNECTED

In [5]: dungeon1.display()
Out[5]: '+-+-+-+-+\n| | | | |\n+ +-+-+-+\n|   | | |\n+-+-+-+-+\n| | | | |\n+-+-+-+-+'
In [6]: print(dungeon1.display())
+-+-+-+-+
| | | | |
+ +-+-+-+
|   | | |
+-+-+-+-+
| | | | |
+-+-+-+-+

In [7]: dungeon1.horizontal_walls[1:3, 2] = Dungeon.CONNECTED

In [8]: dungeon1.vertical_walls[2, :] = Dungeon.CONNECTED

In [9]: print(dungeon1.display())
+-+-+-+-+
| | | | |
+ +-+ +-+
|   | | |
+-+-+ +-+

+-+-+-+-+
```

## Save and Load

- Download [`save_dungeon_script.py`](./save_dungeon_script.py)
- `python save_dungeon_script.py`
- `ipython`
```
In [1]: from save_dungeon_script import SaveableDungeon

In [2]: dungeon1 = SaveableDungeon.load()

In [3]: dungeon1.horizontal_walls[0, 0] = SaveableDungeon.DISCONNECTED

In [4]: dungeon1.save("another_dungeon.pkl")

In [5]: dungeon1 = SaveableDungeon.load()

In [6]: print(dungeon1.display())
+ +-+-+-+
| |     |
+ + +-+ +
| |   | |
+ +-+-+ +
|       |
+-+-+-+-+

In [7]: dungeon2 = SaveableDungeon.load("another_dungeon.pkl")

In [8]: print(dungeon2.display())
+-+-+-+-+
| |     |
+ + +-+ +
| |   | |
+ +-+-+ +
|       |
+-+-+-+-+
```
