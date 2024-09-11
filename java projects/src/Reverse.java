public class Reverse {
    public static int[] reverseArray(int[] array) {
        int left = 0;
        int right = array.length - 1;
        while (left < right) {
            int num = array[left];
            array[left] = array[right];
            array[right] = num;
            left++;
            right--;
        }
        return array;
    }
}
