import java.util.Scanner;

public class Main {
    static int findDistinctNumber(int a, int b, int c) {
        if (a == b && b == c) {
            return a;
        } else if (a == b) {
            return c;
        } else if (b == c) {
            return a;
        } else if (c == a) {
            return b;
        } else {
            return -999;
        }
    }
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter a: ");
        int a = scan.nextInt();

        System.out.print("Enter b: ");
        int b = scan.nextInt();

        System.out.print("Enter c: ");
        int c = scan.nextInt();

        int value = findDistinctNumber(a, b, c);
        System.out.println("Returned value from function = " + value);
    }
}