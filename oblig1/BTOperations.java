class Node {
  int data;
  Node left, right;

  Node(int item) {
    data = item;
    left = right = null;
  }
}

class BinaryTree {
  Node root;

  //---------------different orders------------
  void printPostorder(Node node) {
    if (node == null)
      return;
    printPostorder(node.left);
    printPostorder(node.right);
    System.out.print(node.data + " ");
  }

  void printInorder(Node node) {
    if (node == null)
      return;
    printInorder(node.left);
    System.out.print(node.data + " ");
    printInorder(node.right);
  }

  void printPreorder(Node node) {
    if (node == null)
      return;
    System.out.print(node.data + " ");
    printPreorder(node.left);
    printPreorder(node.right);
  }

  //-----------search and insersion------------
  public Node search(Node node, int key) {
    if (node == null || node.data == key)
      return node;
    if (node.data < key)
      return search(node.right, key);
    return search(node.left, key);
  }

  public Node insert(Node node, int key) {
    if (node == null)
      return new Node(key);
    if (key < node.data)
      node.left = insert(node.left, key);
    else if (key > node.data)
      node.right = insert(node.right, key);

    return node;
  }
  
  //----------------remove------------------
  Node deleteRec(Node node, int key) {
    /* 1. Base Case: If the tree is empty */
    if (node == null)
      return null;

    /* Otherwise, recur down the tree */
    if (key < node.data)
      node.left = deleteRec(node.left, key);
    else if (key > node.data)
      node.right = deleteRec(node.right, key);

    //if key=node.data
    else {
      // 2.& 3. node with only one child or no child
      if (node.left == null)
        return node.right;
      else if (node.right == null)
        return node.left;

      //4.node with two children: 
      //Get the inorder successor (smallest in the right subtree)
      node.data = minValue(node.right);
      //And then Delete the inorder successor
      node.right = deleteRec(node.right, node.data);
    }

    return node;
  }
  
  // ---------------height, minValue-------------------
  int height(Node node) {
    if (node == null)
      return -1;
    else {
      return Math.max(height(node.right), height(node.left)) + 1;
    }
  }

  int minValue(Node node) {
    int minv = node.data;
    while (node.left != null) {
      minv = node.left.data;
      node = node.left;
    }
    return minv;
  }


  public static void main(String[] args) {
    BinaryTree tree = new BinaryTree();
    tree.root = new Node(5);

    tree.insert(tree.root, 8);
    tree.insert(tree.root, 10);
    tree.insert(tree.root, 3);
    tree.insert(tree.root, 41);
    tree.insert(tree.root, 31);
    tree.insert(tree.root, 21);
    // tree.deleteRec(tree.root, 21);
    // tree.deleteRec(tree.root, 18);
    
    System.out.println("Height of tree is : " +
        tree.height(tree.root));

    System.out.println(
        "Preorder traversal of binary tree is ");
    tree.printPreorder(tree.root);

    System.out.println(
        "\nInorder traversal of binary tree is ");
    tree.printInorder(tree.root);

    System.out.println(
        "\nPostorder traversal of binary tree is ");
    tree.printPostorder(tree.root);
  }
}
