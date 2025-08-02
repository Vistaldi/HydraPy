def line_search(file, string):
    # while string not in file.readline():
    #     pass
    while True:
        line = file.readline()
        if not line:
            print("\nEnd of file reached!")
            raise StopIteration
        if string in line:
            return
