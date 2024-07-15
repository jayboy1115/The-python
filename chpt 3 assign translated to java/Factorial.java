import java.util.Scanner;

public class Factorial {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a nonnegative integer: ");
        int num = scanner.nextInt();
        long factorial = calculateFactorial(num);
        System.out.printf("The factorial of %d is %d%n", num, factorial);
    }

    public static long calculateFactorial(int n) {
        long result = 1;
        for (int row = 1; row <= n; row++) {
            result *= row;
        }
        return result;
    }
}
