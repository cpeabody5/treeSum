import re

class Node:

    def __init__(self, val, line, showVal):
        self.children = []
        self.val = val
        self.line = line
        self.depth = 0
        self.showVal = showVal

    def newChild(self, childVal, childLine):
        self.children.append(Node(childVal, childLine, False))
        self.children[-1].depth = self.depth + 1

    def printTree(self):
        if self.showVal:
            res = f' -total: ${self.val:.2f}'
        else:
            res = ''
        print(f'{" "*self.depth}{self.line[:-1]}{res}')
        for c in self.children:
            c.printTree()

    def parseTree(self, lines):
        for l in lines:
            self.parseLine(l)

    def parseLine(self, line):
        #get indentation level
        newDepth = len(line) - len(line.lstrip())
        if newDepth ==  self.depth + 1:
            #get data from line and create child
            childVal = re.search('\$([0-9]+\.?[0-9]*)', line)
            if not childVal:
                childVal = 0
            else:
                childVal = float(childVal.group()[1:])
            self.newChild(childVal, line)
        if newDepth > self.depth + 1:
            self.children[-1].parseLine(line)

    def treeSum(self):
        if self.children:
            for child in self.children:
                child.treeSum()
                if self.val == 0:
                    self.showVal = True
                self.val += child.val

def parseFile(file):
    with open(file) as f:
        lines = f.readlines()
    f.close()
    return lines

def main():
    lines = parseFile('tree.txt')
    tree = Node(0, lines[0], False)
    tree.parseTree(lines[1:])
    print("Original Tree")
    tree.printTree()
    tree.treeSum()
    print("Sumified Tree")
    tree.printTree()

main()

