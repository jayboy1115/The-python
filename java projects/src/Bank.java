import java.util.ArrayList;
import java.util.concurrent.atomic.AtomicInteger;


public class Bank {
    private final ArrayList<Account> accounts;
    private final AtomicInteger nextAccountNumber = new AtomicInteger(1000000000);

    public Bank() {
        accounts = new ArrayList<>();
    }

    public int createAccount(String accountHolderName, String pin) {
        if (pin.length() != 4) {
            throw new IllegalArgumentException("PIN must be four digits");
        }
        // Generate a 10-digit account number
        int accountNumber = nextAccountNumber.getAndIncrement();
        Account account = new Account(accountNumber, accountHolderName, pin);
        accounts.add(account);
        return accountNumber;
    }



    public void deposit(int accountNumber, String pin, double amount) {
        for (Account account : accounts) {
            if (account.getAccountNumber() == accountNumber && account.getPin().equals(pin)) {
                account.deposit(amount);
                return;
            }
        }
        throw new IllegalArgumentException("Invalid account number or PIN");
    }

    public void withdraw(int accountNumber, String pin, double amount) {
        for (Account account : accounts) {
            if (account.getAccountNumber() == accountNumber && account.getPin().equals(pin)) {
                account.withdraw(amount);
                return;
            }
        }
        throw new IllegalArgumentException("Invalid account number or PIN");
    }

    public void transfer(int fromAccountNumber, int toAccountNumber, String pin, double amount) {
        Account fromAccount = null;
        Account toAccount = null;
        for (Account account : accounts) {
            if (account.getAccountNumber() == fromAccountNumber && account.getPin().equals(pin)) {
                fromAccount = account;
            }
            if (account.getAccountNumber() == toAccountNumber) {
                toAccount = account;
            }
        }
        if (fromAccount == null || toAccount == null) {
            throw new IllegalArgumentException("Invalid account number or PIN");
        }
        fromAccount.withdraw(amount);
        toAccount.deposit(amount);
    }

    public void closeAccount(int accountNumber, String pin) {
        Account account = accounts.stream()
                .filter(a -> a.getAccountNumber() == accountNumber && a.getPin().equals(pin))
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("Invalid account number or PIN"));
        accounts.remove(account);
    }

    public Account getAccount(int accountNumber) {
        for (Account account : accounts) {
            if (account.getAccountNumber() == accountNumber) {
                return account;
            }
        }
        return null;
    }
}
