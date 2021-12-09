import BST
import util

def read_tree(src):
    with open(src,"r+") as f:
        list = util.js.load(f)
    univ_tree = BST.BSTNode()
    for i in list:
        univ_tree.insert(i[1],i[0])
    return univ_tree
