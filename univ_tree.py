import BST
import util
def saveBST(dict,dest):
    univ_tree = BST.BSTNode()
    for i in dict:
        univ_tree.insert(dict[i],dict[i]['count'] + 1)
    tree_list = []
    univ_tree.preorder_save(tree_list)
    with open(dest,'w') as f:
        f.write(util.js.dumps(tree_list,ensure_ascii=False,indent=4))
