import argparse
import sys

def analyze_word_count(filepath):
    if filepath:
        with open(filepath, 'r') as file:
            lines = file.readlines()
    else:
        lines = sys.stdin.readlines()

    total_lines = len(lines)
    total_words = sum(len(line.split()) for line in lines)
    total_chars = sum(len(line) for line in lines)

    result_string = f"{total_lines} lines, {total_words} words, {total_chars} characters in {filepath or 'stdin'}"
    print(result_string)

def main():
    parser = argparse.ArgumentParser(description='Word count analysis utility')
    parser.add_argument('filepath', nargs='?', help='File to analyze')
    args = parser.parse_args()

    analyze_word_count(args.filepath)

if __name__ == "__main__":
    main()