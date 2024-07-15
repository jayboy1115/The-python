import java.util.Scanner;

public class TuringTest {
    public static void main(String[] args) {
        System.out.println("WELCOME TO JOHNSON MEDICAL DIAGNOSIS");
        System.out.print("What is your problem? ");
        Scanner scanner = new Scanner(System.in);
        String userInput = scanner.nextLine(); 

        System.out.print("Have you had this problem before (yes or no)? ");
        userInput = scanner.nextLine();

        if (userInput.toLowerCase().equals("yes")) {
            System.out.println("Well, you have it again.");
        } else if (userInput.toLowerCase().equals("no")) {
            System.out.println("Well, you have it now.");
        } else {
            System.out.println("Invalid input. Please answer yes or no.");
        }
    }
}
