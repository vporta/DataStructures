# Binary Search Trees
# Height: the height of a BST - avg: O(log n) - worst: O(n)
# Operation on BST 
# S. No.  Operation   Average Case    Worst Case
# 1       Contains/Search O(log n)    O(n)
# 2       Minimum         O(log n)    O(n)
# 3       Maximum         O(log n)    O(n)
# 4       Predecessor     O(log n)    O(n)
# 5       Successor       O(log n)    O(n)
# 6       Insert          O(log n)    O(n)
# 7       Delete          O(log n)    O(n)

# Traversing
# Use Inorder Traversal when dealing with a binary tree because it allows us to print the values in order

"""
    B
   / \
A       C
""" 
# Inorder
# left, then root, then right 
# A, B, C

# Preorder
# root, then left, then right

# Postorder
# left, then right, then root

# Level Order 
# root level, child level, and so on

# Resources: 
# https://algorithmtutor.com/Data-Structures/Tree/Binary-Search-Trees/
from collections import deque


class Node:

    def __init__(self, value=None, left=None, right=None):
        self.value = value 
        self.left = left
        self.right = right   
        self.size = 0 

    
    def disconnect():
        self.left = None
        self.right = None
        self.parent = None


    def __lt__(self, other):
        return self.value < other.value 


    def __gt__(self, other):
        return self.value > other.value 


    def __eq__(self, other):
        return self.value == other.value 


    # def compare_to(self, other):
    #     if self < other: return -1 
    #     elif self > other: return 1 
    #     else: return 0 


    def __repr__(self):
        return "<Node value = %s, left = %s, right = %s > " % (self.value, self.left, self.right)


class BST:

    def __init__(self, root=None):
        self.root = root 

    def get_root(self):
        return self.root 

    def set_root(self, value):
        self.root = Node(value)

    def insert(self, value):
        """ tc: 
                - avg: O(log n)
                - worst: O(n) 
        """
        def _insert(node, value):
            if node is None:
                return Node(value)
            elif value == node.value:
                return None 
            elif value < node.value:
                node.left = _insert(node.left, value)
                node.parent = self.root
            elif value > node.value:
                node.right = _insert(node.right, value)
                node.parent = self.root 
            return node 
        self.root = _insert(self.root, value)
        return self.root is not None 


    def contains(self, value):
        def _contains(node, value):
            return (
                False if node is None else
                _contains(node.left, value) if value < node.value else
                _contains(node.right, value) if value > node.value else
                True
            )
        return _contains(self.root, value)


    def rank(self, value):
        if value is None: return "argument to rank() is None"
        return self._rank(value, self.root)


    def _rank(self, value, node):
        if node is None: return 0 
        # -1 if node.value > value. 1 if node.value < value. 0 if equal. 
        _cmp = self._compare_to(node.value, value)
        if _cmp < 0: return self._rank(value, node.left)
        elif _cmp > 0:  return 1 + self._size(node.left) + self._rank(value, node.right)
        else: return self._size(node.left) 


    def search(self, value):
        def _search(node, value):
            return (
                "None such node" if node is None else
                _search(node.left, value) if value < node.value else
                _search(node.right, value) if value > node.value else
                node.value
            )
        return _search(self.root, value)


    def minimum(self):
        return self._minimum(self.root).value 


    def _minimum(self, node):
        if node.left is None: return node 
        return self._minimum(node.left)
        """
        iterative approach:
        current = node
        if current is None: return -1  
        while current.left is not None:
            current = current.left
        return current
        """


    def maximum(self):
        return self._maximum(self.root).value


    def _maximum(self, node):
        if node.right is None: return node 
        return self._maximum(node.right)


    def predecessor(self, value):
        """
        Returns the largest key in the BST less than or equal to {@code value}. 
        If the left subtree of node x is non-empty, then the successor of x is just the rightmost node in x‘s left subtree.
        If the left subtree of node x is empty and x has a successor y, then y is the lowest ancestor of x whose right child is also an ancestor of x.
        """
        def _predecessor(node, value):
            if node.left is not None:
                return self._maximum(node.left)
            y = node.parent 
            while y is not None and node == y.left:
                node = y 
                y = y.parent 
            return y 
        return _predecessor(self.root, value)

    def successor(self, value):
        """
        Returns the smallest key in the BST greater than or equal to {@code value}
        If the right subtree of node x is non-empty, then the successor of x is just the leftmost node in x‘s right subtree.
        If the right subtree of node x is empty and x has a successor y, then y is the lowest ancestor of x whose left child is also an ancestor of x.
        """

        def _successor(node, value):
            if node.right is not None:
                return self._minimum(node.right)
            y = node.parent
            while y is not None and node == y.right:
                node = y 
                y = y.parent
            return y
        return _successor(self.root, value)

        
    def _compare_to(self, node_value, value):
        _cmp = None
        if node_value < value:
            _cmp = 1  
        elif node_value > value:
            _cmp = -1 
        else:
            _cmp = 0 
        return _cmp 


    def delete(self, value):
        if value is None: return "calls delete() with a null key"
        self.root = self._delete(self.root, value) 


    def _delete(self, node, value):
        if node is None: return None 
        _cmp = self._compare_to(node.value, value)
        if _cmp < 0:
            node.left = self._delete(node.left, value)
        elif _cmp > 0: 
            node.right = self._delete(node.right, value)
        else: 
            if node.right is None: return node.left 
            if node.left is None: return node.right 
            t = node 
            node = self._minimum(t.right)
            node.right = self._delete_min(t.right)
            node.left = t.left 
        return node 

    
    def delete_min(self):
        if self.is_empty(): return "BST underflow"
        self.root = self._delete_min(self.root)


    def _delete_min(self, node):
        if node.left is None: return node.right 
        node.left = self._delete_min(node.left)
        # node.size = self._size(node.left) + self._size(node.right) + 1
        return node 

                                                       
    def delete_max(self):
        if self.is_empty(): return "BST underflow"
        self.root = self._delete_max(self.root)


    def _delete_max(self, node):
        if node.right is None: return node.left 
        node.right = self._delete_max(node.right)
        # node.size = self._size(node.left) + self._size(node.right) + 1
        return node


    def is_empty(self):
        return self.size() == 0


    def size(self):
        return self._size(self.root)


    def _size(self, node):
        if node is None: return 0 
        return 1 + self._size(node.left) + self._size(node.right)

    
    def height(self):
        return self._height(self.root)


    def _height(self, node):
        if node is None: return -1 
        return 1 + max(self._height(node.left), self._height(node.right))

    
    def min_depth(self):
        return self._min_depth(self.root) 


    def _min_depth(self, node):
        if node is None: return -1 
        if node.left is None and node.right is None: return 1 
        if node.left is None: 
            return self._min_depth(node.right) + 1
        if node.right is None: 
            return self._min_depth(node.left) + 1
        return min(self._min_depth(node.left), self._min_depth(node.right)) + 1


    def find_depth_of_node(self, value):
        return self._find_depth_of_node(self.root, value)


    def _find_depth_of_node(self, node, value):
        if not node: raise ValueError('Tree must contain a root value.')
        if node.value == value: return 0
        return 1 + min(self._find_depth_of_node(node.left, value), self._find_depth_of_node(node.right, value))


    def is_BST(self):   
        def _is_BST(root, min_value, max_value):
            if root is None:
                return True 
            if root.value > min_value and root.value < max_value and _is_BST(root.left, min_value, root.value) and _is_BST(root.right, root.value, max_value):
                return True 
            else:
                return False 
        return _is_BST(self.root, float('-inf'), float('inf'))
        # def _height(node):
        #     if node is None: return 0 
        #     left_height = _height(node.left)
        #     right_height = _height(node.right)

        #     if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
        #         return -1 
        #     return 1 + max(_height(node.left), _height(node.right))

        # return _height(self.root) != -1         


    # Traversals
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)
        return 


    def preorder(self, node):
        if node:
            print(node.value)
            self.preorder(node.left)
            self.preorder(node.right)
        return 

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value)
        return 


    def level_order(self):
        """ Print Nodes level by level. """
        keys = deque()
        queue = deque()
        queue.append(self.root)
        while queue:
            x = queue.popleft()
            if x is None: continue
            keys.append(x.value)
            queue.append(x.left)
            queue.append(x.right)
        return keys 


    def __str__(self):
        return '<BST(root = %s)>' % (self.root)


def main():
    t = BST()
    # t.set_root(5)
    t.insert(10)
    t.insert(5)
    t.insert(1)
    t.insert(6)
    t.insert(14)
    t.insert(12)
    t.insert(16)

    print(t)
    print('search', t.search(50))
    print('size', t.size())
    print('contains', t.contains(10))
    print('inorder', t.inorder(t.root))
    print('pre order', t.preorder(t.root))
    print('post orde r', t.postorder(t.root))
    print('level order', t.level_order())
    print('minimum', t.minimum())
    print('maximum', t.maximum())
    # print('delete', t.delete(5))
    print('predecessor', t.predecessor(10))
    print('successor', t.successor(10))
    print('height', t.height())
    print('is_BST()', t.is_BST())
    # print('delete_min', t.delete_min())
    # print('delete_max', t.delete_max())
    print('size', t.size())
    print('rank', t.rank(8))
    print(t)
main()











