import java.util.Random;
import java.util.Scanner;

public class ArithmeticQuiz {
    public static void main(String[] args) {
        Random rand = new Random();
        Scanner scanner = new Scanner(System.in);
        int score = 0;
        int attempts = 10;

        while (attempts > 0) {
            int num1 = rand.nextInt(10) + 1;
            int num2 = rand.nextInt(10) + 1;
            int answer = num1 + num2;

            System.out.printf("What is %d + %d? (%d attempts left)%n", num1, num2, attempts);
            int userAnswer = scanner.nextInt();

            if (userAnswer == answer) {
                System.out.println("Correct!");
                score++;
            } else {
                System.out.println("Incorrect. The correct answer is " + answer + ".");
            }

            attempts--;
        }

        System.out.println("Your final score is " + score + " out of 10.");
    }
}
