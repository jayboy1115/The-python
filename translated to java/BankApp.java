  import java.util.Scanner;

public class BankApp {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        System.out.printf("Welcome to Johnson Kolo Bank, %s!%n", name);
        double balance = 0;
        while (true) {
            System.out.print("Enter D to deposit, E to withdraw, or F to check balance: ");
            String alphabet = scanner.next().toUpperCase();
            if (alphabet.equals("D")) {
                System.out.print("Enter the amount you want to deposit: ");
                double deposit = scanner.nextDouble();
                balance += deposit;
                System.out.printf("Deposit successful! Your new balance is %.2f%n", balance);
            } else if (alphabet.equals("E")) {
                System.out.print("Enter the amount you want to withdraw: ");
                double withdraw = scanner.nextDouble();
                if (withdraw < 0) {
                    System.out.println("Withdrawal amount cannot be negative!");
                } else if (withdraw > balance) {
                    System.out.println("Insufficient funds!");
                } else {
                    balance -= withdraw;
                    System.out.printf("Withdrawal successful! Your new balance is %.2f%n", balance);
                }
            } else if (alphabet.equals("F")) {
                System.out.printf("Your current balance is %.2f%n", balance);
            } else {
                System.out.println("Invalid input! Please try again.");
     }   
    }
   }
}
