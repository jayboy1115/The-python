import java.util.Scanner;

public class ValidatingInput {
    public static void main(String[] args) {
        int passes = 0;
        int failures = 0;
	int number1;
	int number2;



        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("Enter first integer (1 or 2): ");
            number1 = scanner.nextInt();
            if (number1 == 1 || number1 == 2) {
                passes++;
                break;
            } else {
                failures++;
                System.out.println("Invalid input. Please enter 1 or 2.");
            }
        }

        while (true) {
            System.out.print("Enter second integer (1 or 2): ");
            number2 = scanner.nextInt();
            if (number2 == 1 || number2 == 2) {
                passes++;
                break;
            } else {
                failures++;
                System.out.println("Invalid input. Please enter 1 or 2.");
            }
        }

        int total = number1 + number2;
        System.out.printf("The sum of %d and %d is %d%n", number1, number2, total);
        System.out.println("Number of passes: " + passes);
        System.out.println("Number of failures: " + failures);
    }
}

