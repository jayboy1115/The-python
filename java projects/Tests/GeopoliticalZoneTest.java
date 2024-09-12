import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;


public class GeopoliticalZoneTest {

    @Test
    void testNorthEast() {
        GeopoliticalZone zone = GeopoliticalZone.NORTHEAST;
        String[] expectedStates = {"Borno", "Yobe", "Bauchi", "Gombe", "Adamawa", "Taraba"};
        assertArrayEquals(expectedStates, zone.getStates());
    }

    @Test
    void testNorthWest() {
        GeopoliticalZone zone = GeopoliticalZone.NORTHWEST;
        String[] expectedStates = {"Kaduna", "Kano", "Katsina", "Sokoto", "Zamfara", "Kebbi", "Jigawa"};
        assertArrayEquals(expectedStates, zone.getStates());
    }

    @Test
    void testNorthCentral() {
        GeopoliticalZone zone = GeopoliticalZone.NORTHCENTRAL;
        String[] expectedStates = {"Kwara", "Niger", "Plateau", "Benue", "Kogi", "Nasarawa", "FCT"};
        assertArrayEquals(expectedStates, zone.getStates());
    }

    @Test
    void testSouthSouth() {
        GeopoliticalZone zone = GeopoliticalZone.SOUTHSOUTH;
        String[] expectedStates = {"Akwa Ibom", "Cross River", "Bayelsa", "Rivers", "Delta", "Edo"};
        assertArrayEquals(expectedStates, zone.getStates());
    }

    @Test
    void testSouthEast() {
        GeopoliticalZone zone = GeopoliticalZone.SOUTHEAST;
        String[] expectedStates = {"Abia", "Anambra", "Enugu", "Imo", "Ebonyi"};
        assertArrayEquals(expectedStates, zone.getStates());
    }

    @Test
    void testSouthWest() {
        GeopoliticalZone zone = GeopoliticalZone.SOUTHWEST;
        String[] expectedStates = {"Ogun", "Oyo", "Osun", "Ondo", "Ekiti", "Lagos"};
        assertArrayEquals(expectedStates, zone.getStates());
    }
}
