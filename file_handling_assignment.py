def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("2nd line with numbers: 12345\n")
            file.write("Another line for testing\n")
        print("File 'my_file.txt' created successfully.")
    except Exception as e:
        print("Error occurred while creating the file:", e)

def read_and_display():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Content of 'my_file.txt':\n", content)
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied to access the file.")
    except Exception as e:
        print("Error occurred while reading the file:", e)

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appended line 1\n")
            file.write("Appending more: ABCDE\n")
            file.write("Last line appended\n")
        print("Content appended to 'my_file.txt' successfully.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied to access the file.")
    except Exception as e:
        print("Error occurred while appending to the file:", e)

if __name__ == "__main__":
    create_file()
    read_and_display()
    append_to_file()
    read_and_display()
