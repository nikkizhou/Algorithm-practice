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
  Node root;
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
    if (node == null) {
      node = new Node(key);
      return node;
    }
    if (key < node.data)
      node.left = insertRec(node.left, key);
    else if (key > node.data)
      node.right = insertRec(node.right, key);
    else  //duplicate inserting
      return null;

    return node;
  }

  public void insert(int key) {
    root = insertRec(root, key);
    if (root != null) 
      size++;
  }

  public Node removeRec(Node node, int key) {
    // if there is no matched node??
    if (node == null)
      return null;

    if (key < node.data) {
      node.left = removeRec(node.left, key);
      return node;
    }

    if (key > node.data) {
      node.right = removeRec(node.right, key);
      return node;
    }

    if (node.left == null) {
      return node.right;
    }
    if (node.right == null) {
      return node.left;
    }

    node.data = minValue(node.right);
    node.right = removeRec(node.right, node.data);
    return node;

    // // case 2:if the tree is not empty, recur down the tree
    // // 2-1 try removing key fom left child
    // if (key < node.data) {
    //   node.left = removeRec(node.left, key);
    //   return node;
    // }
    // // 2-2 try removing key from right child
    // else if (key > node.data) {
    //   node.right = removeRec(node.right, key);
    //   return node;
    // }
    // // 2-3 found the matched node
    // else { 
    //   // 2-3-1 node with only one child or no child
    //   if (node.left == null)
    //     return node.right;
    //   else if (node.right == null)
    //     return node.left;

    //   // 2-3-2 node with two children:
    //   // Get the minValue in the right subtree
    //   node.data = minValue(node.right);
    //   // Delete the minValue in the right subtree
    //   node.right = removeRec(node.right, node.data);
    // }

    // return node;
  }

  //????
  public void remove(int key) {
    if (contains(root,key)) {
      size=size-1;
    }
    root = removeRec(root, key);
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
  }
}
