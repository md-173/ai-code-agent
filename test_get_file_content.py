from functions.get_file_content import get_file_content

print("Result for current directory lorem.txt:")
print(get_file_content("calculator", "lorem.txt"))
print("Result for current directory main.py:")
print(get_file_content("calculator", "main.py"))
print("Result for file in pkg:")
print(get_file_content("calculator", "pkg/calculator.py"))
print("Result for '/bin' directory:")
print(get_file_content("calculator", "/bin/cat"))
print("Result for missing file:")
print(get_file_content("calculator", "pkg/does_not_exist.py"))
