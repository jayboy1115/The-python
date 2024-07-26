import java.util.Scanner;

public class Looping {
	public static void main(String[] args){
	Scanner Johnson = new Scanner(System.in);
	int sum = 0;
	int average = 0;
	for(int counter = 0; counter < 10; counter++){
  	    System.out.print("Enter a number: ");
  	    int numbers = Johnson.nextInt();
	 sum = sum + numbers;
	average = sum/10;
 	}
     System.out.println("the sum is " + sum);
     System.out.println("the average is " + average);
    }
}
