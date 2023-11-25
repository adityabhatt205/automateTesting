import subprocess


def run_test(code_file, input_data):
    try:
        # Compile the C program using gcc
        compile_process = subprocess.Popen(
            ["gcc", code_file, "-o", "a.out"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        _, compile_error = compile_process.communicate(timeout=5)

        if compile_error:
            return None, compile_error

        # Run the compiled program
        run_process = subprocess.Popen(
            ["./a.out"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Provide input to the program
        stdout, stderr = run_process.communicate(input_data, timeout=5)

        # Return the output and error (if any)
        return stdout, stderr

    except subprocess.TimeoutExpired:
        return None, "Timeout Error: The program took too long to execute."

    except Exception as e:
        return None, f"Error: {str(e)}"


def main():
    # List of test cases
    test_cases = [
        {"input": "2", "expected_output": "4\n"},
        {"input": "4", "expected_output": "16\n"},
        # Add more test cases as needed
    ]

    # Path to the C program to be tested
    c_program = "temp.c"

    # Run tests
    for i, test_case in enumerate(test_cases, start=1):
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]

        print(f"Running Test Case #{i}")
        output, error = run_test(c_program, input_data)

        if error:
            print(f"Error: {error}")
        else:
            if output == expected_output:
                print("Test Passed!")
            else:
                print("Test Failed. Expected output:", repr(expected_output))
                print("Actual output:", repr(output))


if __name__ == "__main__":
    main()
