class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#def preOrderTraversal(node):
#    if node is None:
#        return
#    print(node.data, end=", ")
#    preOrderTraversal(node.left)
#    preOrderTraversal(node.right)

#def inOrderTraversal(node):
#    if node is None:
#        return
#    inOrderTraversal(node.left)
#    print(node.data, end=", ")
#    inOrderTraversal(node.right)

#def postOrderTraversal(node):
#    if node is None:
#        return
#    postOrderTraversal(node.left)
#    postOrderTraversal(node.right)
#    print(node.data, end=", ")

root = TreeNode('r')
nodeA = TreeNode('a')
nodeB = TreeNode('b')
nodeC = TreeNode('c')
nodeD = TreeNode('d')
nodeE = TreeNode('e')
nodeF = TreeNode('f')
nodeG = TreeNode('g')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# print("root.right.left.data:", root.right.right.left.data)

# preOrderTraversal(root)

# inOrderTraversal(root)

# postOrderTraversal(root)
