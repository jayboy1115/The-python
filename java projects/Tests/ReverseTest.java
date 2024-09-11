import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

public class ReverseTest {

    @Test
    void testReverseArray() {
        int[] array = {4, 5, 2, 1, 6};
        int[] expected = {6, 1, 2, 5, 4};
        int[] result = Reverse.reverseArray(array);
        assertArrayEquals(expected, result);
    }

    @Test
    void testReverseArray_SingleElement() {
        int[] array = {1};
        int[] expected = {1};
        int[] result = Reverse.reverseArray(array);
        assertArrayEquals(expected, result);
    }

    @Test
    void testReverseArray_EmptyArray() {
        int[] array = {};
        int[] expected = {};
        int[] result = Reverse.reverseArray(array);
        assertArrayEquals(expected, result);
    }

    @Test
    void testReverseArray_DuplicateElements() {
        int[] array = {1, 2, 2, 3, 4};
        int[] expected = {4, 3, 2, 2, 1};
        int[] result = Reverse.reverseArray(array);
        assertArrayEquals(expected, result);
    }
}
