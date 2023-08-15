import sys

def wrap_lines(filename, width):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    if lines:
        for line in lines:
            stripped_line = line.strip()
            while len(stripped_line) > width:
                print(stripped_line[:width])
                stripped_line = stripped_line[width:]
            print(stripped_line)
    else:
        print("File not found or empty.")

if len(sys.argv) != 3:
    print("Usage: python wrap.py <filename> <width>")
else:
    filename = sys.argv[1]
    width = int(sys.argv[2])
    wrap_lines(filename, width)
