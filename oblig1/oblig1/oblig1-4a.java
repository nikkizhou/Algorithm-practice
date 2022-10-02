import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;



class AvlArr {

  void printBalanced(int arr[], int start, int end) {
    if (start > end) 
      return;
    
    int mid = (start + end) / 2;
    System.out.println(arr[mid]);
    
    printBalanced(arr, mid + 1, end);
    printBalanced(arr, start, mid - 1);
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

    //2. print array in a balanced way
    AvlArr tree = new AvlArr();
    tree.printBalanced(arr, 0, arr.length - 1);
  }
} 
