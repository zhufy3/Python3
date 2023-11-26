import sys

def to_CBST(a):
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def store_keys_inorder(node, keys):
        if node is None:
            return
        store_keys_inorder(node.left, keys)
        keys.append(node.key)
        store_keys_inorder(node.right, keys)

    def convert_tree_to_bst(node, keys):
        if node is None:
            return
        convert_tree_to_bst(node.left, keys)
        node.key = keys[0]
        keys.pop(0)
        convert_tree_to_bst(node.right, keys)


    def binary_tree_to_bst(root):
        keys = []
        store_keys_inorder(root, keys)   # Step 1
        keys.sort()   # Step 2
        convert_tree_to_bst(root, keys)  # Step 3


    def preorder_traversal(root, result):
        if root:
            result.append(root.key)
            preorder_traversal(root.left, result)
            preorder_traversal(root.right, result)
        return result


    nod=[]
    def test_binary_tree_to_bst(a):
        nodes = {}
        for line in a:
            key, left, right = line[0],line[1],line[2]
            if key not in nodes:
                nodes[key] = Node(int(key))
                nod.append(key)
            if left != 'x':
                nodes[left] = nodes.get(left, Node(int(left)))
                nodes[key].left = nodes[left]
                if left in nod:
                    nod.remove(left)
            if right != 'x':
                nodes[right] = nodes.get(right, Node(int(right)))
                nodes[key].right = nodes[right]
                if right in nod:
                    nod.remove(right)
        root = nodes[nod[0]]
        binary_tree_to_bst(root)
        return preorder_traversal(root, [])
    return test_binary_tree_to_bst(a)


num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [s.split(':') for s in sys.stdin.readline().split()]
    print(*to_CBST(a),sep=' ')
