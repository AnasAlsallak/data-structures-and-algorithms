def tree_breadth_first(tree):

    if tree.root is None:
        return []

    result = []
    nodes = [tree.root]

    while nodes:
        # Should always pop the node at index 0 
        current_node = nodes.pop(0)
        result.append(current_node.value)

        if current_node.left:
            nodes.append(current_node.left)
        if current_node.right:
            nodes.append(current_node.right)

    return result
