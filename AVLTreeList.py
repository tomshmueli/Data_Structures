# username - einatgelbort and tomshmueli
# id1      - 208275651
# name1    - einat gelbort
# id2      - 315363473
# name2    - tom shmueli

"""A class represnting a node in an AVL tree"""
import random

class AVLNode(object):
    """Constructor, you are allowed to add more fields.
        @type value: str
        @param value: data of your node
        """

    def __init__(self, value=False):
        if value is False:
            self.real_node = False
            self.value = value
            self.left = None
            self.right = None
            self.parent = None
            self.height = -1
            self.size = 0  # size of the subtree including self
        else:
            r_son = AVLNode()
            l_son = AVLNode()
            self.real_node = True
            self.value = value
            self.left = r_son
            self.right = l_son
            self.parent = None
            self.height = 0
            self.size = 1
            r_son.setParent(self)
            l_son.setParent(self)

    """returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""

    def getLeft(self):
        return self.left

    """returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""

    def getRight(self):
        return self.right

    """returns the parent

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""

    def getParent(self):
        return self.parent

    """return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""

    def getValue(self):
        return self.value if self.isRealNode() else None

    """returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""

    def getHeight(self):
        h = -1
        if self.real_node:
            h =  max(self.getRight().height, self.getLeft().height) + 1
        return h

    """returns the size

    @rtype: int
    @returns: the size of self, 0 if the node is virtual
    """

    def getSize(self):
        s = 0
        if self.isRealNode():
            s = self.getLeft().size + self.getRight().size + 1
        return  s

    """sets left child

	@type node: AVLNode
	@param node: a node
	"""

    def setLeft(self, node):
        if node is None:
            node = AVLNode()
        self.left = node
        node.setParent(self)

    """sets right child

	@type node: AVLNode
	@param node: a node
	"""

    def setRight(self, node):
        if node is None:
            node = AVLNode()
        self.right = node
        node.setParent(self)

    """sets parent

	@type node: AVLNode
	@param node: a node
	"""

    def setParent(self, node):
        self.parent = node

    """sets value

	@type value: str
	@param value: data
	"""

    def setValue(self, value):
        self.value = value
        if value != False:
            self.setRealNode(True)

    def setRealNode(self, real_node):
        self.real_node = real_node

    """sets the balance factor of the node

	@type h: int
	@param h: the height
	"""

    def setHeight(self, h):
        self.height = h
    def setSize(self, s):
        self.size = s

    """returns whether self is not a virtual node

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""

    def isRealNode(self):
        return self.real_node

    def isLeaf(self):
        if self.getRight() is None:
            self.setRight(AVLNode())
        if self.getLeft() is None:
            self.setLeft(AVLNode())
        return not self.getLeft().isRealNode() and not self.getRight().isRealNode()

    def isCriminalNode(self):
        if self.isLeaf():
            return False
        return abs(self.getLeft().getHeight() - self.getRight().getHeight()) >= 2

    def getBF(self):
        if self.getLeft() is None:
            self.setLeft(AVLNode())
        if self.getRight() is None:
            self.setRight(AVLNode())
        return self.getLeft().getHeight() - self.getRight().getHeight()

"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
    """
        Constructor function for AVLTreeList
        @:type: root --> AVLNode()
        @:type: first_node --> AVLNode()
        @:type: last_node --> AVLNode()
    """
    def __init__(self, root=AVLNode()):
        self.root = root
        self.first_node = root
        self.last_node = root

    """insert AVLNode with the given value to the end of the list 
	@type val: str
	@param val: the value we insert
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
    """
    def append(self, val):  # FOR TESTSING PURPOSE
        return self.insert(self.length(), val)

    """returns the value of the first item in the list
    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """
    def first(self):
        return self.first_node.getValue()

    """returns the value of the last item in the list
    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """
    def last(self):
        return self.last_node.getValue()

    """update the last node in the list
    @type node: AVLNode
    @param node: the new node that is the last item
    """
    def setLast(self, node):
        self.last_node = node

    """update the first node in the list
    @type node: AVLNode
    @param node: the new node that is the first item
    """
    def setFirst(self, node):
        self.first_node = node

    """returns whether the list is empty
    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """
    def empty(self):
        return not self.getRoot().isRealNode()

    """returns the root of the tree representing the list
    @rtype: AVLNode
    @returns: the root, virtual node if the list is empty
    """
    def getRoot(self):
        return self.root

    """update the root node of the tree representing the list
    @type node: AVLNode
    @param node: the new node that is the root
    """
    def setRoot(self, node):
        self.root = node


    """returns the Height of the tree
    @rtype: int
    @returns: height of the root, if the list is empty return 0
    """
    def getTreeHeight(self):
        return self.getRoot().getHeight() if not self.empty() else 0

    """returns the size of the list
    @rtype: int
    @returns: the size of the list, if the list is empty return 0
    """
    def length(self):
        return self.getRoot().getSize()

    """returns the minimum of the AVL
    @rtype: AVLNODE
    @returns: the first node in an inorder list of the AVL tree
    """
    def setFields(self, node):
        node.setSize(node.left.size + node.right.size + 1)
        node.setHeight(max(node.left.height, node.right.height) + 1)

    """ returns the first node in inorder list of the AVLTreeList 
        @:param sub_root: current root to start from 
        @rtype: AVLNode
    """
    def Min(self, sub_root=None):
        if sub_root is None:
            if not self.getRoot().isRealNode():
                return None
            p = self.getRoot()
            while p.getLeft().isRealNode():
                p = p.getLeft()
            return p
        else:
            if not sub_root.isRealNode():
                return None
            p = sub_root
            while p.getLeft().isRealNode():
                p = p.getLeft()
            return p

    """ returns the last node in inorder list of the AVLTreeList 
       @:param sub_root: current root to start from 
       @rtype: AVLNode
   """

    def Max(self, sub_root=None):
        if sub_root is None:
            if not self.getRoot().isRealNode():
                return None
            p = self.getRoot()
            while p.getRight().isRealNode():
                p = p.getRight()
            return p
        else:
            if not sub_root.isRealNode():
                return None
            p = sub_root
            while p.getRight().isRealNode():
                p = p.getRight()
            return p

    """returns the following node in the inorder list of AVLTreeList
    @:param x: AVLNode
    @pre AVLNODE == real_node
    @rtype: AVLNODE
    @:return: the successor of the node
    """

    def successor(self, x: AVLNode):
        max_node = self.Max()
        if max_node is None or max_node == x:   # x has no successor
            return None
        if x.getRight().isRealNode():
            right_subtree = x.getRight()
            return self.Min(right_subtree)
        y = x.getParent()
        while y.isRealNode() and y.getRight() == x:
            x = y
            y = x.getParent()
        return y

    """returns the previous node in the inorder list of AVLTreeList
   @:param x: AVLNode
   @pre AVLNODE == real_node
   @rtype: AVLNODE
   @:return: the predecessor of the node
   """

    def predecessor(self, x: AVLNode):
        if not self.getRoot().isRealNode():
            return None
        if self.Min(self.getRoot()) == x:
            return None
        if x.getLeft().isRealNode():
            left_subtree = x.getLeft()
            return self.Max(left_subtree)
        y = x.getParent()
        while y.isRealNode() and y.getLeft() == x:
            x = y
            y = x.getParent()
        return y

    """recursive function for returning the i'th node in the AVLTreeList
    
    	@param i: index in the list
    	@param node: current AVLNode
    	@rtype: AVLNode
    	@returns: the Node in the i'th place in the list
    """

    def recRetrieve(self, node, i):
        if not node.isRealNode():
            return None
        if node.getSize() <= i:
            return None
        l_child = node.getLeft()
        r_child = node.getRight()
        l_size = l_child.getSize()
        if l_size == i:  # if looking for root
            return node

        if i > l_size:
            return self.recRetrieve(r_child, i - l_size - 1)
        if i < l_size:
            return self.recRetrieve(l_child, i)

    """retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""

    def retrieve(self, i):
        node = self.recRetrieve(self.getRoot(), i)
        return None if node is None else node.getValue()

    """inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

    def insert(self, i, val):
        if i == self.getRoot().getSize():
            if self.getRoot().getSize() == 0:  # create new tree
                new_node = AVLNode(val)
                self.setRoot(new_node)
                self.first_node = self.getRoot()
                self.last_node = self.getRoot()
                parent = None
                prev_height = 0
            else:  # add at end
                max_node = self.Max()
                prev_height = max_node.getHeight()
                parent = max_node
                new_node = AVLNode(val)
                max_node.setRight(new_node)
        else:
            next_node = self.recRetrieve(self.getRoot(), i)
            if next_node is None:  # edge case --> next_node is root
                next_node = self.getRoot()
            if not next_node.getLeft().isRealNode():
                new_node = AVLNode(val)
                prev_height = next_node.getHeight()
                parent = next_node
                next_node.setLeft(new_node)
            else:
                predecessor = self.predecessor(next_node)
                prev_height = predecessor.getHeight()
                parent = predecessor
                new_node = AVLNode(val)
                predecessor.setRight(new_node)
        counter = self.fixAndUpdateAVLTree(parent, prev_height)
        if self.first_node.getLeft().isRealNode():
            self.first_node = self.first_node.getLeft()
        if self.last_node.getRight().isRealNode():
            self.last_node = self.last_node.getRight()
        return counter

    """Update the tree size and height for each relevant node, 
        reblancing the AVLTree in case is needed
     	@type node: AVLNode
     	@param node: The node that we start from to update field and reblancing if needed
     	@type prev_height: int
     	@param prev_height: the height of this node before modify the sub_tree below
     	@rtype: int
	    @returns: the number of rebalancing operation due to AVL rebalancing
     """

    def fixAndUpdateAVLTree(self, node, prev_height):
        counter = 0
        while node is not None and node.isRealNode():
            if not self.shouldCheckRotate(node, prev_height):
                while node is not None:
                    node.setSize(node.getSize())
                    node = node.getParent()
                return counter

            prev_height = node.getParent().getHeight() if node.getParent() else None
            if node.isCriminalNode():
                (rotate_number, top_node) = self.rotate(node)
                node = top_node
                counter += rotate_number
            else:
                node.setHeight(node.getHeight())
                node.setSize(node.getSize())
            node = node.getParent()
        return counter

    """Check if we should check rotate for this node or above
        The criteria are : if the node is criminal node 
            or the height of this node has changed after modification
    	@type node: AVLNode
    	@param node: The node that we should check for rotate option
    	@type prev_height: int
    	@param prev_height: the height of this node before modify the sub_tree below
    	@rtype: boolean
    	@returns: True if there is any option that we should rotate in this tree, else False
    """

    def shouldCheckRotate(self, node, prev_height):
        return node.isCriminalNode() or prev_height != node.getHeight()

    """Rotate the edge below the given node in order to rebalancing the AVLTree
    	@type node: AVLNode
    	@param node: The node that we should rotate below and balance the subTree
    	@rtype: Topule. The first index - counter from type int
    	                The second index - topNode from type AVLNode
    	@returns: Topule of the counter and topNode. 
    	    Counter is the rebalncing operations due to the specific node
    	     topNode - the AVLNode that after the rotations is the top for this subTree
    """

    def rotate(self, node):
        if node.getBF() == -2:
            child_node = node.getRight()
            if child_node.getBF() < 0:
                # lace to right
                self.rotateOnce(node, child_node, "l")
                counter = 1
            else:
                # child to right and then left
                deep_node = child_node.getLeft()
                self.rotateOnce(child_node, deep_node, "r")
                self.rotateOnce(node, deep_node, "l")
                counter = 2
        else:
            child_node = node.getLeft()
            if child_node.getBF() > 0:
                # lace to left
                self.rotateOnce(node, child_node, "r")
                counter = 1
            else:
                # child to left and then right
                deep_node = child_node.getRight()
                self.rotateOnce(child_node, deep_node, "l")
                self.rotateOnce(node, deep_node, "r")
                counter = 2
        # the order of the update is from bottom to top
        node.setHeight(node.getHeight())
        child_node.setHeight(child_node.getHeight())
        if counter == 2:
            top_node = deep_node
            deep_node.setHeight(deep_node.getHeight())
        else:
            top_node = child_node
        if self.getRoot().getParent() is not None:
            self.setRoot(self.getRoot().getParent())

        return counter, top_node

    """rotate the tree in order to balance it after crating criminal node
    	@type node: AVLNode
    	@param node: The upper node in the edge that we should rotate
    	@type child_node: AVLNode
    	@param child_node: The down node in the edge that we should rotate
    	@type direction: str
    	@pre: "l" == direction or "r" == direction
    	@param direction: The direction to rotate the edge between the given nodes
    """
    def rotateOnce(self, node, child_node, direction):
        parent = node.getParent()
        if parent is not None:
            if parent.getRight() == node:
                parent.setRight(child_node)
            else:
                parent.setLeft(child_node)
        else:
            child_node.setParent(None)
        if direction == "l":
            l_child_node = child_node.getLeft()
            child_node.setLeft(node)
            node.setRight(l_child_node)  # current can be virtual or not
        else:
            r_child_node = child_node.getRight()
            child_node.setRight(node)
            node.setLeft(r_child_node)
        node.setSize(node.getSize())
        node.setHeight(node.getHeight())
        child_node.setSize(child_node.getSize())  # current can be virtual or not
        child_node.setHeight(child_node.getHeight())  # current can be virtual or not

    """deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@type inner_delete: boolean
	@param inner_delete: identify its regual delete or innerDelete. he intended index in the list to be deleted
	    innerDelete is the case when we delete node with two keys and then we delete the successor node
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

    def delete(self, i, inner_delete=False):
        if inner_delete == False:
            to_del = self.recRetrieve(self.getRoot(), i)
            if to_del is None:
                return -1
        else:
            to_del = i
        parent = to_del.getParent()
        if to_del.isLeaf():  # delete to_del
            if parent is not None:
                prev_height = parent.getHeight()
                if parent.getRight() is to_del:
                    parent.setRight(AVLNode())
                else:
                    parent.setLeft(AVLNode())
            else:  # tree had 1 node
                prev_height = 0
                self.setRoot(AVLNode())
        elif not to_del.getLeft().isRealNode() or not to_del.getRight().isRealNode():  # to_del has 1 son
            if parent is not None:
                prev_height = parent.getHeight()
                if parent.getRight() is to_del:
                    if to_del.getRight().isRealNode():
                        parent.setRight(to_del.getRight())
                    else:
                        parent.setRight(to_del.getLeft())
                else:  # to_del is left son
                    if to_del.getRight().isRealNode():
                        parent.setLeft(to_del.getRight())
                    else:
                        parent.setLeft(to_del.getLeft())
            else:
                new_root = to_del.getLeft() if to_del.getLeft().isRealNode() else to_del.getRight()
                self.setRoot(new_root)
                prev_height = self.getRoot().getHeight() - 1
                self.getRoot().setParent(None)
        else:  # to_del has 2 sons
            successor = self.successor(to_del)
            parent = successor.getParent()
            prev_height = parent.getHeight()
            to_del.setValue(successor.getValue())
            self.delete(successor, True)

        parent = parent if parent is not None else self.getRoot()
        if inner_delete == False:
            counter = self.fixAndUpdateAVLTree(parent, prev_height)
            # if we delete the first or the last it will be leaf. it will work also if the tree is empty
            if i == 0:
                successor = self.successor(to_del)
                self.first_node = successor if successor is not None else AVLNode()
            if self.length() <= 1:
                self.last_node = self.getRoot()
                return 0
            if i == self.length():
                if parent.getValue() == to_del.getValue():
                    self.last_node = parent
                else:
                    predecessor = self.predecessor(to_del)
                    self.last_node = predecessor if predecessor is not None else AVLNode()
            if self.length() == 0:
                return 0
            return counter

    """
    transforms AVLTreeList into regular array using recursive helper function
    @pre: self.root.size >= 1
	@rtype: list
	@returns: a list representing AVLTreeList
	"""

    def listToArray(self):
        if self.length() == 1:
            return [self.getRoot().getValue()]
        return self.listToArrayRec(self.getRoot(), [], self.length())

    """
    returns an array representing list of in order scan until specific node
    using recurstion on subtrees
    
    @param node: The current node
    @type val: AVLNode
    @param array: the desired array
    @type array: List
    @param size: length of the List (determined by size of original root)
    @type size: int
    @rtype: list
    @returns: array
    """
    def listToArrayRec(self, node, array, size):
        if not node.isRealNode():
            return None
        if node.isLeaf():
            array.append(node.getValue())
            return None
        self.listToArrayRec(node.getLeft(), array, size)
        array.append(node.getValue())
        self.listToArrayRec(node.getRight(), array, size)
        return array

    """sort the info values of the list
    @rtype: AVLTreeList
    @returns: an AVLTreeList where the values are sorted by the info of the original list.
    """
    def sort(self):
        sort_array = self.mergeSortRec(self.getRoot())
        return self.buildTree(sort_array)

    """merge in sorted way between two sorted list and values
      @param lList: sorted array that representing the sorted value of the left sub tree
      @pre: lList[i-1] < lList[i] < lList[i+1] and none in the beginning of the list
      @param rList: sorted array that representing the sorted value of the right sub tree
      @pre: rList[i-1] < rList[i] < rList[i+1] and none in the beginning of the list
      @type val: int
      @param val: the value of the node
     @rtype: list
     @returns: a list where the values are sorted, the none values appear in the beginning of the list
     """
    def mergeSort(self, lList, rList, val):
        mergeList = []
        lPointer = 0
        rPointer = 0
        none_counter = 0
        valInserted = False

        if val is None:
            none_counter += 1
            valInserted = True

        while rPointer < len(rList) and lPointer < len(lList):
            if lList[lPointer] is None:
                lPointer += 1
                none_counter += 1
            elif rList[rPointer] is None:
                rPointer += 1
                none_counter += 1
            elif lList[lPointer] < rList[rPointer]:
                if not valInserted and val < lList[lPointer]:
                    mergeList.append(val)
                    valInserted = True
                mergeList.append(lList[lPointer])
                lPointer += 1
            else:
                if not valInserted and val < rList[rPointer]:
                    mergeList.append(val)
                    valInserted = True
                mergeList.append(rList[rPointer])
                rPointer += 1
        while rPointer < len(rList):
            if rList[rPointer] is None:
                none_counter += 1
            elif not valInserted and val < rList[rPointer]:
                mergeList.append(val)
                valInserted = True
            mergeList.append(rList[rPointer])
            rPointer += 1
        while lPointer < len(lList):
            if lList[lPointer] is None:
                none_counter += 1
            if not valInserted and val < lList[lPointer]:
                mergeList.append(val)
                valInserted = True
            mergeList.append(lList[lPointer])
            lPointer += 1
        if (not valInserted):
            mergeList.append(val)
        if none_counter ==0:
            return mergeList
        return [None] * none_counter + mergeList


    """sort the info values of the subtree for the specific node 
       @type node: AVLNode
       @param node: the node that we sorted the subtree for
      @rtype: list
      @returns: a list where the values are sorted by the info of the original list in this subtree.
       The none values appear in the beginning of the list
      """
    def mergeSortRec(self, node):
        if not node.isRealNode():
            return []
        if node.isLeaf():
            return [node.getValue()]
        currValue = node.getValue()
        lArray = self.mergeSortRec(node.getLeft())
        rArray = self.mergeSortRec(node.getRight())
        return self.mergeSort(lArray, rArray, currValue)

    """Build tree from Inorder list
    @:type array_t: List
    @param: array_t an Inorder list of values to build tree from
    @rtype: list
    @returns: AVLTreeList
    """

    def buildTree(self, array_t):
        new_tree = AVLTreeList()
        if len(array_t) == 0:
            return new_tree
        n_root = self.buildTreeRec(array_t, 0, len(array_t) - 1)
        new_tree.root = n_root
        new_tree.first_node = new_tree.Min()
        new_tree.last_node = new_tree.Max()
        return new_tree

    """recursive helper function for buildTree 
    @:type: array_t: List
    @param: array_t --> list to build AVLTreeList from
    @:type r,l: int
    @param: r,l --> right and left boundaries of the sub array
    @rtype: AVLNode
    @returns: an AVLNode that is the root of the built tree
    """

    def buildTreeRec(self, array_t, l, r):
        median = (l + r) // 2
        curr = AVLNode(array_t[median])

        if r > median:
            curr.setRight(self.buildTreeRec(array_t, median + 1, r))
        if median > l:
            curr.setLeft(self.buildTreeRec(array_t, l, median - 1))
        self.setFields(curr)

        return curr

    """
    converts the AVLTreeList to a List, permutates the values in the List
    using Randomness ,and builds a new tree from the permutated List using BuildTree function  
       
    @rtype: AVLTreeList
    @returns: new AVLTreeList with the same values in permutated order
    """

    def permutation(self):
        self_arr = self.listToArray()
        perm_arr = []
        n = len(self_arr)
        index_lst = random.sample(range(0, n), n)
        for i in index_lst:
            perm_arr.append(self_arr[i])
        return self.buildTree(perm_arr)


    """
    updates height,size fields for node and all of his ancessters 
    helper function for concat.
    @pre : node != None
    @type node: AVLNode
    """

    def updateFields(self, node):
        while node is not None:
            curr_height = max(node.getRight().getHeight(), node.getLeft().getHeight())
            curr_size = node.getRight().getSize() + node.getLeft().getSize()
            node.setSize(curr_size + 1)
            node.setHeight(curr_height + 1)
            node = node.getParent()

    """
    joins together two AVLTreeLists

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def concat(self, other_tree):
        # edge cases - one of the trees is empty
        if self.empty():
            self.setRoot(other_tree.root)
            self.first_node = other_tree.first_node
            self.last_node = other_tree.last_node
            return other_tree.getTreeHeight()
        if other_tree.empty():
            return self.getTreeHeight()

        x = AVLNode("x")  # x is the combining parent - will be deleted later
        diff_heights = abs(self.getTreeHeight() - other_tree.getTreeHeight())
        self_size = self.length()
        if self.getTreeHeight() == other_tree.getTreeHeight():
            x.setLeft(self.getRoot())
            x.setRight(other_tree.getRoot())
            self.setRoot(x)

        elif self.getTreeHeight() > other_tree.getTreeHeight():  # climb on self, connect x with other's root from right
            a = self.Max()
            while a.getHeight() <= other_tree.getTreeHeight():
                a = a.getParent()
            a_dad = a.getParent()
            x.setLeft(a)
            x.setRight(other_tree.getRoot())
            if a_dad is None:  # if x is root
                self.setRoot(x)
            else:
                a_dad.setRight(x)

        else:  # other is higher than self --> climb on other, connect x with self's root from left
            b = other_tree.Min()
            while b.getHeight() <= self.getTreeHeight():
                b = b.getParent()
            b_dad = b.getParent()
            x.setRight(b)
            x.setLeft(self.getRoot())
            if b_dad is None:  # if x should be new root
                self.setRoot(x)
                self.getRoot().setParent(None)
            else:
                b_dad.setLeft(x)
                self.setRoot(other_tree.getRoot())

        # last step - delete x and fix new concatenated AVL tree
        self.last_node = other_tree.Max()
        self.updateFields(x)
        self.delete(self_size)  # delete x
        return diff_heights

    """searches for a *value* in the list
    
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    """

    def search(self, val):
        if val is None or self.empty():
            return -1
        arr_lst = self.listToArray()
        for i in range(len(arr_lst)):
            if arr_lst[i] == val:
                return i
        return -1
