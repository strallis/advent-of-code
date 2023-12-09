# from aocd import lines
from anytree import Node, RenderTree


def traverse_dir(index: int) -> int:
    level = 0
    size = 0
    for command in lines[index:]:
        if level == -1:
            return size
        if command == "$ cd ..":
            level -= 1
        elif command[0:4] == "$ cd":
            level += 1
        elif command.split(" ")[0].isdigit():
            size += int(command.split(" ")[0])
    return size


lines = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
lines = lines.split("\n")
root = Node(f"{lines[0]} (dir)")
parent_node = root
for index, command in enumerate(lines):
    if command[0] == "$":
        pass
    else:
        if command[0:3] == "dir":
            dir_name = command.split(" ")[1]
            size = traverse_dir(index)
            Node(f"{dir_name} (dir) | size={size}", parent=parent_node)
        # else:
        #    size, name = command.split(" ")
        #    Node(f"{name} (file, size={int(size)})", parent=parent_node)

for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))
