# This is Two Sigma interview question.
# For a given tree (not necessarily binary tree), let {1, 2, …, n} be its vertices.
# An array is used to denote the tree, as below:
#     A[i] = parent of i
# Question: for a given node, delete its child tree.
# We can design an O(n) algorithm to mark the nodes that get deleted.
# The idea is to check each node once and only once, by using a “checked” flag for each node.
# 
# Starting from each node, travel up until either root or a deleted node:
# if to root, keep everything along the route;
# if reaching a deleted node, delete all nodes along the route

class Node:
    def __init__(self, index, parent):
        self.index = index
        self.parent = parent
        self.deleted = False
        self.checked = False
    def __str__(self):
        return "Node {0}, parent {1}, deleted {2}, checked {3}".format(
            self.index, self.parent,
            'D' if self.deleted else 'N',
            'Y' if self.checked else 'N')

class Tree:
    def __init__(self):
        self.tree = []
    def add_node(self, node):
        self.tree.append(node)

    def get_node(self, index):
        return self.tree[index-1]
    def get_parent(self, node):
        return self.get_node(node.parent)

    def __str__(self):
        S = ""
        for node in self.tree:
            S = S + str(node) + "\n"
        return S

    def delete_subtree(self, index_to_delete):
        self.get_node(index_to_delete).deleted = True
        self.get_node(index_to_delete).checked = True
        L = []
        for node in self.tree:
            if node.checked: continue
            print "Checking ", node.index
            t = node
            L.append(t)
            t.checked = True
            while t.parent != 0 and not self.get_parent(t).deleted:
                t = self.get_parent(t)
                L.append(t)
                t.checked = True

            if t.parent == 0:
                L[:] = []
            else:
                for n in L:
                    n.deleted = True

if __name__ == "__main__":
    tree = Tree()
    tree.add_node(Node(1, 6))
    tree.add_node(Node(2, 4))
    tree.add_node(Node(3, 0))
    tree.add_node(Node(4, 3))
    tree.add_node(Node(5, 3))
    tree.add_node(Node(6, 7))
    tree.add_node(Node(7, 3))
    tree.add_node(Node(8, 9))
    tree.add_node(Node(9, 7))
    print tree
    tree.delete_subtree(7)
    print tree
