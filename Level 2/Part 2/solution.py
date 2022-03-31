#I used my college Data Structure course notes and online articles about perfect binary trees to solve this challenge

def solution(h, q):
    maxNode = 2**h - 1
    perfTree = Node()
    for i in range(1, maxNode):
        perfTree.add()
    postOrderLabel(perfTree)
    finalList = search(perfTree, q, maxNode)
    print(finalList)

def search(root, keys, maxNode):
    def helper(root, key):
        if root.left:
            if root.left.label == key or root.right.label == key:
                positions.append(root.label)
            else: 
                helper(root.left, key)
                helper(root.right, key)
    positions = []
    for key in keys:
        if key == maxNode:
            positions.append(-1)
        else:
            helper(root, key)
    return positions


def postOrderLabel(root):
    qu = []
    def helper(root):
        if root:
            helper(root.left)
            helper(root.right)
            qu.append(root)
    helper(root)
    for i in reversed(range(1, len(qu) + 1)):
        qu.pop().label = i

class Node:
    def __init__(self):
            self.size = 1
            self.left = None
            self.right = None
            self.label = 0

    def add(self):
        if(self.left == None):
            self.left = Node()
            self.size += 1
        elif (self.right == None):
            self.right = Node()
            self.size += 1
        else:
            if(self.goLeft()): 
                self.left.add()
                self.size += 1
            else:
                self.right.add()
                self.size += 1

    def goLeft(self):
        h = 2
        temp = self.left
        while(temp.left):
            h += 1
            temp = temp.left
        leaves = 2**(h - 1)
        leavesIfFull = 2**h - 1
        emptySlots = leavesIfFull - self.size

        if emptySlots == 0:
            return True
        else:
            return (leaves/2) > (leaves - emptySlots)