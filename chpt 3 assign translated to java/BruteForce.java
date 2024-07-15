public class BruteForce {
    public static void main(String[] args) {
        for (int side1 = 1; side1 <= 20; side1++) {
            for (int side2 = side1; side2 <= 20; side2++) {
                for (int hypotenuse = side2; hypotenuse <= 20; hypotenuse++) {
                    if (side1 * side1 + side2 * side2 == hypotenuse * hypotenuse) {
                        System.out.println(side1 + " " + side2 + " " + hypotenuse);
             }
           }
       }
  }
 }
}
