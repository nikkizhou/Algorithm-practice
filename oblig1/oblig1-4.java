import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

class Node {
  int data;
  Node left, right;

  Node(int item) {
    data = item;
    left = right = null;
  }
}

class AvlTre {
  static Node root;

  Node converArrToAvl(int arr[], int start, int end) {
    if (start > end) 
      return null;
    
    int mid = (start + end) / 2;
    Node node = new Node(arr[mid]);

    node.left = converArrToAvl(arr, start, mid - 1);
    node.right = converArrToAvl(arr, mid + 1, end);

    return node;
  }

  void preOrder(Node node) {
    if (node == null) return;
    System.out.print(node.data + " ");
    preOrder(node.left);
    preOrder(node.right);
  }

  int minHeight(Node v) {
    return v == null ? -1 : 1 + Math.min(minHeight(v.left), minHeight(v.right));
  }

  int height(Node v) {
    return v==null ? -1 : 1 + Math.max(height(v.left), height(v.right));
  }

  boolean isBalanced() {
    return height(root) - minHeight(root) <= 1;
  }

  public static void main(String[] args) throws IOException {
    // 1. convert input to array
    int[] arr = {};
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    for (String line = br.readLine(); line != null; line = br.readLine()) {
      arr = Arrays.copyOf(arr, arr.length + 1);
      int x = Integer.parseInt(line);
      arr[arr.length-1] = x;
    }

    //2. convert array to AvlTre
    AvlTre tree = new AvlTre();
    root = tree.converArrToAvl(arr, 0, arr.length - 1);
    System.out.println("Preorder printing of of the tree: ");
    tree.preOrder(root);

    //3. check balance
    System.out.println(tree.isBalanced() 
      ? "\nDette treet ser balansert ut!"
      : "\nDette treet ser ikke helt balansert ut... prøv igjen!"); 
  }
}
