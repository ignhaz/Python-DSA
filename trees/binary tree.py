import math
class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.value = val

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.value,end=' ')

def preorder(root):
    if root is not None:
        print(root.value,end=' ')
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root is not None:
        preorder(root.left)
        print(root.value,end=' ')
        preorder(root.right)

def maxheight(root):
    if root == None:  
        return 0    #if height starts from 1.
    else:
        lefth = maxheight(root.left)
        righth = maxheight(root.right)

    return max(lefth,righth) + 1

def diameter(root):
    if root == None:
        return 0
    p_diam = 1 + maxheight(root.left) + maxheight(root.right)
    lc_diam = diameter(root.left)
    rc_diam = diameter(root.right)

    return max(p_diam,max(lc_diam,rc_diam))

max_diam = 0
def Odiameter(root):
    if root == None:
        return 0
    
    lc_height = Odiameter(root.left)
    rc_height = Odiameter(root.right)

    global max_diam
    max_diam = max(max_diam, 1 + lc_height + rc_height)

    return 1 + max(lc_height, rc_height)

def printknode(root,k):
    if root == None:
        return
    if k == 0:
        print(root.value,end=' ')
    else:
        printknode(root.left,k-1)
        printknode(root.right, k-1)

def levelorder(root):
    if root == None:
        return
    queue = []
    queue.append(root)

    while len(queue) > 0:
        print(queue[0].value,end=' ')
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

def sizeoftree(root):
    if root is None:
        return 0
    else:
        leftsize = sizeoftree(root.left)
        rightsize = sizeoftree(root.right)
    return leftsize + rightsize + 1

def maxoftree(root):
    if root is None:
        return -math.inf
    else:
        return max(root.value, max(maxoftree(root.left),maxoftree(root.right)))   

def helper(root):
    max_level_visted = [0]
    leftview(root,max_level_visted,1)

def leftview(root,max_level_visited,curr_level):
    if root == None:
        return
    if max_level_visited[0] < curr_level:
        print(root.value,end=' ')
        max_level_visited[0] = curr_level
    leftview(root.left,max_level_visited,curr_level+1)
    leftview(root.right,max_level_visited,curr_level+1)

def leftview_2(root):
    queue = []
    queue.append(root)

    while len(queue) != 0:
        n = len(queue)
        for i in range(0,n):
            temp = queue[0]
            queue.pop(0)
            if i == 0:
                print(temp.value,end=' ')
            if temp.left != None:
                queue.append(temp.left)
            if temp.right != None:
                queue.append(temp.right)

def spiral(root):
    if root is None:
        return 
    
    q = [] 
    s = []
    q.append(root)
    left_right = True
    while (len(q)):
        n = len(q)
        for i in range(0,n):
            temp = q[0]
            q.pop(0)
            if left_right:
                print(temp.value,end=' ')
            else:
                s.append(temp.value)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        if left_right == False:
            while len(s):
                print(s.pop(),end=' ')
            left_right = True
        else:
            left_right = False

def spiral_2(root):
    if root == None:
        return
    
    s1 = []
    s2 = []
    s1.append(root)
    while len(s1) or len(s2):
        while len(s1):
            temp = s1.pop()
            print(temp.value,end=' ')
            if temp.left:
                s2.append(temp.left)
            if temp.right:
                s2.append(temp.right)
        while len(s2):
            temp = s2.pop()
            print(temp.value,end=' ')
            if temp.right:
                s1.append(temp.right)
            if temp.left:
                s1.append(temp.left)

def getpath(root, path, val):
    if root is None:
        return False
    
    path.append(root.value)
    if root.value == val:
        return True
    if getpath(root.left,path,val) or getpath(root.right,path,val):
        return True
    
    path.pop()
    return False

def getLCA(root,val1,val2):
    path1 = []
    path2 = []
    if getpath(root,path1,val1) == False or getpath(root,path2,val2) == False:
        return None
    
    i = 0 
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right = Node(7)
root.left.right.right = Node(8)
root.left.left.left.left = Node(9)
root.left.right.right.right = Node(10)

print ("Preorder: ")
preorder(root)
 
print ("\nInorder: ")
inorder(root)
 
print ("\nPostorder: ")
postorder(root)


h = maxheight(root)
print ("\nheight of the tree:",h)

print ("\nPrint nodes at distance k: ")
printknode(root, 2)

print('\nPrint level order traversal: ')
levelorder(root)

s = sizeoftree(root)
print('\nSize of the tree:',s)

m = maxoftree(root)
print('\nMaximum element in the tree:',m)

print('\nLeft view of the tree:')
helper(root)

print('\nLeft view of the tree(method 2):')
leftview_2(root)

print('\nSpiral traversal:')
spiral(root)

print('\nSpiral traversal (method2):')
spiral_2(root)

d = diameter(root)
print('\nDiameter of the tree:',d)

Odiameter(root)
print("The diameter of Tree (efficient way):",max_diam)

path = []
getpath(root,path,10)
print('\nThe path from root to desired node:',path)

lca = getLCA(root,9,3)
print('\nLowest common ancestor:',lca)