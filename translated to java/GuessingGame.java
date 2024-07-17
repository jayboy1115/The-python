import java.util.Random;
import java.util.Scanner;

public class GuessingGame {
    public static void main(String[] args) {
        Random rand = new Random();
        int game = rand.nextInt(1000) + 1;
        int totalTrials = 0;
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("Guess my number between 1 and 1000 with the fewest guesses: ");
            int user = scanner.nextInt();
            totalTrials++;

            if (user == -1) {
                break;
            }

            if (user == game) {
                System.out.printf("Congratulations! You guessed the number in %d trials.%n", totalTrials);
                System.out.print("Do you want to play again? (yes/no): ");
                String playAgain = scanner.next();
                if (playAgain.equalsIgnoreCase("yes")) {
                    game = rand.nextInt(1000) + 1;
                    totalTrials = 0;
                } else {
                    break;
                }
            } else if (user > game) {
                System.out.println("Your guess is too high. Try again!");
            } else {
                System.out.println("Your guess is too low. Try again!");
            }
        }

        scanner.close();
    }
}
