"Attempt to read a file in the current directory"
"Read a file by changing the working directory"

import os

def main():
    "Main logic"
    os.chdir("/tmp")
    with open("protoss.txt", "r") as foo:
        print(foo.read())

main()
