# FileSystemSim
Simple Python program that simulates a shell/file system. It supports ls, mkdir, cd and touch using a linked list.

### Features

* Basic file system commands:
* ```ls```: List directory contents
* ```mkdir```: Create a new directory
* ```cd```: Change directory (supports relative, absolute paths, and commands like <```cd ..```> to return the the parent directory, and <```cd /```> to go to home directory)
* ```touch```: Create a new file

### Prerequisites

Python 3.x

### How to Run

Run Program by using: ```python3 file_system_sim.py```


### How to Test

```
mkdir project
cd project
mkdir test1
cd /
cd project/test1
touch main.py
ls
```
