import re
import sys

def grep(pattern, filename):
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                print(pattern)
                print(line)
                a = re.search(pattern, line)
                print(a)
                if re.search(pattern, line):
                    print(f"{filename}:{line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python grep.py <pattern> <filename>")
        sys.exit(1)

    pattern = sys.argv[1]
    filename = sys.argv[2]

    grep(pattern, filename)