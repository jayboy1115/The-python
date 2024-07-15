import java.util.Scanner;

public class MultiplicationTable {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = scanner.nextInt();
        printMultiplicationTable(num);
    }

    public static void printMultiplicationTable(int num) {
        for (int count = 1; count <= 10; count++) {
            System.out.println(num + "x" + count + "=" + num * count);
        }
    }
}