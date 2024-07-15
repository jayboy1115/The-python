import java.util.Scanner;

public class Arithmetic {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] numbers = new int[4];

        for (int row = 0; row < 4; row++) {
            System.out.print("Enter integer " + (row+1) + ": ");
            numbers[row] = scanner.nextInt();
        }

        int sum = 0;
        for (int num : numbers) {
            sum += num;
        }
        double average = (double) sum / 4;
        int product = 1;
        for (int num : numbers) {
            product *= num;
        }
        int smallest = numbers[0];
        int largest = numbers[0];
        for (int row = 1; row < 4; row++) {
            if (numbers[row] < smallest) {
                smallest = numbers[row];
            }
            if (numbers[row] > largest) {
                largest = numbers[row];
            }
        }

        System.out.println("Sum: " + sum);
        System.out.println("Average: " + average);
        System.out.println("Product: " + product);
        System.out.println("Smallest: " + smallest);
        System.out.println("Largest: " + largest);
    }
}
