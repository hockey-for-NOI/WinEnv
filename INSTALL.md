# Environment Install

## MSYS2

- [MSYS2 Website](https://www.msys2.org/)
    - After Installation, Search `MSYS2 UCRT64` in your `Start Menu`
    - Right Click --> Open File Position --> Copy to Desktop
    - Right Click the copied icon --> Properties
    - The `Target` should point to somewhere like `C:\msys64\ucrt64.exe`
    - Try if you can open `MSYS2 UCRT64`

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
        - `:1` goes to line 1, `:20` goes to line 20, etc.
        - `/abc` searches for keyword 'abc', use 'n' to search next and 'N' to search previous. 
        - See `https://vim.rtorr.com/` for more info.
    - Be careful with your CAPS LOCK and CHINESE INPUT METHODS!

## Git

- `pacman -Ss git`
- `pacman -S git`

- We install git here only for `oh-my-zsh`
	- Git is too complex to introduce here.
	- See `https://git-scm.com/docs/gittutorial` for more information.

## Zsh

- `pacman -Ss zsh`
- `pacman -S zsh`

- Zsh is a bit hard to configure, use [Oh My Zsh](https://ohmyz.sh/#install)
    - In case the website is blocked, use [Zsh Wiki](https://github.com/ohmyzsh/ohmyzsh/wiki) instead.
    - After installation, you can use `exit` or `Ctrl+d` to exit zsh.

- Give it a try
    - Initially, Make sure you are not in zsh.
    - `ls /d`
    - `zsh`
    - `ls /d`
    - `exit`
    - Check the difference between two `ls`s.

- Now we are going to use the previously installed `Vim` to edit Zsh configurations.
    - Before you edit existing file, give it a backup.
    - Now we are going to edit `~/.zshrc`
        - So we first execute `cp ~/.zshrc ~/.zshrc.backup`
        - Once we want to roll back, execute `cp ~/.zshrc.backup ~/.zshrc`
    - `vim ~/.zshrc`
        - Find `ZSH_THEME="xxx"`
        - Replace that with `ZSH_THEME="clean"`
        - Save and quit. (Remember howto?)
    - Now enter zsh again and try.
        - If you are already in zsh, you can exit and zsh again
        - Another way to flush without exit is `. ~/.zshrc`

## Tmux

- `pacman -Ss tmux`
- `pacman -S tmux`

- Now we are going to edit `~/.tmux.conf` as follows

```
# Lines begins with '#' are comments.
# Add or remove them won't cause any effects.

set -g prefix C-a  # Use Ctrl-a instead of Ctrl-b (default) as key 'a' is near to key 'Ctrl'
set -g default-shell /usr/bin/zsh  # Use zsh as default shell. Check `which zsh`
```

- Try tmux
    - `tmux`
    - `Ctrl-a` then `%`
    - `Ctrl-a` then `"`
    - `Ctrl-a` then Up / Down / Left / Right
    - Use `exit` or `Ctrl-d` to kill one
    - `Ctrl-a` then `c` to create a new page, you can see page list on bottom.
    - `Ctrl-a` then `0` switch to page 0, better not exceed 9!
    - `Ctrl-a` then `d` detach, and `tmux a` back.
	- See `https://github.com/tmux/tmux/wiki/Getting-Started` for more info.


## Python

- `pacman -S mingw-w64-ucrt-x86_64-python`
- `pacman -S mingw-w64-ucrt-x86_64-python-numpy`
- `pacman -S mingw-w64-ucrt-x86_64-python-ipython`
