"""
solution for day 3

pseudocode + notes:

    @see:   https://pythonschool.net/data-structures-algorithms/binary-tree/
            https://algorithm.yuanbin.me/zh-hans/binary_tree/binary_tree_serialization.html
"""

class BinaryTree():
    def __init__(self, rootid):
        self.left = None
        self.right = None
        self.rootid = rootid

    def printTree(self):
        if(self.rootid != None):
            print(self.rootid)
        else:
            print("Tree is empty")


def serialize(mytree):
    return ""

def deserialize(mytree):
    return ""

if __name__ == "__main__":
    mytree = BinaryTree(1)
    mytree.printTree()

    #serialize
    #turn tree into string
    serialize(mytree_tree)
    
    #deserialize
    #turn string into tree
    deserialize(mytree_string)
