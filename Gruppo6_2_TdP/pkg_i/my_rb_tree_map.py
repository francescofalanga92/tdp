from TdP_collections.map.red_black_tree import RedBlackTreeMap
from TdP_collections.queue.array_queue import ArrayQueue


class MyRBTreeMap(RedBlackTreeMap):
    # -------------------------- nested _Node class --------------------------
    class _Node(RedBlackTreeMap._Node):
        """Node class for red-black tree maintains bit that denotes color."""
        __slots__ = '_left_size', '_right_size'  # add additional data member to the Node class

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._left_size = 0
            self._right_size = 0

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            walk = p
            parent = self.parent(walk)
            while parent is not None:  # keep walking parent
                if self.left(parent) == walk:
                    parent._node._left_size -= 1
                else:
                    parent._node._right_size -= 1
                walk = parent
                parent = self.parent(walk)
            if k == p.key():
                self.delete(p)  # rely on positional version
                return  # successful deletion complete
            self._rebalance_access(p)  # hook for balanced tree subclasses
        raise KeyError('Key Error: ' + repr(k))

    def _rotate(self, p):
        """Rotate Position p above its parent.

        Switches between these configurations, depending on whether p==a or p==b.

              b                  a
             / \                /  \
            a  t2             t0   b
           / \                     / \
          t0  t1                  t1  t2

        Caller should ensure that p is not the root.
        """
        """Rotate Position p above its parent."""
        x = p._node
        y = x._parent  # we assume this exists
        z = y._parent  # grandparent (possibly None)
        if z is None:
            self._root = x  # x becomes root
            x._parent = None
        else:
            self._relink(z, x, y == z._left)  # x becomes a direct child of z
        # now rotate x and y, including transfer of middle subtree
        if x == y._left:
            self._relink(y, x._right, True)  # x._right becomes left child of y
            self._relink(x, y, False)  # y becomes right child of x
            y._left_size = x._right_size
            x._right_size = y._left_size + y._left_size + 1
        else:
            self._relink(y, x._left, False)  # x._left becomes right child of y
            self._relink(x, y, True)  # y becomes left child of x
            y._right_size = x._left_size
            x._left_size = y._left_size + y._left_size + 1

    def _rebalance_insert(self, p):
        walk = p
        parent = self.parent(walk)
        while parent is not None:  # keep walking parent
            if self.left(parent) == walk:
                parent._node._left_size += 1
            else:
                parent._node._right_size += 1
            walk = parent
            parent = self.parent(walk)
        self._resolve_red(p)  # new node is always red

    def _black_depth(self):
        """Return black depth of RB Tree."""
        walk = self.root()
        black_depth = 1
        while self.left(walk) is not None:  # keep walking left
            walk = self.left(walk)
            if not super()._is_red(walk):
                black_depth += 1
        return black_depth

    def _find_black_parent_right(self, bd1):
        """Return black position of specified depth on right of root."""
        bd = self._black_depth()
        if bd < bd1:
            raise ValueError("La profondità specificata è più grande di quella dell'albero.")
        walk = self.root()
        d_bd = bd - bd1 - 1
        while d_bd != 0:
            walk = self.right(walk)
            if not super()._is_red(walk):
                d_bd -= 1
        return walk

    def _find_black_parent_left(self, bd1):
        """Return black position of specified depth on left of root."""
        bd = self._black_depth()
        if bd < bd1:
            raise ValueError("La profondità specificata è più grande di quella dell'albero.")
        walk = self.root()
        d_bd = bd - bd1 - 1
        while d_bd != 0:
            walk = self.left(walk)
            if not super()._is_red(walk):
                d_bd -= 1
        return walk

    def fusion(self, t1):
        maxt = self.last()                               # O(logn)
        mint1 = t1.first()                               # O(logm)
        if mint1.key() < maxt.key():
            raise ValueError("Le chiavi dell'albero passato non sono maggiori delle chiavi di quest'albero.")
        bd_t = self._black_depth()                        # O(logn)
        bd_t1 = t1._black_depth()                         # O(logm)
        len1 = len(self)
        len2 = len(t1)
        self._size = len1 + len2
        node = t1._validate(mint1)
        del t1[mint1.key()]                                # O(logm)
        node._parent = None

        if bd_t == bd_t1:
            self._root._parent = node
            node._left = self._root
            self._root = node
            if not t1.is_empty():
                t1._root._parent = node
                node._right = t1._root

        elif bd_t > bd_t1:
            bp = self._validate(self._find_black_parent_right(bd_t1))           # O(log(m))
            node._left = bp._right
            bp._right = node
            node._parent = bp
            node._right = t1._root
            node._red = True
            child = self._make_position(node._left)
            self._rebalance_insert(child)               # O(logn)
        else:
            bp = t1._validate(t1._find_black_parent_left(bd_t))                 # O(log(n))
            node._right = bp._left
            bp._left = node
            node._parent = bp
            node._left = self._root
            node._red = True
            self._root = t1._root
            child = self._make_position(node._right)
            self._rebalance_insert(child)               # O(logm)
        t1._root = None
        t1._size = 0

    def split(self, k):
        p = self.find_position(k)                       # O(logn)
        if p is None or p.key() != k:
            raise ValueError("La chiave k non appartiene all'albero.")
        node = self.validate(p)
        t1 = node._left
        t2 = node._right


        self._root = None
        self._size = 0
        return t1, t2

    def breadthfirst(self):
        """Iterator breadth first of Tree Positions"""
        if not self.is_empty():
            fringe = ArrayQueue()
        fringe.enqueue(self.root())
        while not fringe.is_empty():
            p = fringe.dequeue()
            yield p
            if p is not None:
                fringe.enqueue(self.left(p))
                fringe.enqueue(self.right(p))

    def __str__(self):
        if self.is_empty():
            raise ValueError("L'abero è vuoto.")
        for p in self.breadthfirst():
            if p is None:
                to_print += ",#"
            elif self.is_root(p):
                to_print = '{' + str(p.key())
            elif self._is_red(p):
                to_print += ",\033[1;31;0m" + str(p.key()) + "\033[0m"
            else:
                to_print += "," + str(p.key())
        to_print += "}"
        return to_print
