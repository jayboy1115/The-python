import java.util.Scanner;

public class MilesPerGallon {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double totalMiles = 0;
        double totalGallons = 0;

        while (true) {
            System.out.print("Enter gallons used (-1 to end): ");
            double gallons = scanner.nextDouble();
            if (gallons == -1) {
                break;
            }

            System.out.print("Enter miles driven: ");
            double miles = scanner.nextDouble();

            double mpg = miles / gallons;
            System.out.printf("The miles/gallon for this tank was %.6f%n", mpg);

            totalMiles += miles;
            totalGallons += gallons;
        }

        double combinedMpg = totalMiles / totalGallons;
        System.out.printf("The overall average miles/gallon was %.6f%n", combinedMpg);
    }
}
