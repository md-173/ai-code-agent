from functions.run_python_file import run_python_file

def test():
    print("Result for running calculator main.py")
    print(run_python_file("calculator", "main.py"))
    print("Result for running 3+5 input for calculator main.py")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print("Result for running calculator tests")
    print(run_python_file("calculator", "tests.py"))
    print("Result for running outside directory")
    print(run_python_file("calculator", "../main.py"))
    print("Result for running nonexistent file")
    print(run_python_file("calculator", "nonexistent.py"))
    print("Result for running non executable")
    print(run_python_file("calculator", "lorem.txt"))

if __name__ == "__main__":
    test()
