import java.util.Scanner;

public class PrimeNumbers {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a positive integer: ");
        int num = input.nextInt();

        if (num <= 1) {
            System.out.println(num + " is not a prime number");
        } else if (num == 2 || num == 3) {
            System.out.println(num + " is a prime number");
        } else if (num % 2 == 0 || num % 3 == 0) {
            System.out.println(num + " is not a prime number");
        } else {
            System.out.println(num + " is a prime number");
        }
    }
}
