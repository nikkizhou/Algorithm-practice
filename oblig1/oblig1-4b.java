import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

class balancedHeap {

  public static void main(String[] args) throws IOException{
    // 1. convert input to heap
    int[] arr = {};
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    for (String line = br.readLine(); line != null; line = br.readLine()) {
      arr = Arrays.copyOf(arr, arr.length + 1);
      int x = Integer.parseInt(line);
      arr[arr.length - 1] = x;
    }

    //2.convert heap to AvlTre
  }

  
}
