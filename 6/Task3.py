import os
import sys

def print_tree(path, prefix=""):
    for i, name in enumerate(sorted(os.listdir(path))):
        full_path = os.path.join(path, name)
        is_last = i == len(os.listdir(path)) - 1
        connector = "└── " if is_last else "├── "
        print(prefix + connector + name)
        if os.path.isdir(full_path):
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(full_path, new_prefix)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Вкажіть шлях до директорії.")
    else:
        path = sys.argv[1]
        if os.path.isdir(path):
            print(os.path.basename(os.path.abspath(path)))
            print_tree(path)
        else:
            print("Це не директорія або шлях не існує.")