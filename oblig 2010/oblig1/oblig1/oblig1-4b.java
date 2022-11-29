import java.util.PriorityQueue;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class AvlHeap {
  public void printBalanced(PriorityQueue<Integer> main) {
    int size = main.size();

    //case 1: no more element in que
    if (size == 0) 
      return;
    //case 2: only one element in que
    else if (size == 1) 
      System.out.println(main.poll());
    // case 3: more than one elements in que
    else {
      // 3-1. move half of the que(main) to another queue(left)
      PriorityQueue<Integer> left = new PriorityQueue<Integer>();
      for (int i = 0; i < size / 2; i++) 
        left.add(main.poll());
      
      // 3-2. remove and print the middle 
      int mid = main.poll();
      System.out.println(mid);

      printBalanced(main);
      printBalanced(left);
    }
  }

  public static void main(String[] args) throws IOException{
    AvlHeap heap = new AvlHeap();
    PriorityQueue<Integer> que = new PriorityQueue<Integer>();
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    // 1.convert input to the priority que
    for (String line = br.readLine(); line != null; line = br.readLine()) {
      int value = Integer.parseInt(line);
      que.add(value);
    }

    // 2. print que in a balanced way
    heap.printBalanced(que);
  }
}
