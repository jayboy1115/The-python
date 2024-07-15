import java.math.BigDecimal;

public class Approximation {
    public static void main(String[] args) {
        BigDecimal e = estimateE(10);
        System.out.println("Estimated value of e: " + e);
    }

    public static BigDecimal estimateE(int n) {
        BigDecimal e = BigDecimal.ZERO;
        for (int i = 0; i < n; i++) {
            e = e.add(BigDecimal.ONE.divide(factorial(i)));
        }
        return e;
    }

    public static BigDecimal factorial(int n) {
        BigDecimal fact = BigDecimal.ONE;
        for (int i = 1; i <= n; i++) {
            fact = fact.multiply(BigDecimal.valueOf(i));
        }
        return fact;
    }
}
