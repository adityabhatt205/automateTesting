# Automated Testing Script for C Programs

A simple Python script to automate the testing of a C program.

## Usage:

In the `test_cases` variable, provide a list of dictionaries representing the test cases to be checked.

```python
    test_cases: list[dict[str, str] | dict[str, str]] = [
        {"input": "2", "expected_output": "4\n"},
        {"input": "4", "expected_output": "16\n"}
        # Add more test cases as needed
    ]
```

In the `c_program` variable, provide the path to the C program to be tested.

```python
    # Path to the C program to be tested
    c_program = r"temp.c"
```

In the `run_test()` function, the execution of `["./a.out"]` is specific to Linux . If you are running this script on different operating system, you may need to adjust the code accordingly.  
For Windows, the command must be `["a.exe"]`.  


```python
run_process = subprocess.Popen(
            ["./a.out"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
```   


## Motivation:

The script is designed to automate the process of checking C code submitted by the students participating in intra&nbsp;college coding competitions.  
It can be modified as needed.

## How It Works:

1. Provide a list of test cases in the `test_cases` variable.
2. Specify the path to the C program to be tested in the `c_program` variable.

The script will compile and then execute the C program for each test case, compare the output with the expected results, and provide feedback.

### Note:

Make sure to adapt the script based on the specific requirements and characteristics of the C programs being tested. Feel free to modify the test cases and program paths as needed.
 