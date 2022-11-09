import java.util.Scanner;

public class Palindromes {

    public static void main(String[] args) {

        boolean palindrome = true;

        Scanner scan = new Scanner(System.in);
        String original;
        String reversed = "";

        System.out.print("Enter a word or phrase: ");
        original = scan.nextLine();
        original = original.replace(" ", "");

        Palindrome(palindrome, original, reversed);
    }

    private static void Palindrome(boolean palindrome, String original, String reversed) {
        for (int i = original.length() - 1; i >= 0; i--) {
            reversed += original.charAt(i);
        }

        for (int i = 0; i < reversed.length(); i++) {
            if (reversed.charAt(i) != original.charAt(i)) {
                palindrome = false;
            }
        }

        if (palindrome) {
            System.out.println("PALINDROME");
        }
        else {
            System.out.println("Not a Palindrome");
        }
    }
}
