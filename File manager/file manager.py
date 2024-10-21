import os

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def display(self, indent=0):
        print(" " * indent + f"File: {self.name} (Size: {self.size} bytes)")
    
    def full_path(self):
        return os.path.join(self.parent.path, self.name) if self.parent else self.name

class Directory:
    def __init__(self, name, path=None):
        self.name = name
        self.children = []
        self.parent = None  # Reference to the parent directory
        self.path = path if path else self.name  # Set the directory path
    
    def add_child(self, child):
        child.parent = self  # Set the parent of the child
        self.children.append(child)
        if isinstance(child, Directory):
            child.path = os.path.join(self.path, child.name)  # Set full path for subdirectories
    
    def display(self, indent=0):
        print(" " * indent + f"Directory: {self.name} (Path: {self.path})")
        for child in self.children:
            child.display(indent + 4)

# Creating a file tree with C drive as the root path
root_path = "C:\\"
root = Directory("root", path=root_path)

root.display()