import java.util.Scanner;

public class StudentScores {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int passCount = 0;

        for (int counter = 0; counter < 15; counter++) {
            System.out.print("Enter score for student " + (counter + 1) + ": ");
            int score = scanner.nextInt();

            if (score >= 45) {
                passCount++;
            }
        }

        System.out.println("Number of students who passed: " + passCount);
        System.out.println("Number of students who failed: " + (15 - passCount));
    }
}

