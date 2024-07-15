import java.util.Scanner;

public class Palindromes {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

	System.out.println("WELCOME TO JOHNSON WORLD");

        System.out.print("Enter a five-digit integer: ");
        int num = scanner.nextInt();

        int a = num / 10000;
        int b = (num / 1000) % 10;
        int c = (num / 100) % 10;
        int d = (num / 10) % 10;
        int e = num % 10;

        if (a == e && b == d) {
            System.out.printf("%d is a palindrome.%n", num);
        } else {
            System.out.printf("%d is not a palindrome.%n", num);
        }
    }
}
