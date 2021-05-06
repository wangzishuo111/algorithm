class  Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#[3,5,1,6,2,9,8,null,null,7,4]
a1 = Node(3)
a2 = Node(5)
a3 = Node(1)
a4 = Node(6)
a5 = Node(2)
a6 = Node(9)
a7 = Node(8)
a8 = Node(None)
a9 = Node(None)
a10 = Node(7)
a11 = Node(4)

a1.left = a2
a1.right = a3
a2.left = a4
a2.right = a5
a3.left = a6
a3.right = a7
a5.left = a10
a5.right = a11

#[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
treeb = Node
b1 = treeb(3)
b2 = treeb(5)
b3 = treeb(1)
b4 = treeb(6)
b5 = treeb(7)
b6 = treeb(4)
b7 = treeb(2)
b8 = treeb(None)
b9 = treeb(None)
b10 = treeb(None)
b11 = treeb(None)
b12 = treeb(None)
b13 = treeb(None)
b14 = treeb(9)
b15 = treeb(8)

b1.left = b2
b1.right = b3
b2.left = b4
b2.right = b5
b3.left = b6
b3.right = b7
b7.left = b14
b7.right = b15

def dfs(tree, mylist):
    if tree.val == None:
        return
    if (tree.left == None) and (tree.right == None):
        mylist.append(tree.val)
        return
    if tree.left:
        dfs(tree.left, mylist)
    if tree.right:
        dfs(tree.right, mylist)

mylista = []
mylistb = []
dfs(a1, mylista)
print (mylista)
dfs(b1, mylistb)
print (mylistb)
