import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Array3Test {

    @Test
    public void testArray3_AllOnes() {
        String expectedOutput = "* * * \n* * * \n* * * \n";
        assertEquals(expectedOutput, getOutput(new int[][]{{1, 1, 1}, {1, 1, 1}, {1, 1, 1}}));
    }

    @Test
    public void testArray3_AllZeros() {
        String expectedOutput = "      \n      \n      \n";
        assertEquals(expectedOutput, getOutput(new int[][]{{0, 0, 0}, {0, 0, 0}, {0, 0, 0}}));
    }

    @Test
    public void testArray3_Mixed() {
        String expectedOutput = "*   * \n  *   \n* *   \n";
        assertEquals(expectedOutput, getOutput(new int[][]{{1, 0, 1}, {0, 1, 0}, {1, 1, 0}}));
    }

    private String getOutput(int[][] array) {
        StringBuilder output = new StringBuilder();
        Array3.array3(array, output);
        return output.toString();
    }
}








