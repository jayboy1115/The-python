import java.util.Scanner;

public class InvestmentReturn {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter initial investment: ");
        double principal = scanner.nextDouble();
        System.out.print("Enter annual interest rate (in %): ");
        double rate = scanner.nextDouble();

        for (int year = 1; year <= 30; year++) {
            double amount = principal * Math.pow(1 + rate / 100, year);
            System.out.printf("Year %d: $%.2f%n", year, amount);
        }
    }
}
