import java.util.Scanner;

public class BankApp {
    private final Bank bank;
    private final Scanner scanner;

    public BankApp() {
        bank = new Bank();
        scanner = new Scanner(System.in);
    }

    public void run() {
        while (true) {
            System.out.println("1. Create Account");
            System.out.println("2. Deposit");
            System.out.println("3. Withdraw");
            System.out.println("4. Transfer");
            System.out.println("5. Close Account");
            System.out.println("6. Exit");

            System.out.print("Choose an option: ");
            int option = Integer.parseInt(scanner.nextLine());

            switch (option) {
                case 1:
                    createAccount();
                    break;
                case 2:
                    deposit();
                    break;
                case 3:
                    withdraw();
                    break;
                case 4:
                    transfer();
                    break;
                case 5:
                    closeAccount();
                    break;
                case 6:
                    System.out.println("Exiting...");
                    return;
                default:
                    System.out.println("Invalid option. Please choose a valid option.");
            }
        }
    }

    private void createAccount() {
        System.out.print("Enter account holder name: ");
        String accountHolderName = scanner.nextLine();
        System.out.print("Enter PIN: ");
        String pin = scanner.nextLine();

        int accountNumber = bank.createAccount(accountHolderName, pin);
        System.out.println("Account created successfully. Account number: " + accountNumber);
    }

    private void deposit() {
        System.out.print("Enter account number: ");
        int accountNumber = Integer.parseInt(scanner.nextLine());
        System.out.print("Enter PIN: ");
        String pin = scanner.nextLine();
        System.out.print("Enter amount to deposit: ");
        double amount = Double.parseDouble(scanner.nextLine());

        bank.deposit(accountNumber, pin, amount);
        System.out.println("Deposit successful.");
    }

    private void withdraw() {
        System.out.print("Enter account number: ");
        int accountNumber = Integer.parseInt(scanner.nextLine());
        System.out.print("Enter PIN: ");
        String pin = scanner.nextLine();
        System.out.print("Enter amount to withdraw: ");
        double amount = Double.parseDouble(scanner.nextLine());

        bank.withdraw(accountNumber, pin, amount);
        System.out.println("Withdrawal successful.");
    }

    private void transfer() {
        System.out.print("Enter from account number: ");
        int fromAccountNumber = Integer.parseInt(scanner.nextLine());
        System.out.print("Enter PIN: ");
        String pin = scanner.nextLine();
        System.out.print("Enter to account number: ");
        int toAccountNumber = Integer.parseInt(scanner.nextLine());
        System.out.print("Enter amount to transfer: ");
        double amount = Double.parseDouble(scanner.nextLine());

        bank.transfer(fromAccountNumber, toAccountNumber, pin, amount);
        System.out.println("Transfer successful.");
    }

    private void closeAccount() {
        System.out.print("Enter account number: ");
        int accountNumber = Integer.parseInt(scanner.nextLine());
        System.out.print("Enter PIN: ");
        String pin = scanner.nextLine();

        bank.closeAccount(accountNumber, pin);
        System.out.println("Account closed successfully.");
    }

    public static void main(String[] args) {
        BankApp bankApp = new BankApp();
        bankApp.run();
    }
}
