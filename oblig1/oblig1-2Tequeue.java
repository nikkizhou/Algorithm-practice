import java.util.Deque;
import java.util.LinkedList;
import java.util.List;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

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
    if (frontDque.size() < backDque.size())
      frontDque.addLast(x);
    else
      backDque.addFirst(x);

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
    else if (frontDque.size() < backDque.size() + 1)
      frontDque.addLast(backDque.pollFirst());
  }
  

  public static void main(String[] args) {
    Teque teque = new Teque();
    String fileName = args[0];

    try {
      File minFil = new File("input/input/" + fileName);
      Scanner sc = new Scanner(minFil);
      while (sc.hasNextLine()) {
        String[] lineArr = sc.nextLine().split(" ");
        int i = lineArr.length > 1 ? Integer.parseInt(lineArr[1]) : -1;
        switch (lineArr[0]) {
          case "push_back":
            teque.push_back(i);
            break;
          case "push_front":
            teque.push_front(i);
            break;
          case "push_middle":
            teque.push_middle(i);
            break;
          case "get":
            System.out.println(teque.get(i));
            break;
          default:
            break;
        }
      }
      sc.close();
    } catch (FileNotFoundException e) {
      System.out.println("Error: File <" + fileName + "> can't be found");
    }
  }
}
