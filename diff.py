import sys
import difflib
import argparse

from pathlib import Path

def create_diff(file_A: Path, file_B: Path, output_file: Path = None):
    file_one = open(file_A).readlines()
    file_two = open(file_B).readlines()

    if output_file:
        delta = difflib.HtmlDiff().make_file(
            file_A, file_B, file_A.name, file_B.name
        )
        with open(output_file, "w") as f:
            f.write(delta)
    else:
        delta = difflib.unified_diff(file_A, file_B, file_A.name, file_B.name)
    sys.stdout.writelines(delta)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_A_version")
    parser.add_argument("file_B_version")
    parser.add_argument("--html")
    args = parser.parse_args()

    file_A = Path(args.file_A_version)
    file_B = Path(args.file_B_version)

    if args.html:
        output_file = Path(args.html)
    else:
        output_file = None

    create_diff(file_A, file_B, output_file)

if __name__ == "__main__":
    main()

