import java.lang.Math;

public class DivideOrSquare {
    public static double divideOrSquare(int num) {
        if (num % 5 == 0) {
            return Math.sqrt(num);
        } else {
            return num % 5;
        }
    }

    public static void main(String[] args) {
        System.out.println(divideOrSquare(8));

      }
 }