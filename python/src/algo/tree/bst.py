from __future__ import print_function

class Node:
    def __init__(self, data, parent=None):
        self.left = None
        self.right = None
        self.parent = parent
        self.data = data

    def __str__(self):
        return "Node {0} - parent {1} - left {2} - right {3}".format(
            self.data, self.parent.data if self.parent is not None else '/',
            self.left.data if self.left is not None else '/',
            self.right.data if self.right is not None else '/',
        )

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data, self)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data, self)
                else:
                    self.right.insert(data)
            else:
                raise RuntimeError("Key {0} already exist".format(data))
        else:
            print("Why here?")
            self.data = data

    def search(self, key, parent=None):
        '''
        :param key: what to search
        :param parent: node's parent
        :return: node and its parent, or (None, None) if not found
        '''

        if key == self.data:
            return self, parent
        if key < self.data:
            if self.left is None:
                return None, None
            else:
                return self.left.search(key, self)
        if key > self.data:
            if self.right is None:
                return None, None
            else:
                return self.right.search(key, self)

    # To search iteratively
    def search_i(self, key, parent=None):
        node = self
        while node is not None:
            if key == node.data:
                return node, parent
            if key < node.data:
                parent = node
                node = node.left
            else:
                parent = node
                node = node.right
        return None, None

    def min(self):
        node = self
        while node.left is not None:
            node = node.left
        return node

    def successor(self):
        # 1. if it has right child, the successor is the left most of its right child
        if self.right is not None:
            node = self.right
            while node.left is not None:
                node = node.left
            return node

        # 2. if not having right child

        # 2.1 if this is the left child of its parent, successor is its parent
        if self == self.parent.left:
            return self.parent

        # 2.2 if this is the right child of its parent, look up
        while self.parent is not None and self == self.parent.right:
            self = self.parent
        if self.parent is None: return None
        return self.parent

    def replace_node_in_parent(self, new_node=None):
        if self.parent:
            if self == self.parent.left:
                self.parent.left = new_node
            else:
                self.parent.right = new_node
        if new_node:
            new_node.parent = self.parent

    def delete(self, key):
        if key < self.data:
            self.left.delete(key)
        elif key > self.data:
            self.right.delete(key)
        else:       # delete the key here
            if self.left and self.right:        # if both children are present
                successor = self.right.min()
                self.key = successor.key
                successor.delete(successor.key)
            elif self.left:
                self.replace_node_in_parent(self.left)
            elif self.right:
                self.replace_node_in_parent(self.right)
            else:
                self.replace_node_in_parent()

    def print_tree(self):
        if self.left: self.left.print_tree()
        print(self.data, end=", ")
        if self.right: self.right.print_tree()

if __name__ == "__main__":
    root = Node(80)
    root.insert(30)
    root.insert(100)
    root.insert(10)
    root.insert(60)
    root.insert(40)
    root.insert(70)
    root.insert(140)
    root.insert(130)
    root.insert(90)
    root.insert(150)
    root.insert(120)
    root.insert(135)

    root.print_tree()

    print("\nDoing search now ...")
    n, p = root.search(140)
    if p: p.print_tree()

    print("\nDoing search_i now ...")
    n, _ = root.search_i(100)
    if n: n.print_tree()

    print("\nDoing min now ...")
    root.min().print_tree()
    n, _ = root.search_i(60)
    n.min().print_tree()
    print(n)

    print("\nDoing successor now ...")
    n, _ = root.search_i(135)
    if n:
        print("\tThe tree nodes: ", end="")
        n.print_tree()
        print("\n\tThe successor is: {0}".format(n.successor()), end="")

    print("")
