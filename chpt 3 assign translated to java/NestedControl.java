import java.util.Scanner;

public class NestedControl {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double largest = Double.NEGATIVE_INFINITY;
        double secondLargest = Double.NEGATIVE_INFINITY;

        for (int row = 0; row < 10; row++) {
            System.out.print("Enter number " + (row+1) + ": ");
            double num = scanner.nextDouble();

        if (num > largest) {
                secondLargest = largest;
                largest = num;
            } else if (num > secondLargest) {
                secondLargest = num;
            }
        }
	System.out.println("The two largest values are " + largest + " and " + secondLargest);
    }
}
