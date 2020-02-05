# coding: utf-8

# Binary Tree:
#   A tree whose elements have at most 2 children is called a binary tree. 
#   Since each element in a binary tree can have only 2 children, we typically name them the left and right child.

class Node:

    # Constructor to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def create_tree_example1():
    # Let's show how to create
    #       tree
    #       ----
    #        j    <-- root
    #      /   \
    #     f      k  
    #   /   \      \
    #  a     h      z    <-- leaves 
    root = Node('j')
    root.left = Node('f')
    root.right = Node('k')
    root.left.left = Node('a')
    root.left.right = Node('h')
    root.right.right = Node('z')
    return root

# Tree Traversals

#        j    <-- root
#      /   \
#     f      k  
#   /   \      \
#  a     h      z    <-- leaves 


def print_inorder(root):
    # 1. Inorder <Left, Root, Right> (reucrsively)
    # O(n)
    if not root:
        return
    print_inorder(root.left)
    print(root.val, end=' ')
    print_inorder(root.right)

def print_preorder(root):
    # 2. Preorder <Root, Left, Right> (recursively)
    # O(n)
    if not root:
        return
    print(root.val, end=' ')
    print_preorder(root.left)
    print_preorder(root.right)

def print_postorder(root):
    # 3. Postorder <Left, Right, Root> (recursively)
    # o(n)
    if not root:
        return
    print_postorder(root.left)
    print_postorder(root.right)
    print(root.val, end=' ')

def print_levelorder(root):
    # 4. Levelorder <Lefr

if __name__ == '__main__':
    root = create_tree_example1()
    print('Inorder:', end=' ')
    print_inorder(root)
    print('\nPreorder:', end=' ')
    print_preorder(root)
    print('\nPostorder:', end=' ')
    print_postorder(root)
