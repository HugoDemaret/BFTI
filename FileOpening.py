def fileopening():
    file_path = input("Enter you binary file path")
    file = open(file_path, "r+")
    lines = file.readlines()
    for line in lines:
        line_string = line
        for letter in line_string:
            print(letter)
    file.close()
