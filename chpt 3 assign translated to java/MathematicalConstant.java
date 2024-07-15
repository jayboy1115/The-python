import java.text.NumberFormat;

public class MathematicalConstant {
    public static void main(String[] args) {
        System.out.println("Number of terms | Approximation of π");
        System.out.println("-------------|--------------------");
        for (int i = 1; i <= 100; i++) {
            double pi = calculatePi(i);
            NumberFormat formatter = NumberFormat.getInstance();
            formatter.setMinimumFractionDigits(6);
            System.out.println(i + " | " + formatter.format(pi));
            if (pi >= 3.14 && i == 1) {
                System.out.println("First 3.14: " + i + " terms");
            } else if (pi >= 3.141 && i == 2) {
                System.out.println("First 3.141: " + i + " terms");
            } else if (pi >= 3.1415 && i == 3) {
                System.out.println("First 3.1415: " + i + " terms");
            } else if (pi >= 3.14159 && i == 4) {
                System.out.println("First 3.14159: " + i + " terms");
                break;
            }
        }
    }
	public static double calculatePi(int n) {
        double pi = 0.0;
        for (int i = 0; i < n; i++) {
            pi += Math.pow(-1, i) / (2 * i + 1);
        }
        pi *= 4;
        return pi;
    }
}

