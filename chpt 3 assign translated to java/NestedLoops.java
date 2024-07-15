public class NestedLoops {
    public static void main(String[] args) {
        
        for (int row = 0; row < 10; row++) {
            for (int column = 0; column <= row; column++) {
                System.out.print("*");
            }
            System.out.println();
        }

        System.out.println();  

        for (int row = 10; row > 0; row--) {
            for (int column = 0; column < row; column++) {
                System.out.print("*");
            }
            System.out.println();
        }

        System.out.println();  

        for (int row = 0; row < 10; row++) {
            for (int column = 0; column < 10 - row; column++) {
                System.out.print(" ");
            }
            for (int asterik = 0; asterik <= row; asterik++) {
                System.out.print("*");
	    }
            System.out.println();
        }

        System.out.println();  

        for (int row = 10; row > 0; row--) {
            for (int column = 0; column < 10 - row; column++) {
                System.out.print(" ");
            }
            for (int asterik = 0; asterik < row; asterik++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
