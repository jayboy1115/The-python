class Array3 {
    public static void array3(int[][] array, StringBuilder output) {
        for (int[] row : array) {
            for (int column : row) {
                if (column == 1) {
                    output.append("* ");
                } else {
                    output.append("  ");
                }
            }
            output.append("\n");
        }
    }

    public static void main(String[] args) {
        int[][] array = {
                {1, 0, 1},
                {0, 1, 0},
                {1, 1, 0}
        };
        StringBuilder output = new StringBuilder();
        array3(array, output);
        System.out.println(output.toString());
    }
}
















