# Binary tree Module to implement Binary Tree.
print()

import binarytree

root=binarytree.Node(10)
root.left=binarytree.Node(20)
root.right=binarytree.Node(30)

print(root)

print()

print('Inorder of Nodes',root.inorder)
print('Postorder of Nodes',root.postorder)
print('Preorder of Nodes',root.preorder)

print()

print('Size',root.size)

print('Height of Tree',root.height)