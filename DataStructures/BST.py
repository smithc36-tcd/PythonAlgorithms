"""Implementation of Binary Search Tree"""
import unittest


class BSTNode:

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __lt__(self, other):
        if isinstance(other, int):
            return self.data < other
        if isinstance(other, str):
            return self.data < other

    def __eq__(self, other):
        if isinstance(other, int):
            return self.data == other
        if isinstance(other, str):
            return self.data == other

    def insert(self, data):
        """Insert an element recursively into the BST """
        if self.data is None:
            self.data = data
            return

        if (self.data == data):
            return

        if (self.data < data):
            if self.right:
                self.right.insert(data)
                return
            self.right = BSTNode(data)

        else:
            if self.left:
                self.left.insert(data)
                return
            self.left = BSTNode(data)

    def delete(self, data):
        """Delete and element from a tree given its value"""

    def search(self, data):
        """Checking if some element exists"""
        if not self.data:
            return False

        if self.data == data:
            return True

        if self.data < data:
            if self.right:
                return self.right.search(data)
            else:
                return False

        else:
            if self.left:
                return self.left.search(data)
            else:
                return False

    def min(self):
        """Returns min value of BST"""
        current = self
        while current.left is not None:
            current = current.left
        return current.data

    def max(self):
        """Returns max value of BST """
        current = self
        while current.right is not None:
            current = current.right
        return current.data

    def PrintTree(self):
        """print tree"""
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    def inOrder(self):
        inOrdList = []
        if self.data:
            if self.left:
                inOrdList = self.left.inOrder()
            inOrdList.append(self.data)
            if self.right:
                inOrdList = inOrdList + self.right.inOrder()
        return inOrdList

    def preOrder(self):
        preOrdList = []
        if self.data:
            preOrdList.append(self.data)
            if self.left:
                preOrdList = preOrdList + self.left.preOrder()
            if self.right:
                preOrdList = preOrdList + self.right.preOrder()
        return preOrdList

    def postOrder(self):
        postOrderList = []
        if self.data:
            if self.left:
                postOrderList = self.left.postOrder()
            if self.right:
                postOrderList = postOrderList + self.right.postOrder()
            postOrderList.append(self.data)
        return postOrderList


class TestBSTFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(self):
       # set up test for whole class
        nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
        letters = ['l', 'm', 'd', 't', 'q', 'a', 'd', 'p', 'v', 'e', 's']
        self.bst1 = BSTNode()
        self.bst2 = BSTNode()
        for num in nums:
            self.bst1.insert(num)
        for letter in letters:
            self.bst2.insert(letter)

    def test_search(self):
        self.assertEqual(self.bst1.search(19), True)
        self.assertEqual(self.bst1.search(7), False)

    def test_max(self):
        self.assertEqual(self.bst1.max(), 24)

    def test_min(self):
        self.assertEqual(self.bst1.min(), 3)

    def test_InOrder(self):
        """Testing In Order Traversal"""
        InOrder1 = [3, 4, 5, 6, 11, 12, 18, 19, 21, 24]
        InOrder2 = ['a', 'd', 'e', 'l', 'm', 'p', 'q', 's', 't', 'v']
        self.assertEqual(self.bst1.inOrder(), InOrder1)
        self.assertEqual(self.bst2.inOrder(), InOrder2)

    def test_preOrder(self):
        """Testing Pre Order Traversal"""
        preOrder1 = [12, 6, 3, 5, 4, 11, 18, 19, 21, 24]
        preOrder2 = ['l', 'd', 'a', 'e', 'm', 't', 'q', 'p', 's', 'v']
        self.assertEqual(self.bst1.preOrder(), preOrder1)
        self.assertEqual(self.bst2.preOrder(), preOrder2)

    def test_postOrder(self):
        """Testing Post Order Traversal"""
        postOrder1 = [4, 5, 3, 11, 6, 24, 21, 19, 18, 12]
        postOrder2 = ['a', 'e', 'd', 'p', 's', 'q', 'v', 't', 'm', 'l']
        self.assertEqual(self.bst1.postOrder(), postOrder1)
        self.assertEqual(self.bst2.postOrder(), postOrder2)


def main():
    unittest.main()


main()
