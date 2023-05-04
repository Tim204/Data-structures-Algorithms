
class BinaryTreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert(self, value):
        if self.value is None:
            self.value = value
            return
        current = self.value

        while True:
            if value < current:
                if self.left_child is None:
                    self.left_child = BinaryTreeNode(value)
                    break
                current = self.left_child
            else:
                if self.right_child is None:
                    self.right_child = BinaryTreeNode(value)
                    break
                current = self.right_child


root = BinaryTreeNode()
root.insert(4)
root.insert(9)
root.insert(1)
root.insert(8)



# Creating node class
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.leftChild = None
#         self.rightChild = None
#
# # Function to insert in BST
#     def insert(self, data):
#         # if value is lesser than the value of the parent node
#         if data < self.data:
#             if self.leftChild:
#                 # if we still need to move towards the left subtree
#                 self.leftChild.insert(data)
#             else:
#                 self.leftChild = Node(data)
#                 return
#         # if value is greater than the value of the parent node
#         else:
#             if self.rightChild:
#                 # if we still need to move towards the right subtree
#                 self.rightChild.insert(data)
#             else:
#                 self.rightChild = Node(data)
#                 return
#
#     # function to print a BST
#     def PrintTree(self):
#         if self.leftChild:
#             self.leftChild.PrintTree()
#         print( self.data),
#         if self.rightChild:
#             self.rightChild.PrintTree()
#
#     # def PrintTree(self):
#     #     if self.left:
#     #         self.left.PrintTree()
#     #     print(self.data),
#     #     if self.right:
#     #         self.right.PrintTree()
#
#
# # Creating root node
# root = Node(27)
# # Inserting values in BST
# root.insert(14)
# root.insert(35)
# root.insert(31)
# root.insert(10)
# root.insert(19)
# # printing BST
# root.PrintTree()