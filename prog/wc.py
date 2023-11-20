import argparse
import sys

def word_count_analysis(filepath):
    if filepath:
        with open(filepath, 'r') as file:
            lines = file.readlines()
    else:
        lines = sys.stdin.readlines()

    total_lines = len(lines)
    total_words = sum(len(line.split()) for line in lines)
    total_chars = sum(len(line) for line in lines)

    result = f"{total_lines} {total_words} {total_chars} {filepath or 'stdin'}"
    print(result)

def main():
    parser = argparse.ArgumentParser(description='Word count utility')
    parser.add_argument('filepath', nargs='?', help='File to analyze')
    args = parser.parse_args()

    word_count_analysis(args.filepath)

if __name__ == "__main__":
    main()