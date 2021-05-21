#  Implementation of BST and AVL tree data structures 
#Mara Silva

#creation of a root node of any tree
class root:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
        
#insertion on a BST        
def insert(root, node):
        if root==None:
            root=node
        else:
            if root.data>node.data:
                if root.left==None:
                    root.left=node
                else:
                    insert(root.left, node)
            if root.data<node.data:
                if root.right==None:
                    root.right=node
                else:
                    insert(root.right, node)

#output the data in different ways
#in order visits the nodes in increasing order

def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.data)

        print_inorder(root.right)

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data)

def pre_order(root):
    if root:
        print(root.data)
        pre_order(root.left)
        pre_order(root.right)

#height of a tree
def helper_height(root):
    
    if root==None:
        return 0
    else:
        left=helper_height(root.left)
        right=helper_height(root.right)
        
        if left>right:
             return left+1
        else:
            return right+1

def height(root):
    return helper_height(root)-1

#find if an element is part of the tree   
def find(data, tree):
    
    if tree==None:
        return False
    elif data==tree.data:
        return True
    else:
        if data>tree.data:
            return find(data, tree.right)
        else:
            return find(data, tree.left)

#minimum tree element
def mini(tree, minimum=None):
 
    if tree is not None:
        minimum=tree.data
        return mini(tree.left, minimum)
    else:
        return minimum
    
#maximum tree element
def maxim(tree, maximum=None):
    
    if tree is not None:
        maximum=tree.data
        return maxim(tree.right, maximum)
    else:
        return maximum
        
#The user inputs an element and this function finds the next bigger element
def next_bigger(data, tree, parent=None, granparent=None):
   #base case
    if tree==None:
        msg="The value is not on the tree"
        return msg
    
    # find if root node == to data input
    elif data==tree.data:
        #if the data is found next bigger could be any of this posibilities
        if tree.right:
            return mini(tree.right)
        else:
            if parent:
                if parent.data>data:
                    return parent.data
                else:
                    if granparent:
                        if granparent.data>data:
                            return granparent.data
                        else:
                            msg="The value you entered is the max of the tree"
                            return msg
                        
            #if node doesn't have parent and no right tree
            #then it is the max of the tree
            else:
                msg="The value you entered is the max of the tree"
                return msg
    else:
        #if data isn't the root node searche right or left tree accordingly
        #switch granparent to parent and parent to tree as we go down the tree
        if data>tree.data:
            return next_bigger(data, tree.right, tree, parent)
        else:
            return next_bigger(data, tree.left, tree, parent)
        
        
# Find the parent of a node  
def parenthood(node, tree, parent=None):

    if tree==None:
        return None
    elif node.data==tree.data:
        return parent
    else: 
        parent=tree.data
            
        if node.data>parent:
            return parenthood(node, tree.right, parent)
        else:
            return parenthood(node, tree.left, parent)
        
#Find granparent     
def granparent(node, tree):
    if tree==None or node==None:
        return None
    else:
        parent=parenthood(node, tree)
        if parent==None:
            return None
        else:
            node=root(parent)
            return parenthood(node,tree)

#find a node's uncle    
def uncle(node, tree, parent=None, granparent=None):
    #base case
    if tree==None:
        return None
    
    #if node is found, return uncle if it exists
    elif node.data==tree.data:
        if granparent and granparent.right and granparent.left:
            
            if parent.data==granparent.right.data:
                unclei=granparent.left
            else:
                unclei=granparent.right
            return unclei
        
        else:
            #if granparent doesn't have right nor left child
            #that means that uncle doesn't exist:
            return None
    
    else:
        #search for node in the correct branch
        #switch parent to tree and granparent to parent
        if node.data>tree.data:
            return uncle(node, tree.right, tree, parent)
        else:
            return uncle(node, tree.left, tree, parent)

#get uncle.data        
def get_uncle(node, tree):
    unclei=uncle(node, tree)
    if unclei:
        return unclei.data
    

# getting cousins, simply get uncle's right and left subtree   
def cousins(node, tree):
    if tree==None or node==None:
        return None
    else:
        unclei=uncle(node, tree)
        if unclei:
            if unclei.right and unclei.left:
                return unclei.right.data, unclei.left.data
            if unclei.left:
                return unclei.left.data
            if unclei.right:
                return unclei.right
        else:
            return None
        
#BST deletion
def del_elem(elem, tree,previous=None):
    
    if tree==None:
        return tree
    if tree.data==elem:
                
        if tree.right:
            replacement=mini(tree.right)
            tree.data=replacement
            del_elem(replacement,tree.right,tree)

        
        elif tree.left:
            replacement=maxim(tree.left)
            tree.data=replacement
            del_elem(replacement,tree.left,tree)
            
            
        else:
            if tree.data>previous.data:
                previous.right=None
            elif tree.data<previous.data:
                previous.left=None
            else:
                if previous.right and tree.data==previous.right.data :
                    previous.right=None
                    
                else:
                    previous.left=None
            
            
    else:
        if elem>tree.data:
            del_elem(elem, tree.right,tree)
        else:
            del_elem(elem, tree.left,tree)
            
#Rotations needed on a AVL tree:
def R_rot(tree):
    temp=tree.right
    tree.right=root (tree.data)
    tree.right.right=temp
    tree.right.left=tree.left.right
    tree.data=tree.left.data
    tree.left=tree.left.left
    return tree

def L_rot(tree):
    temp=tree.left
    tree.left=root(tree.data)
    tree.left.left=temp
    tree.left.right=tree.right.left
    tree.data=tree.right.data
    tree.right=tree.right.right
    return tree

def RL(tree):
    R_rot(tree.right)
    L_rot(tree)
    return tree

def LR(tree):
    L_rot(tree.left)
    R_rot(tree)
    return tree

#balance a bst tree
def balance (tree):
    left=height(tree.left)
    
    right=height(tree.right)
        
    is_balanced=left-right
        
    if is_balanced>1:
        if height(tree.left.right)>height(tree.left.left):
            return LR(tree)
        else:
            return R_rot(tree)
        
    if is_balanced<-1:
        if height(tree.right.left)>height(tree.right.right):
            return RL(tree)
        else:
            return L_rot(tree)
        
#AVL insertion
def AVL_insert(tree,new_node,insertion=False, previous=None):
    
    if tree==None:
        tree=new_node
        insertion=True
        
    else:
         if new_node.data>tree.data:
             if tree.right==None:
                 tree.right=new_node
                 insertion=True
             else:
                 AVL_insert(tree.right,new_node,insertion, tree)
         else:
             if tree.left==None:
                 tree.left=new_node
                 insertion=True
             else:
                 AVL_insert(tree.left,new_node,insertion, tree)
        
    
    if insertion is True:
    
        balance(tree)
        
    
    if previous is not None:
           balance(previous)
           
#AVL deletion
def AVL_delete(tree,data, previous=None, deletion=False):
    if tree.data==data:
        del_elem(tree.data, tree)
        deletion=True
        
    else:
        if tree.data>data:
            AVL_delete(tree.left,data, tree, deletion)
        else:
            AVL_delete(tree.right,data, tree, deletion)

    if deletion is True:
        balance(tree)   
    if previous is not None:
        balance(previous)
        
        
    
#----------------TESTINGS-------------------
tree=root(50)
 
insert(tree,root(70))
insert(tree,root(90))
insert(tree,root(40))
insert(tree,root(20))
insert(tree,root(10))
insert(tree,root(30))
insert(tree,root(60))
insert(tree,root(80))

print("In order traversal:")
print_inorder(tree)
print("\n  ")

print("Post order traversal:")
post_order(tree)
print("\n  ")

print("Pre order traversal:")
pre_order(tree)
print("\n  ")

print("Tree height:")
print(height(tree))
print("\n  ")

if find(5, tree)==False:
    print("5 not in the tree \n")
else:
    print("5 in the tree \n")
    
if find(30, tree)==False:
    print("30 not in the tree \n")
else:
    print("30 in the tree \n")
    
print("Next bigger than 30:")    
print(next_bigger(30, tree))
print("\n  ")
print("Next bigger than 80:") 
print(next_bigger(80, tree))
print("\n  ")
print("Next bigger than 90:") 
print(next_bigger(90, tree))
print("\n  ")
print("Next bigger than 50:") 
print(next_bigger(50, tree))
print("\n  ")
print("Next bigger than 70:") 
print(next_bigger(70, tree))
print("\n  ")

print("The maximum tree element: ")
print(maxim(tree))
print("\n  ")

print("The minimum tree element:  ")
print(mini(tree))
print("\n  ")
print(" Node 70 parent:")
print(parenthood(root(70), tree))
print("\n  ")
print(" Node 60 parent:")
print(parenthood(root(60), tree))
print("\n  ")
print(" Node 50 parent:")
print(parenthood(root(50), tree))
print("\n  ")

print(" Node 60 granparent:")
print(granparent(root(60), tree))
print("\n  ")
print(" Node 80 granparent:")
print(granparent(root(80), tree))
print("\n  ")
print(" Node 50 granparent:")
print(granparent(root(50), tree))
print("\n  ")

print(" Node 50 uncle:")
print(get_uncle(root(50), tree))
print("\n  ")
print(" Node 80 uncle:")
print(get_uncle(root(80), tree))
print("\n  ")
print(" Node 20 uncle:")
print(get_uncle(root(20), tree))
print("\n  ")

print(" Node 20 cousins:")
print(cousins(root(20), tree))
print("\n  ")
print(" Node 60 cousins:")
print(cousins(root(60), tree))
print("\n  ")
print(" Node 90 cousins:")
print(cousins(root(90), tree))
print("\n  ")
print(" Node 30 cousins:")
print(cousins(root(30), tree))
print("\n  ")
print(" Node 80 cousins:")
print(cousins(root(80), tree))
print("\n  ")

del_elem(70, tree)
del_elem(30, tree)
del_elem(10, tree)
print("Tree in order traversalafter deletion of nodes:70,30 and 10")
print_inorder(tree)
print("\n  ")


avl_tree=root(10)
AVL_insert(avl_tree, root(85))

AVL_insert(avl_tree, root(15))

AVL_insert(avl_tree, root(70))

AVL_insert(avl_tree, root(20))

AVL_insert(avl_tree, root(60))

AVL_insert(avl_tree, root(30))

AVL_insert(avl_tree, root(50))

AVL_insert(avl_tree, root(65))

AVL_insert(avl_tree, root(80))

AVL_insert(avl_tree, root(90))

AVL_insert(avl_tree, root(40))

AVL_insert(avl_tree, root(5))

AVL_insert(avl_tree, root(55))



print("In order traversal of AVL tree after insertion ")

print_inorder(avl_tree)
print("\n  ")
print("Post order traversal of AVL tree after insertion ")
post_order(avl_tree)
print("\n  ")
print("Pre order traversal of AVL tree after insertion ")
pre_order(avl_tree)

AVL_delete(avl_tree,50)
print("\nIn order traversal of AVL tree after deletion of 50")
print_inorder(avl_tree)
