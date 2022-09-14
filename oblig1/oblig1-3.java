import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


class Node {
  int data;
  public Node foreldre;

  Node(int item) {
    data = item;
    foreldre = null;
  }
}

class ReversedTre {

  public static void main(String[] args) {
    String fileName = args[0];
  
    try {
      File minFil = new File("input/input/" + fileName);
      Scanner sc = new Scanner(minFil);
      int kittenIndex = Integer.parseInt(sc.nextLine().trim());

      // 1.make an array with nodes
      Node[] nodeTree = new Node[100];
      for (int i = 0; i < 100; i++)
        nodeTree[i] = new Node(i);
      
      //2.map the tree to the array
      while (sc.hasNextLine()) {
        String[] lineArr = sc.nextLine().split(" ");// ["23", "13", "19", "32", "22"]
        int foreldreIndex = lineArr.length > 1 ? Integer.parseInt(lineArr[0]) : -1;

        if (foreldreIndex != -1) { // filter out the first and last line
          // 2-1.get the pointer to the parent node
          Node forelNode = nodeTree[foreldreIndex];

          // 2-2.connect every child to it's parent
          for (int i = 1; i < lineArr.length; i++) {
            int number = Integer.parseInt(lineArr[i]);
            nodeTree[number].foreldre = forelNode;
          }
        }
      }
      
      //3.print out the 'sti'
      Node peker = nodeTree[kittenIndex];
      String resultat = "";
      while (peker != null) {
        resultat += " "+peker.data;
        peker = peker.foreldre;
      }
      System.out.println(resultat);
      sc.close();
    } catch (FileNotFoundException e) {
      System.out.println("Error: File <" + fileName + "> can't be found");
    }
    
  } 
}
