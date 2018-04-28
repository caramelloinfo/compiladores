#trabalho 28/04/208

class Tree :
  def __init__(self, carga, left=None, right=None) :
    self.carga = carga
    self.left  = left
    self.right = right

  def __str__(self) :
    return str(self.carga)


left = Tree(2)
right = Tree(3)

tree = Tree(1, left, right);

def total(tree) :
  if tree == None : return 0
  return total(tree.left) + total(tree.right) + tree.carga

def printTree(tree) :
  if tree == None : return
  print(tree.carga)
  printTree(tree.left)
  printTree(tree.right)
