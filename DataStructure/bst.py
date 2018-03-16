#coding=utf-8

class node(object):
    '''
    bst的节点
    '''
    def __init__(self,val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None

class bst(object):
    '''
    BST
    '''
    def __init__(self):
        self.root = None

    def inorder_tree_walk(self, p):
        '''
        得到的结果一定是由大到小
        '''
        if p != None:
            self.inorder_tree_walk(p.left)
            print p.val
            self.inorder_tree_walk(p.right)
        # pass
        # return None

    def preorder_tree_walk(self, p):
        if p != None:
            print p.val
            self.inorder_tree_walk(p.left)
            self.inorder_tree_walk(p.right)

    def postorder_tree_walk(self, p):
        if p != None:
            self.inorder_tree_walk(p.left)
            self.inorder_tree_walk(p.right)
            print p.val

    def find_max(self,node):
        p = node
        while p.right != None:
            p = p.right
        return p

    def find_min(self,node):
        p = node
        while p.left != None:
            p = p.left
        return p

    def find_preprocessor(self,val):
        '''
        查找给定值的节点的前驱
        '''
        n = self.search(self.root,val)
        if n == None:
            return None
        #如果存在左子树，就查找左子树里面最大值
        if n.left != None:
            return self.find_max(n.left)
        else:
            #如果没有左子树，就往上找第一个有右子树且左子树里没有x节点的祖先
            p = n.parent
            while p.next != None and p.right != n:
                n = p
                p = p.parent
            return p



    def find_successor(self,val):
        '''
        查找给定值的节点的前驱
        '''
        n = self.search(self.root,val)

        if n == None:
            return None
        #如果存在有，就查找右子树里面最小值
        if n.right != None:
            return self.find_min(n.right)
        else:
            #如果没有右子树，就往上找第一个有右子树且左子树里没有x节点的祖先
            p = n.parent
            while p.next != None and p.left != n:
                n = p
                p = p.parent
            return p
     


    def delete(self, val):
        '''
        删除
        '''
        z = self.search(self.root,val)
        #没找到
        if z == None:
            return None

        if z.left == None and z.right == None:
            #如果是个叶子节点
            if z.parent.left == z:
                z.parent.left = None
            else:
                z.parent.right = None

        elif z.left != None and z.right != None:
            # 如果有两个后继
            # 1.先删掉他的后驱节点
            y = self.find_successor(val)
            # print y.val
            self.delete(y.val)
            # 2.然后将后驱节点的值替换z节点
            z.val = y.val

        # 如果只有一个后继节点，就让父节点
        elif z.left != None:
            if z.parent.left == z:
                z.parent.left = z.left
            else:
                z.parent.right = z.left
        else:
            if z.parent.left == z:
                z.parent.left = z.right
            else:
                z.parent.right = z.right            
        # elif z.left == None:
        #     #如果只有一个后继
        #     z.parent


    def search(self,node,val):
        '''
        search
        val:int
        return:node
        '''
        p = node
        while p != None:
            if p.val == val:
                return p
            elif p.val > val:
                return self.search(p.left, val)
            else:
                return self.search(p.right, val)

    def insert(self, val):
        '''
        insert
        '''
        y = None
        x = self.root
        while x != None:
            y = x
            if x.val > val:
                x = x.left
            else:
                x = x.right
        n = node(val)
        n.parent = y
        if y == None:
            self.root = n
        else:
            if val < y.val:
                y.left = n
            else:
                y.right = n
        # print n.val
        # if y != None:
        #     print y.val

if __name__ == '__main__':
    tree = bst()
    tree.insert(3)
    tree.insert(2)
    tree.insert(6)
    tree.insert(1)
    tree.insert(4)
    tree.insert(5)
    tree.insert(10)
    tree.insert(7)
    # tree.inorder_tree_walk(tree.root)
    # tree.preorder_tree_walk(tree.root)
    # print tree.find_max(tree.root.right).val
    # print tree.find_min(tree.root.right).val
    # print tree.find_successor(6).val
    # print tree.find_preprocessor(6).val
    # print tree.search(tree.root,4).val
    tree.delete(6)
    tree.inorder_tree_walk(tree.root)


        
