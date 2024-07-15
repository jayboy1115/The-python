import java.util.Scanner;

public class BinaryToDecimal {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a binary number: ");
        int binary = scanner.nextInt();
        int decimal = 0;
        int power = 1;

        while (binary != 0) {
            int digit = binary % 10;
            decimal += digit * power;
            power *= 2;
            binary /= 10;
        }

        System.out.println("Decimal equivalent: " + decimal);
    }
}

