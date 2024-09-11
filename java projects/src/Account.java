public class Account {
    private final int accountNumber;
    private final String accountHolderName;
    private String accountNumberStr = "";
    private final String pin;
    private double balance;

    public Account(int accountNumber, String accountHolderName, String pin) {
        this.accountNumber = accountNumber;
        this.accountHolderName = accountHolderName;
        this.accountNumberStr = accountNumberStr;
        this.pin = pin;
        this.balance = 0;
    }

    public int getAccountNumber() {
        return accountNumber;
    }

    public String getAccountHolderName() {
        return accountHolderName;
    }

    public String getAccountNumberStr() {
        return accountNumberStr;
    }

    public String getPin() {
        return pin;
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        if (amount < 0) {
            throw new IllegalArgumentException("Deposit amount cannot be negative");
        }
        balance += amount;
    }

    public void withdraw(double amount) {
        if (amount < 0) {
            throw new IllegalArgumentException("Withdrawal amount cannot be negative");
        }
        if (amount > balance) {
            throw new IllegalArgumentException("Insufficient funds");
        }
        balance -= amount;
    }
}