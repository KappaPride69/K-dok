import java.util.*;  

class feladat{
public static void main(String[] args)  
{  
    Scanner sc= new Scanner(System.in);   
    System.out.print("Adj meg egy számoot ");  
    int szam= sc.nextInt();  
    for (int i = 1; i <= szam; i++) {
            if (szam % i == 0) {
                System.out.print(i + " ");
}  
    }
}
}