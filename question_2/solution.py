# Question 2 - File Explorer
# Reads commands from stdin, one per line (command + arg separated by a space),
# and simulates an in-memory file system. See the PDF for the exact command specs.

import sys


class Node:
    def __init__(self, name, is_dir, parent=None):
        self.name = name
        self.is_dir = is_dir
        self.parent = parent
        self.children = {} if is_dir else None  # name -> Node


class FileExplorer:
    def __init__(self):
        self.root = Node("", is_dir=True, parent=None)
        self.current = self.root

    def _abs_path(self, node):
        if node is self.root:
            return "/"
        parts = []
        while node is not self.root:
            parts.append(node.name)
            node = node.parent
        return "/" + "/".join(reversed(parts))

    def cwd(self):
        return self._abs_path(self.current)

    def cd(self, path):
        # absolute path starts from root, otherwise walk from current dir
        start = self.root if path.startswith("/") else self.current
        parts = [p for p in path.split("/") if p != ""]

        node = start
        for part in parts:
            if part == "..":
                if node is self.root:
                    return "currently at root."
                node = node.parent
            else:
                child = node.children.get(part) if node.is_dir else None
                if child is None:
                    return f"{part} not found."
                if not child.is_dir:
                    return f"{path} is not a directory."
                node = child

        self.current = node
        return None

    def ls(self):
        names = sorted(self.current.children.keys())
        return " ".join(names)

    def mkdir(self, name):
        if name in self.current.children:
            return f"{name} already exists."
        self.current.children[name] = Node(name, is_dir=True, parent=self.current)
        return None

    def touch(self, name):
        if name in self.current.children:
            return f"{name} already exists."
        self.current.children[name] = Node(name, is_dir=False, parent=self.current)
        return None


def main():
    fe = FileExplorer()

    for raw_line in sys.stdin:
        line = raw_line.strip()
        if not line:
            continue

        parts = line.split(" ", 1)
        command = parts[0]
        arg = parts[1] if len(parts) > 1 else None

        if command == "exit":
            break
        elif command == "cwd":
            print(fe.cwd())
        elif command == "cd":
            result = fe.cd(arg)
            if result is not None:
                print(result)
        elif command == "ls":
            result = fe.ls()
            if result:
                print(result)
        elif command == "mkdir":
            result = fe.mkdir(arg)
            if result is not None:
                print(result)
        elif command == "touch":
            result = fe.touch(arg)
            if result is not None:
                print(result)


if __name__ == "__main__":
    main()
