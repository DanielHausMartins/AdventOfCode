class Directory :
    def __init__(self, name, parent, subdirectories, files):
        self.parent = parent
        self.name = name
        self.subdirectories = subdirectories
        self.files = files
        self.total_size = None

    def set_total_size(self) :
        self.total_size = sum([file.size for file in self.files])
        for dir in self.subdirectories :
            if not dir.total_size :
                dir.set_total_size()
            self.total_size += dir.total_size

class File :
    def __init__(self, name, size):
        self.name = name
        self.size = size

def is_int(s) :
    try :
        int(s)
    except Exception :
        return False
    return True

def parse_history_file(hist) :
    root = Directory("\\", None, [], [])
    current_dir = root
    for command in [cmd.strip() for cmd in hist.split("$")] :
        if command.startswith("ls") :
            lines = command.split("\n")[1:]
            for line in lines :
                size,name = line.split(" ")
                if size == "dir" :
                    current_dir.subdirectories.append(Directory(name, current_dir, [], []))
                elif is_int(size) :
                    current_dir.files.append(File(name, int(size)))
        elif command.startswith("cd") :
            dirname = command.split(" ")[1]
            if dirname == ".." and current_dir.parent :
                current_dir = current_dir.parent
            else :
                for subdir in current_dir.subdirectories :
                    if subdir.name == dirname :
                        current_dir = subdir
    return root

with open("input.txt") as file :
    history_contents = file.read().strip("\n")

root_dir = parse_history_file(history_contents)
root_dir.set_total_size()

def solution1(directory) :
    res = []
    if not directory.subdirectories and directory.total_size < 100000 :
        return [(directory.name, directory.total_size)]
    for subdir in directory.subdirectories :
        res += solution1(subdir)
    if directory.total_size < 100000 :
        res.append((directory.name, directory.total_size))
    return res

def find_smallest_dir_to_delete(directory, space_needed) :
    smallest = (directory.name, directory.total_size)
    for subdir in directory.subdirectories :
        if subdir.total_size > space_needed :
            smallest_found = find_smallest_dir_to_delete(subdir, space_needed)
            if smallest_found[1] < smallest[1] :
                smallest = smallest_found
    return smallest

def solution2(directory) :
    space_needed = directory.total_size - 40000000
    smallest = find_smallest_dir_to_delete(directory, space_needed)
    print(smallest)

print(sum([dir[1] for dir in solution1(root_dir)]))
solution2(root_dir)










