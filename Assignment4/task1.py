try:
    f = open('sample.txt', 'r')
    l1 = f.readline()
    l2 = f.readline()
    print("Reading file content:")
    print("Line 1: ",l1)
    print("Line 2: ",l2)
    f.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
