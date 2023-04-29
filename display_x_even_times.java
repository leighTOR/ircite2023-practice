import java.util.Scanner;

public class Main {
    static void displayXEvenTimes(int x, char c) {
        if (x % 2 == 0) {
            for(int i = 0; i < x; i++) {
                System.out.println(c);
            }
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter x: ");
        int x = scan.nextInt();

        System.out.print("Enter the character: ");
        char c = scan.next().charAt(0);

        displayXEvenTimes(x, c);
    }
}