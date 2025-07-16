from functions.run_python import run_python_file

def test():
    result = run_python_file("calculator", "main.py")
    print("Result: ")
    print(result)
    print("")

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Result: ")
    print(result)
    print("")

    result = run_python_file("calculator", "tests.py")
    print("Result: ")
    print(result)
    print("")

    result = run_python_file("calculator", "../main.py")
    print("Result: ")
    print(result)
    print("")

    result = run_python_file("calculator", "nonexistent.py")
    print("Result: ")
    print(result)
    print("")


if __name__ == "__main__":
    test()
