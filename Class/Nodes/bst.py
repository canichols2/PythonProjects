"""Binary Search Tree Objects
"""


class BSTNode(object):
    """A Node with 2  nodes and a value

    Arguments:
        object {value, parent, left, right} --
        The node has 2 ren nodes,
        left and right, and a parent node.
    """

    def __init__(self, val, parent=None, left=None, right=None):
        """Builds the initial node with a value,
        and optional parent and or ren
        """

        self.val = val
        self.parent = parent
        self.left = left
        self.right = right

    def addLeft(self, val):
        self._addLeft(BSTNode(val))

    def _addLeft(self, node: BSTNode):
        """Adds node to left of parent and sets child parent to self

        Arguments:
            node {BSTNode} -- Node to add to left
        """

        node.parent = self
        self.left = node

    def addRight(self, val):
        self._addRight(BSTNode(val))

    def _addRight(self, node: BSTNode):
        """Adds node to right of parent and sets child parent to self

        Arguments:
            node {BSTNode} -- Node to add to right
            
        """

        node.parent = self
        self.right = node

    def getNextValue(self):
        """Returns the value of the next infix node of the right child

        Returns:
            [type] -- Value of the next node
        """

        return self._getNextNode().val

    def _getNextNode(self):
        """Returns the next in order successive node of the right child

        Returns:
            BSTNode -- The next infix Node
        """

        node = self.right
        while node.hasLeft():
            node = node.left
        return node

    def hasLeft(self):
        return self.left

    def hasRight(self):
        return self.right

    def isLeft(self):
        return self.parent and self.parent.left == self

    def isRight(self):
        return self.parent and self.parent.right == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right or self.left)

    def hasAnyChildren(self):
        return self.right or self.left

    def hasBothChildren(self):
        return self.right and self.left

    def getHeight(self):
        """Recursively calculates the hight of the tree
        Returns:
            int -- height of tallest leaf.
        """

        height = 1
        hLeft = self.left.getHeight()
        hRight = self.right.getHeight()
        if hLeft > hRight:
            return height + hLeft
        else:
            return height + hRight


class BST(object):
    """A Binary Search Tree

    Arguments:
        object {obj} -- Builds a tree with methods to add/remove
    """
    def __init__(self):
        self.root = None
        self.size = 0

    def __str__(self):
        """This was going to return a string formatted into a node tree
        using ascii art, but not finished.
        Returns:
            str -- the grahical representation of the tree
        """

        height = ""
        return height

    def add(self, val):
        if self.root:
            self._add(val, self.root)
        else:
            self.root = BSTNode(val)
        self.size += 1

    def _add(self, val, CN: BSTNode):  # CN = CurrentNode
        if val <= CN.val:
            if CN.hasLeft():
                self._add(val, CN.left)
            else:
                CN.left = BSTNode(val, parent=CN)
        else:
            if CN.hasRight():
                self._add(val, CN.right)
            else:
                CN.right = BSTNode(val, parent=CN)

    def remove(self, val):
        self._remove(
            self._findNode(val, self.root)
        )

    def _findNode(self, val, node: BSTNode) -> BSTNode:
        """Finds the first instance of "val" and
        returns the node associated with it. using infix
        Arguments:
            val {[type]} -- the value you are looking for
            node {BSTNode} -- the node for recursion
        Returns:
            BSTNode -- Returns the node you are looking for
        """
        if(node.val is val):
            return node
        if node.val > val:
            return self._findNode(val, node.left)
        else:
            return self._findNode(val, node.right)

    def _remove(self, node: BSTNode):
        """Checks if the node has children and removes the node
        and reorders the rest of the nodes as needed
        Arguments:
            node {BSTNode} -- Node to remove
        """

        if node.hasAnyChildren():
            if node.hasBothChildren():
                node.val = node.getNextValue()
                self._remove(
                    node._getNextNode()
                )
            else:
                if node.hasLeft():
                    if node.isLeft():
                        node.parent._addLeft(node.left)
                    else:
                        node.parent._addRight(node.left)
                else:  # Has Right Child
                    if node.isLeft():
                        node.parent._addLeft(node.right)
                    else:
                        node.parent._addRight(node.right)
        else:
            if node.isLeft():
                node.parent.left = None
            else:
                node.parent.right = None


if __name__ == "__main__":
    l1 = BST()
    l1.add(5)
    l1.add(4)
    l1.add(3)
    l1.add(1)
    l1.add(2)
    l1.add(8)
    l1.add(6)
    l1.add(7)
    l1.remove(8)
    l1.remove(5)
    l1.remove(1)
