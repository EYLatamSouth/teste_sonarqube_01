import os
import sys

def add_bug(a, b):
    result = a + b
    print(result) # debug line

def show_vulnerability(name):
    os.system("echo Hello, " + name)

def main():
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "World"
    show_vulnerability(name)
    add_bug(2, 2)

main()