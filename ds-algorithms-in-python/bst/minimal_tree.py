# We’re given a sorted array(ascending order) with unique integer elements.
# Write an algorithm to create a binary search tree with minimal height.
# Credits https://pythonwife.com/interview-questions-on-trees-in-python/

#Initializing the Binary Search Tree class
class BSTNode:
    def __init__(self, data=None, left = None, right= None):
        self.data = data
        self.left = left
        self.right = right


#Function to create a binary search tree of minimum height
def minimalTree(sortedArray):
    if len(sortedArray) == 0:
        return None
    if len(sortedArray) == 1:
        return BSTNode(sortedArray[0])
    mid = int(len(sortedArray)/2)
    left = minimalTree(sortedArray[:mid])
    right = minimalTree(sortedArray[mid+1:])
    return BSTNode(sortedArray[mid], left, right)

sortedArray = [1,2,3,4,5,6,7,8,9]
bst = minimalTree(sortedArray)