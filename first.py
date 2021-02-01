# binary tree - serialize

#   1
#    /\
#  2    3
#  /
# 4 -1 -1  5
#
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def __int__(self, head=None):
        self.head = head

def serialize(treeHead):
    str = []
    if treeHead != None:
        str.append(treeHead.data)
        str.append(" ")
    else:
        str.append(-1)

    left_str = serialize(treeHead.left)
    right_str = serialize(treeHead.right)

    return str + left_str + right_str


start = Node(1)
start.left = Node(3)

myTree = Tree(start)
print(serialize(start))
