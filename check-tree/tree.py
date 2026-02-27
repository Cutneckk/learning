import argparse
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SPACE = "    "
I = "│   "
T = "├── "
L = "└── "

def print_tree(path, prefix="", level=0, max_level=None, dirs_only=False):
    if max_level is not None and level >= max_level:
        return

    items = sorted(path.iterdir())

    if dirs_only:
        items = [item for item in items if item.is_dir()]

    for i, item in enumerate(items):
        connector = L if i == len(items) - 1 else T
        logger.info(prefix + connector + item.name)

        if item.is_dir():
            extension = SPACE if i == len(items) - 1 else I
            print_tree(item, prefix + extension, level + 1, max_level, dirs_only)


def count_items(path, max_level=None, dirs_only=False, level=0):
    if max_level is not None and level >= max_level:
        return 0, 0

    try:
        items = path.iterdir()
    except PermissionError:
        return 0, 0

    dirs = 0
    files = 0

    for item in items:
        if item.is_dir():
            dirs += 1
            sub_dirs, sub_files = count_items(item, max_level, dirs_only, level + 1)
            dirs += sub_dirs
            files += sub_files
        else:
            files += 1

    return dirs, files


def main():
    parser = argparse.ArgumentParser(prog="tree.py")
    parser.add_argument("dir", nargs='?',default=".", help="show structure")
    parser.add_argument("-d", help="show only directories")
    parser.add_argument("-L", type=int, help="deep show")

    args = parser.parse_args()
    root = Path(args.dir)

    if not root.is_dir():
        logger.info(f"error: '{args.dir}' is not directory")
        return

    logger.info(f"{root}/")
    print_tree(root, max_level=args.L, dirs_only=args.d)
    logger.info('')

    dirs, files = count_items(root, max_level=args.L, dirs_only=args.d)
    logger.info(f"{dirs} directories, {files} files")


if __name__ == "__main__":
    main()

