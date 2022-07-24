using System;

namespace Prime_Number_Checker
{
    class Program
    {
        static void Main(string[] args)
        {
            string a;
            ulong num=0;
            Console.Title = "Prime Number Checker";
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.SetCursorPosition(20, 0);
            Console.WriteLine("A simple Program to Check Prime Numbers");
            Console.ForegroundColor = ConsoleColor.DarkCyan;
            Console.Write("\nEnter a Number=");
            a = Console.ReadLine();
            try
            {
                num = Convert.ToUInt64(a);
            }
            catch(Exception e)
            {
                Console.ForegroundColor = ConsoleColor.DarkGreen;
                Console.WriteLine("\n{0} is not a Prime Number", a);
                entr();
                return;
            }
            Console.ForegroundColor = ConsoleColor.DarkYellow;
            Console.WriteLine("\n{0} is{1} a Prime Number",num,ck(num)?"":" not");
            entr();
        }
        static bool ck(ulong n)
        {
            if (n == 0)
                return false;
            for (ulong i = 2; i < n; i++)
            {
                if (n % i == 0)
                    return false;
            }
            return true;
        }
        static void entr()
        {
            Console.ForegroundColor = ConsoleColor.White;
            char cv = '\0';
            Console.WriteLine("\nPress Enter To Continue");
            while(true)
            {
                cv = Console.ReadKey(true).KeyChar;
                if (cv == '\r')
                    return;
            }
        }
    }
}
