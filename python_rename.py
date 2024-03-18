import os
import sys

def addBug(a, b):
    result = a + b
    print(result) # debug line

def showVulnerability(name):
    os.system("echo Hello, " + name)

def main():
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "World"
    showVulnerability(name)
    addBug(2, 2)

main()
