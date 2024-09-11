import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class BankTest {
    private Bank bank;

    @BeforeEach
    void setUp() {
        bank = new Bank();
    }

    @Test
    void testCreateAccount() {
        int accountNumber = bank.createAccount("John Doe", "1234");
        assertNotNull(bank.getAccount(accountNumber));
    }

    @Test
    void testGetAccount() {
        int accountNumber = bank.createAccount("John Doe", "1234");
        Account account = bank.getAccount(accountNumber);
        assertEquals("John Doe", account.getAccountHolderName());
    }

    @Test
    void testDepositWithPin() {
        int accountNumber = bank.createAccount("John Doe", "1234");
        bank.deposit(accountNumber, "1234", 100.00);
        assertEquals(100.00, bank.getAccount(accountNumber).getBalance());
    }

    @Test
    void testDepositInvalidPin() {
        int accountNumber = bank.createAccount("John Doe", "1234");
        assertThrows(IllegalArgumentException.class, () -> bank.deposit(accountNumber, "5678", 100.00));
    }

    @Test
    void testWithdrawWithPin() {
        int accountNumber = bank.createAccount("John Doe", "1234");
        bank.deposit(accountNumber, "1234", 100.00);
        bank.withdraw(accountNumber, "1234", 50.00);
        assertEquals(50.00, bank.getAccount(accountNumber).getBalance());
    }

    @Test
    void testWithdrawInvalidPin() {
        int accountNumber = bank.createAccount("John Doe", "1234");
        bank.deposit(accountNumber, "1234", 100.00);
        assertThrows(IllegalArgumentException.class, () -> bank.withdraw(accountNumber, "5678", 50.00));
    }

    @Test
    void testTransferWithPin() {
        int fromAccountNumber = bank.createAccount("John Doe", "1234");
        int toAccountNumber = bank.createAccount("Jane Doe", "5678");
        bank.deposit(fromAccountNumber, "1234", 100.00);
        bank.transfer(fromAccountNumber, toAccountNumber, "1234", 50.00);
        assertEquals(50.00, bank.getAccount(fromAccountNumber).getBalance());
        assertEquals(50.00, bank.getAccount(toAccountNumber).getBalance());
    }

    @Test
    void testTransferInvalidPin() {
        int fromAccountNumber = bank.createAccount("John Doe", "1234");
        int toAccountNumber = bank.createAccount("Jane Doe", "5678");
        bank.deposit(fromAccountNumber, "1234", 100.00);
        assertThrows(IllegalArgumentException.class, () -> bank.transfer(fromAccountNumber, toAccountNumber, "5678", 50.00));
    }

    @Test
    void testCreateAccountInvalidPinLength() {
        assertThrows(IllegalArgumentException.class, () -> bank.createAccount("John Doe", "123"));
        assertThrows(IllegalArgumentException.class, () -> bank.createAccount("John Doe", "12345"));
    }

    @Test
    void testCloseAccount() {
        int accountNumber = bank.createAccount("John Doe", "1234");
        bank.closeAccount(accountNumber, "1234");
        assertNull(bank.getAccount(accountNumber));
    }

    @Test
    void testCloseAccountInvalidPin() {
        int accountNumber = bank.createAccount("John Doe", "1234");
        assertThrows(IllegalArgumentException.class, () -> bank.closeAccount(accountNumber, "5678"));
    }

    @Test
    void testCloseAccountInvalidAccountNumber() {
        assertThrows(IllegalArgumentException.class, () -> bank.closeAccount(12345, "1234"));
    }

}
