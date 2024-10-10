import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.Scanner;

public class MenstrualCycleApp {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        LocalDate lastPeriodDate = getLastPeriodDate(scanner);
        int cycleLength = getCycleLength(scanner);
        int periodLength = getPeriodLength(scanner);

        LocalDate nextPeriodDate = calculateNextPeriodDate(lastPeriodDate, cycleLength);
        LocalDate ovulationDate = calculateOvulationDate(nextPeriodDate, cycleLength);

        printResults(nextPeriodDate, ovulationDate);

        scanner.close();
    }

    private static LocalDate getLastPeriodDate(Scanner scanner) {
        System.out.println("Enter the date of your last period (yyyy-mm-dd): ");
        String[] dateParts = scanner.nextLine().split("-");
        return LocalDate.of(Integer.parseInt(dateParts[0]), Integer.parseInt(dateParts[1]), Integer.parseInt(dateParts[2]));
    }

    private static int getCycleLength(Scanner scanner) {
        System.out.println("Enter the average length of your cycle: ");
        return scanner.nextInt();
    }

    private static int getPeriodLength(Scanner scanner) {
        System.out.println("Enter the average length of your period: ");
        return scanner.nextInt();
    }

    private static LocalDate calculateNextPeriodDate(LocalDate lastPeriodDate, int cycleLength) {
        return lastPeriodDate.plusDays(cycleLength);
    }

    private static LocalDate calculateOvulationDate(LocalDate nextPeriodDate, int cycleLength) {
        return nextPeriodDate.minusDays(cycleLength / 2);
    }

    private static void printResults(LocalDate nextPeriodDate, LocalDate ovulationDate) {
        System.out.println("Your next period is expected on: " + nextPeriodDate);
        System.out.println("Ovulation is expected on: " + ovulationDate);
    }
}

