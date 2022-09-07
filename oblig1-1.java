// Operasjonen size bør være O(1)?
//java BinaryTreeSet input_100 | cmp - output/output/output_100   show: - output/output/output_100 differ: char 2, line 1
import java.io.File; 
import java.io.FileNotFoundException; 
import java.util.Scanner;

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
    if (node == null) {
      node = new Node(key);
      return node;
    }
    if (key < node.data)
      node.left = insertRec(node.left, key);
    else if (key > node.data)
      node.right = insertRec(node.right, key);

    
    return node;
  }
  
  public void insert(int key) {
    root = insertRec(root, key);
    size++;
  }


  public Node removeRec(Node node, int key) {
    /* 1. Base Case: If the tree is empty */
    if (node == null)
      return null;

    /* Otherwise, recur down the tree */
    if (key < node.data)
      node.left = removeRec(node.left, key);
    else if (key > node.data)
      node.right = removeRec(node.right, key);

    // if key=node.data
    else {
      // 2.& 3. node with only one child or no child
      if (node.left == null)
        return node.right;
      else if (node.right == null)
        return node.left;

      // 4.node with two children:
      // Get the inorder successor (smallest in the right subtree)
      node.data = minValue(node.right);
      // And then Delete the inorder successor
      node.right = removeRec(node.right, node.data);
    }

    
    return node;
  }

  public void remove(int key) {
    root = removeRec(root, key);
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

  // int height(Node node) {
  //   if (node == null)
  //     return -1;
  //   else {
  //     return Math.max(height(node.right), height(node.left)) + 1;
  //   }
  // }

  // void printPreorder(Node node) {
  //   if (node == null)
  //     return;
  //   System.out.print(node.data + " ");
  //   printPreorder(node.left);
  //   printPreorder(node.right);
  // }
  

  public static void main(String[] args) {
    BinaryTreeSet tree = new BinaryTreeSet();
    String fileName = args[0];
    
    try {
      File minFil = new File("input/input/"+fileName);
      Scanner sc = new Scanner(minFil);
      while (sc.hasNextLine()) {
        String[] lineArr = sc.nextLine().split(" ");
        int i = lineArr.length>1 ? Integer.parseInt(lineArr[1]) : -1;
      
        switch (lineArr[0]) {
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
      sc.close();
    } catch (FileNotFoundException e) {
      System.out.println("Error: File <"+fileName+"> can't be found");
    }
  }
}
