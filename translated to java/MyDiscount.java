public class MyDiscount {
    public static double myDiscount(double price, double discount) {
        double discountAmount = (discount / 100) * price;
        return price - discountAmount;
    }

    public static void main(String[] args) {
        System.out.println(myDiscount(250, 10));
     }
}