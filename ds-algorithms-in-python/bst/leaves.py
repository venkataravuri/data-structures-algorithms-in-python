def num_leaves(node):
    count = 0
    if node.left is None and node.right is None:
        count += 1
    if node.left:
        count += num_leaves(node.left)
    elif not node.right is None:
        count += num_leaves(node.right)

    return count

