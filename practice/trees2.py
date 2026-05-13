class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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

print("root.right.left.data:", root.right.left.data)

