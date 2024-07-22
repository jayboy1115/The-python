public class OnlyFloats {
    public static int onlyFloats(Object a, Object b) {
        int count = 0;
        if (a instanceof Float || a instanceof Double) {
            count++;
        }
        if (b instanceof Float || b instanceof Double) {
            count++;
        }
        return count;
    }
public static void main(String[] args) {
        System.out.println(onlyFloats(5.0, 2.1));
    }
}
