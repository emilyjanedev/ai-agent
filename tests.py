from functions.write_file_content import write_file

def test():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result: ")
    print(result)
    print("")

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result: ")
    print(result)
    print("")

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Result: ")
    print(result)
    print("")


if __name__ == "__main__":
    test()
