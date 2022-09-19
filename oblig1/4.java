import java.util.PriorityQueue;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class AvlTreHeap {
  PriorityQueue<Integer> que = new PriorityQueue<Integer>();

  public void printBalanced(PriorityQueue<Integer> right) {
    int size = right.size();
    if (size == 1) {
      System.out.println(right.poll());
    }

    else {
      // move half of the que(right) to another queue(left)
      PriorityQueue<Integer> left = new PriorityQueue<Integer>();
      for (int i = 0; i < size / 2; i++) {
        left.add(right.poll());
      }
      // remove and print the middle 
      int mid = right.poll();
      System.out.println(mid);

      //
      if (right.size() >= 1) {
        printBalanced(right);
        printBalanced(left);
      } else {
        System.out.println(left.poll());
      }
    }
  }

  public static void main(String[] args) throws IOException{
    AvlTreHeap heap = new AvlTreHeap();
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    // convert input to the priority que in heap
    for (String line = br.readLine(); line != null; line = br.readLine()) {
      int x = Integer.parseInt(line);
      heap.que.add(x);
    }

    // convert the heap to avl
    heap.printBalanced(heap.que);

  }
}
