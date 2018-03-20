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


class BST(object):
    """A Binary Search Tree

    Arguments:
        object {obj} -- Builds a tree with methods to add/remove
    """
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, val):
        None

    def _add(self, val, CN):  # CN = CurrentNode
        if val <= CN.val:
            if CN.hasLeft():
                self._add(val, CN.left)
            else:
                CN.Left = BSTNode(val, parent=CN)
        else:
            if CN.hasRight():
                self._add(val, CN.right)
            else:
                CN.right = BSTNode(val, parent=CN)
