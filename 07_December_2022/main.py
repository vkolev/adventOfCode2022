import os
BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def create_commands():
    with open(os.path.join(BASE_DIR, "input.txt")) as file:
        content = file.read().replace("\n$", "$").split("$ ")[1:]
        result = []
        for command in content:
            command_lines = command.split("\n")
            result.append((command_lines[0], command_lines[1:]))
        return result

def dirsizes(name, dir_size, path):
        path[name] = sum(
            v if isinstance(v, int) else dirsizes(name+"/"+k, v, path)[0] 
            for k,v in dir_size.items() if k != "..")
        return path[name], path


def main():
    commands = create_commands()
    dir_size = {"/": {}}; 
    current_size = dir_size

    for command, output in commands:
        if command[:3] == "cd ":
            current_size = current_size[command[3:]] 
            continue 
        for line in output:
            if line[:4] == "dir ": 
                current_size[line[4:]] = {"..": current_size}
                continue
            size, file = line.split(" ")
            current_size[file] = int(size)

    _, acc = dirsizes("", dir_size["/"], {})
    print(sum(filter(lambda e: e <= 100000, acc.values())))
    print(min(filter(lambda e: e >= acc[""] - 40000000, acc.values())))


if __name__ == "__main__":
    main()
