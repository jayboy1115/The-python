import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class AccountTest {
    private Account account;

    @BeforeEach
    void setUp() {
        account = new Account(0, "johnson",  "1234");
    }

    @Test
    void testThatAccountCanDeposit() {
        account.deposit(100.00);
        assertEquals(100.00, account.getBalance());
    }

    @Test
    void testThatNegativeValueCannotBeDeposited() {
        assertThrows(IllegalArgumentException.class, () -> account.deposit(-100.00));
    }

    @Test
    void testThatAccountCanCreatePin() {
        assertEquals("1234", account.getPin());
    }

    @Test
    void testThatAccountBalanceDoesNotChangeWhenWithdrawingZero() {
        account.withdraw(0);
        assertEquals(0, account.getBalance());
    }

    @Test
    void testThatAccountCannotWithdrawNegativeAmount() {
        assertThrows(IllegalArgumentException.class, () -> account.withdraw(-100.00));
    }

    @Test
    void testThatAccountCannotWithdrawMoreThanBalance() {
        account.deposit(100.00);
        assertThrows(IllegalArgumentException.class, () -> account.withdraw(200.00));
    }

    @Test
    void testThatAccountCanWithdraw() {
        account.deposit(100.00);
        account.withdraw(50.00);
        assertEquals(50.00, account.getBalance());
    }
}