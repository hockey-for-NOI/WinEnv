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
