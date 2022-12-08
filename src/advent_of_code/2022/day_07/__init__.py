class Directory:
    def __init__(self, *args):
        if len(args) == 0:
            self.root = self
            self.parent = self
        else:
            self.parent = args[0]
            self.root = args[1]

        self.dirs = dict()
        self.files = dict()

        self._file_sizes = 0
        self._total_size = None

    def change_dir(self, dir):
        if dir == "/":
            return self.root

        if dir == "..":
            return self.parent

        if dir in self.dirs:
            return self.dirs[dir]

        next_dir = Directory(self, self.root)
        self.dirs[dir] = next_dir
        return next_dir

    def add_file(self, *args):
        if args[0] == "dir":
            return

        size, file = args

        if file not in self.files or self.files[file] != size:
            self._file_sizes += int(size)

        self.files[file] = size

    def size(self):
        if self._total_size == None:
            self._total_size = self._file_sizes + sum(
                dir.size() for dir in self.dirs.values()
            )

        return self._total_size


def parse_input(input):
    cwd = Directory()

    for line in input.readlines():
        line = line.rstrip()

        if line[0] == "$":
            cmd, *args = line[1:].strip().split(" ")

            if cmd == "cd":
                dir = args[0]
                cwd = cwd.change_dir(dir)

        else:
            cwd.add_file(*line.split(" "))

    return cwd.root


def run(file):
    data = parse_input(file)

    part_1(data)
    part_2(data)


noop = lambda *args: None


def bfs(dir, examine_dir=noop):
    dirs = [dir]
    to_walk = [dir]

    while len(to_walk) > 0:
        cwd = to_walk.pop(0)
        examine_dir(cwd)
        to_walk += cwd.dirs.values()
        dirs += cwd.dirs.values()

    return dirs


def part_1(data):

    all_dirs = bfs(data)

    print(
        "Part_1",
        sum(filter(lambda size: size <= 100000, [dir.size() for dir in all_dirs])),
    )


def part_2(data):
    space_to_free = 30000000 - (70000000 - data.size())
    result = {"min": 70000000}

    def find_min(dir):
        size = dir.size()
        if size > space_to_free and size < result['min']:
            result['min'] = size

    bfs(data, find_min)

    print("Part_2", result['min'])
