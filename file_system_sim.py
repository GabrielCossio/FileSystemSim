class Node:
    def __init__(self, name, is_dir=False):
        self.name = name
        self.is_dir = is_dir
        self.children = []  #List of children for dir
        self.content = None  #String content for files
        self.parent = None

class LinkedList:  # linked list implementation
    def __init__(self):
        self.head = None

    def append(self, node):
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node
    
class FileSystem:
    def __init__(self):
        self.root = Node("/", is_dir=True)
        self.current_dir = self.root

    def ls(self):
        if self.current_dir.children:  # Check for children directly
            for child in self.current_dir.children:
                print(child.name + ("/" if child.is_dir else ""))

    def mkdir(self, name):
        for child in self.current_dir.children:
            if child.name == name:
                print("Error: Directory already exists.")
                return
        new_dir = Node(name, is_dir=True)
        new_dir.parent = self.current_dir  # set parent for the .. functionality  
        self.current_dir.children.append(new_dir) 
  
    def cd(self, path):
        if path == "/":
            self.current_dir = self.root
        elif path == "..":  
            if self.current_dir != self.root:  
                self.current_dir = self.current_dir.parent
            else:
                print("Error: Already at root directory.")  
        else:  
            components = path.split('/')  # Split the path into parts 
            for component in components:
                found = False
                for child in self.current_dir.children:
                    if child.name == component and child.is_dir:
                        self.current_dir = child  
                        found = True
                        break
                if not found:
                    print(f"cd: {component}: No such file or directory") 
                    return  # Stop if path not valid

    def touch(self, name):
        new_file = Node(name)
        self.current_dir.children.append(new_file)

# Main program interaction loop
if __name__ == "__main__":
    fs = FileSystem()

    while True:
        command = input(f"{fs.current_dir.name} > ").split()

        if not command:
            continue
        elif command[0] == "exit":
            break
        elif command[0] == "ls":
            fs.ls()
        elif command[0] == "mkdir":
            if len(command) > 1:
                fs.mkdir(command[1])
            else:
                print("Try: mkdir <directory_name>")
        elif command[0] == "cd":
            if len(command) > 1:
                fs.cd(command[1])
            else:
                print("Try: cd <directory_name>")
        elif command[0] == "touch":
            if len(command) > 1:
                fs.touch(command[1])
            else:
                print("Try: touch <file_name>")
        else:
            print("command not found")
