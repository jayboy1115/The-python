public class TableOfSquares {
    public static void main(String[] args) {
	System.out.println("WELCOME TO JOHNSON WORLD");
        System.out.println("number  square  cube");
        for (int row = 0; row <= 5; row++) {
            System.out.printf("%6d %6d %6d%n", row, row * row, row * row * row);
        }
    }
}
