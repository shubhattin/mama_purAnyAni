import java.util.Scanner;
import java.util.ArrayList;

public class HCF {

    public static void main(String[] args)
    {
        Main a = new Main();
        a.take_input_and_calculate();
        a.display_result();
    }
}

class Main
{
    private ArrayList<Long> num;
    private long gcd;
    private StringBuilder print_set;

    public Main()
    {
        System.out.println("\t\t\tEnter Numbers Seperated by Comma or Spaces e.g :- 12 16 or 12,16");
        num = new ArrayList<Long>();
        print_set = new StringBuilder();
        gcd = 0;
    }

    private boolean inpt()
    {
        System.out.println("Enter Numbers :");
        String set = (new Scanner(System.in)).nextLine();
        final int len = set.length();
        for(int n = len ; n >= 0 ; n--)
        {
            char a = set.charAt(len - n);
            if(a != ' ' && a != ',')
            {
                boolean decimal_status = false;
                StringBuilder temp = new StringBuilder();
                for( ; n != 0 ; n--)
                {
                    char t = set.charAt(len - n);
                    if(t == '-' && temp.length() != 0 || decimal_status && t == '.')
                        return true;
                    if(t != ' ' && t != ',')
                        if((t >= '0' && t <= '9') || t == '-' || t == '.')
                        {
                            decimal_status = t == '.' ? true : decimal_status;
                            temp.append(t);
                        }
                        else
                            return true;
                    else
                        break;
                }
                if (temp.toString().equals("-") || temp.toString().equals("."))
                    return true;
                print_set.append(temp);
                if(n != 0)
                    print_set.append(", ");
                double tmp = Double.parseDouble(temp.toString());
                while((long)tmp != tmp)
                    tmp *= 10;
                num.add(Math.abs((long)tmp));
            }
        }
        return false;
    }

    private void cal()
    {
        long a = num.get(0), b = num.get(1), r = 0;
        for(int x = 0 ; x < num.size() ; x++)
        {
            while(a != 0)
            {
                r = b % a;
                b = a;
                a = r;
            }
            a = b;
            if(x + 2 == num.size())
                break;
            b = num.get(x + 2);
        }
        gcd = a;
    }

    public void take_input_and_calculate()
    {
        if(inpt())
        {
            System.out.println("\nYou Entered Invalid Data\n");
            endprog();
        }
        else if (num.size() < 2)
        {
            System.out.println("\nError - At Least 2 Numbers Required\n");
            endprog();
        }
        cal();
    }

    public void display_result()
    {
        System.out.println("\nHCF of Numbers:");
        System.out.println(print_set);
        System.out.println("Is = " + gcd + '\n');
        endprog();
    }

    private void endprog()
    {
        System.out.print("Press Enter Key To Continue  ");
        (new Scanner(System.in)).nextLine();
        System.exit(0);
    }
}