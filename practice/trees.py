#+ Trees
# similar to linked lists with nodes that contain data and can be linked to other nodes
# non linear, can have single elements which have multiple next elements allowing data structure to branch out 

# useful for; hierarchial data, databases, routing tables, sorting/searching, priority queues

# first node is called root node
# link between nodes are edges
# parent/internal node has links to child nodes
# nodes without child nodes are called leaf nodes

# Binary Trees
# type of tree data structure where each node can have a maximum of two child nodes; a left and right child node

# Benefits
# algs like traversing, searching, inserion and deletion become easier to understand, implement and run faster
# keeping data sorted in a BST makes searching efficient 
# binary trees can be represented as arrays = memory efficient

# Traversal

# Pre Order traversal 
# - type of Depth First Search (DFS)
# this is done by recursively doing a pre order traversal to the left subtree followed by a recursive pre order traversal of the right subtree 
# used for creating a copy of a tree 

# traversal is "pre" order because the node is visited "before" the recursive pre order traversal of the left and right subtrees 

# In Order traversal
# - type of DFS 
# done by a recursive in order traversal of the left subtree, visiting the root node and then recursive in order traversal of the right subtree 
# mainly usedd in BST where it returns values in ascending order

# traversal in order - the node is visitied between the recursive function calls, the node is visitied after the in order traversal of the left subtree and the before the in order traversal of the right subtree

# Post Order traversal 
# - works by recursively doing a post order traversal of the left subtree and the right subtree, followed by a vist to the root node
# use by deleting a tree, post-fix notation of an expression tree

# traversal is post - visiting a node is done "after" the left and right child nodes are called recursively 