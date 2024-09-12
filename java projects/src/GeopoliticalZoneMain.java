import java.util.Scanner;

public class GeopoliticalZoneMain {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a geopolitical zone (NORTHEAST, NORTHWEST, NORTHCENTRAL, SOUTHSOUTH, SOUTHEAST, SOUTHWEST):");
        String zone = scanner.next().toUpperCase();
        GeopoliticalZone geopoliticalZone = GeopoliticalZone.valueOf(zone);
        System.out.println("States in " + zone + ":");
        for (String state : geopoliticalZone.getStates()) {
            System.out.println(state);
        }
    }
}

