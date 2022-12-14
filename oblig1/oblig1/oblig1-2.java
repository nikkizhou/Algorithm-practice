import java.util.Deque;
import java.util.LinkedList;
import java.util.List;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class Teque {
  Deque<Integer> frontDque;
  Deque<Integer> backDque;

  public Teque() {
    frontDque = new LinkedList<Integer>();
    backDque = new LinkedList<Integer>();
  }

  public void push_back(int x) {
    backDque.addLast(x);
    reBalance();
  }

  public void push_front(int x) {
    frontDque.addFirst(x);
    reBalance();
  }

  public void push_middle(int x) {
    if (backDque.size() < frontDque.size())
      backDque.addFirst(x);
    else
      frontDque.addLast(x);

    reBalance();
  }

  public int get(int i) {
    List<Integer> frontList = (LinkedList<Integer>) frontDque;
    List<Integer> backList = (LinkedList<Integer>) backDque;

    if (i < frontDque.size())
      return frontList.get(i);
    else
      return backList.get(i - frontDque.size());
  }

  public void reBalance() {
    // if the teque is front heavy, remove the end of frontDque to the head of backDque
    if (frontDque.size() > backDque.size() + 1)
      backDque.addFirst(frontDque.pollLast());
    // verse visa
    else if (backDque.size() > frontDque.size() + 1)
      frontDque.addLast(backDque.pollFirst());
  }
  
  public String toString() {
    return
    "front size: " + frontDque.size()
    + "\nback size:  " + backDque.size()
    + "\nfrontDque: " + frontDque.toString()
    + "\nbackDque: " + backDque.toString();
  }


  public static void main(String[] args) throws IOException{
    Teque teque = new Teque();
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    //int lineNr = 0;
    for (String line = br.readLine(); line != null; line = br.readLine()) {
      String[] arr = line.split(" ");
      int i = arr.length > 1 ? Integer.parseInt(arr[1]) : -1;
      //lineNr++;

      //System.out.println(lineNr);
      switch (arr[0]) {
        case "push_back":
          teque.push_back(i);
          //System.out.println("push_back: " + i);
          break;
        case "push_front":
          teque.push_front(i);
          //System.out.println("push_front: " + i);
          break;
        case "push_middle":
          teque.push_middle(i);
          //System.out.println("push_middle: " + i);
          break;
        case "get":
          System.out.println(teque.get(i)); 
          break;
        default:
          break;
      }
      //System.out.println(teque.toString());
    }
  }
}
