public class NestedLooping {
    public static void main(String[] args) {
        for (int row = 0; row < 10; row++) {
       
            for (int column = 0; column <= row; column++) {
                System.out.print("*");
            }
            System.out.print("   ");

            for (int column = 0; column < 10 - row; column++) {
                System.out.print("*");
            }
            System.out.print("   ");

            for (int column = 0; column < 10 - row; column++) {
                System.out.print(" ");
            }
            for (int asterik = 0; asterik <= row; asterik++) {
                System.out.print("*");
            }
            System.out.print("   ");

            for (int column = 0; column < row; column++) {
                System.out.print(" ");
            }
            for (int asterik = 0; asterik < 10 - row; asterik++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}

