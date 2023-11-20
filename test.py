import subprocess
import os

def run_test(program, test_name, use_stdin=False):
    input_path = f'test/{program}.{test_name}.in'
    expected_output_path = f'test/{program}.{test_name}.out'

    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"Error: Input file not found - {input_path}")
        return

    # Read input
    with open(input_path, 'r') as input_file:
        input_data = input_file.read()

    # Set up command
    command = ['python', f'prog/{program}.py']


    # Check if using stdin
    if use_stdin:
        result = subprocess.run(command, input=input_data.encode('utf-8'), capture_output=True, text=True)
    else:
        command.append(input_path)
        result = subprocess.run(command, capture_output=True, text=True)

    # Check if output matches the expected output
    if not os.path.exists(expected_output_path):
        print(f"Error: Expected output file not found - {expected_output_path}")
        return

    with open(expected_output_path, 'r') as expected_output_file:
        expected_output = expected_output_file.read()
        if result.stdout.strip() != expected_output.strip():
            print(f"FAIL: {program} {test_name} failed (OutputMismatch)")
            print(f"      expected:\n{expected_output}\n\n           got:\n{result.stdout}")
        else:
            print(f"OK: {program} {test_name}")

def main():
    # Test word_count_analysis
    run_test('word_count_analysis', 'basic')
    run_test('word_count_analysis', 'stdin', use_stdin=True)

    # Test grep
    run_test('grep', 'basic')
    run_test('grep', 'file_not_found')

    # Test analyze_word_count
    run_test('analyze_word_count', 'basic')
    run_test('analyze_word_count', 'stdin', use_stdin=True)

if __name__ == '__main__':
    main()