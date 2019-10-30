//David McGinn
//CMPS 4143
//10-30-19
//A simple guessing game where the user is given
//clues about wether the generated number is higher or
//lower than their guess

import java.util.Random;
import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Random r = new Random();
    Scanner kb = new Scanner(System.in);
    
    int rando = r.nextInt(101-1)+1;
    boolean correct = false;
    int guesses = 0;
    int guess;
    System.out.println("David McGinn\nCMPS 4143\n10-30-19");
    System.out.println("A simple game allowing the user to guess a number chosen");
    System.out.print("At random\n\n\n");
    System.out.println("I am thinking of a number between 1 & 100");
    while(!correct){
      guess = kb.nextInt();
      System.out.println(guess);
      guesses++;
      if(guess == rando){
        System.out.println("correct you got it in " + guesses + " Tries");
        correct = !correct;//flip correct to true
      }
      else if(guess > rando){
        System.out.println("Lower");
      }
      else{
        System.out.println("Higher");
      }
      }
    kb.close();
  }
}
