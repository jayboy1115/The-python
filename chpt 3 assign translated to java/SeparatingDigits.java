import java.util.Scanner;

public class SeparatingDigits {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a five-digit integer: ");
        int num = scanner.nextInt();

        for (int row = 0; row < 5; row++) {
            int digit = num % 10;
            System.out.println(digit);
            num = num / 10;
        }
    }
}

