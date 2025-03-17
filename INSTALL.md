# Environment Install

## MSYS2

- [MSYS2 Website](https://www.msys2.org/)
    - After Installation, Search `MSYS2 MSYS` in your `Start Menu`
    - Right Click --> Open File Position --> Copy to Desktop
    - Right Click the copied icon --> Properties
    - The `Target` should point to somewhere like `C:\msys64\msys2.exe`
    - Try if you can open `MSYS2 MSYS`

- Give it a try
    - `ls /c`
        - See your files & directories in Disk `C:`
        - Try Disk `D:`
    - `echo "HELLO WORLD" > /d/hello.txt`
    - `cat /d/hello.txt`
        - Try open `D:/hello.txt` using notepad
    - `rm /d/hello.txt`
        - Always be careful using `rm`
        - NO CONFIRMATIONS, NO RECYCLEBIN, NO WAY TO REGRET!

## Vim

- `pacman -Ss vim`
    - This command works like a search
    - You may see `msys/vim x.x.xxxx-x`

- `pacman -S vim`
    - This is the actual install command
    - You may need to enter a `y` or just press `Enter` to confirm installation.

- `vim /d/hello.txt`
    - Vim is a little hard to use for beginners, now we try a simple example.
    - Vim has two modes, `Visual Mode` and `Insert Mode`
    - By default, you are in `Visual Mode`, simply use cursors to move.
    - Press 'i' to enter `Insert Mode`, and you can write anything you want.
    - Press `Esc` to go back to `Visual Mode`.
        - If not sure which mode you are currently in, always press `Esc` several times to go back to `Visual Mode`.
    - Type `:w` to save, and `:q` to quit.
    - Most keys in `Visual Mode` represents a command, e.g.
        - Key 'o' creates a new line AND ENTER `Insert Mode`.
        - Key 'u' undos the previous command, and `Ctrl+r` is redo.
        - 'yy' copies the whole current line, 'dd' is cut and 'p' is paste.
        - See `https://vim.rtorr.com/` for more info.
    - Be careful with your CAPS LOCK and CHINESE INPUT METHODS!


