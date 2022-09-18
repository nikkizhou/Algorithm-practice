import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;


class Node {
  int data;
  Node left, right;

  Node(int item) {
    data = item;
    left = right = null;
  }
}

class BinaryTreeSet {
  Node root = null;
  int size = 0;

  public Node search(Node node, int key) {
    if (node == null || node.data == key)
      return node;
    if (node.data < key)
      return search(node.right, key);
    return search(node.left, key);
  }

  public boolean contains(Node node, int key) {
    return search(node, key) != null;
  }

  
  public Node insertRec(Node node, int key) {
    if (node == null) 
      return new Node(key);
      
    if (key < node.data)
      node.left = insertRec(node.left, key);
    else if (key > node.data)
      node.right = insertRec(node.right, key);
    else if(key == node.data)
      return null;
    return node;
  }
  
  public void insert(int key) {
    root = insertRec(root, key);
    if (root!= null) 
      size++;
  }


  public Node removeRec(Node node, int key) {
    //case 1 : If the tree is empty or if key doesn't match any node data
    if (node == null)
      return null;
    //case 2:if the tree is not empty, recur down the tree
    // 2-1 try inserting key to left child
    if (key < node.data)   
      node.left = removeRec(node.left, key);
    // 2-2 try inserting key to right child
    else if (key > node.data) 
      node.right = removeRec(node.right, key);
    // 2-3 found the matched node
    else { 
      // 2-3-1 node with only one child or no child
      if (node.left == null)
        return node.right;
      else if (node.right == null)
        return node.left;

      // 2-3-2 node with two children:
      // Get the inorder successor (smallest in the right subtree)
      node.data = minValue(node.right);
      // Delete the inorder successor
      node.right = removeRec(node.right, node.data);
    }

    return node;
  }

  public void remove(int key) {
    root = removeRec(root, key);
    if (root!=null) 
      size--;
  }

  int size(Node node) {
    return size;
  }

  public int minValue(Node node) {
    int minv = node.data;
    while (node.left != null) {
      minv = node.left.data;
      node = node.left;
    }
    return minv;
  }

  void preOrder(Node node) {
    if (node == null)
      return;
    System.out.print(node.data + " ");
    preOrder(node.left);
    preOrder(node.right);
  }
  

  public static void main(String[] args) throws IOException{
    BinaryTreeSet tree = new BinaryTreeSet();
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    for (String line = br.readLine(); line != null; line = br.readLine()) {
      String[] arr = line.split(" ");
      int i = arr.length > 1 ? Integer.parseInt(arr[1]) : -1;
      switch (arr[0]) {
        case "insert":
          tree.insert(i);
          break;
        case "remove":
          tree.remove(i);
          break;
        case "contains":
          System.out.println(tree.contains(tree.root, i));
          break;
        case "size":
          System.out.println(tree.size(tree.root));
          break;
        default:
          break;
      }
    }
    tree.preOrder(tree.root);
    
  }
}
