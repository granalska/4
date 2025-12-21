class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def dfs(root):
    if not root:
        return []
    
    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val) 

        #зліва на право
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result

#приклад 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Обхід в глибину(DFS):", dfs(root))