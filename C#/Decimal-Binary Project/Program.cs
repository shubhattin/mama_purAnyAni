using System;
using System.Numerics;
using db_data;

namespace Decimal_Binary
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "Decimal-Binary Converter";
            Console.SetWindowSize(Console.LargestWindowWidth-40,Console.LargestWindowHeight-10);
            string d, b;
            char key;
            bool status1 = true, status2 = true;
            BigInteger number = new BigInteger();
            Console.Clear();
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("\t\t\t\tDecimal-Binary Converter");
            Console.ForegroundColor = ConsoleColor.Green;
            Console.Write("Enter a Number = ");
            number = BigInteger.Parse(data.input());           
            Console.CursorVisible = false;
            data num = new data(number);
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.Write("\n\nDecimal Form = ");            
            d = num.conveted_decimal_number;
            Console.ForegroundColor = ConsoleColor.White;
            Console.WriteLine(d);
            Console.Beep();
            Console.ForegroundColor = ConsoleColor.Red;
            Console.Write("Binary Form = ");            
            b = num.converted_binary_number;
            Console.ForegroundColor = ConsoleColor.White;
            Console.WriteLine(b + '\n');
            Console.Beep();
            status1 = !d.Contains("a");
            K1:
            if (status1)
            {
                Console.Write("Press 1 key :-");
                Console.ForegroundColor = ConsoleColor.Magenta;
                Console.WriteLine(" To see Solution For Converting From Binary To Decimal");
            }
            K2:
            if(status2)
            {
                Console.ForegroundColor = ConsoleColor.White;
                Console.Write("Press 2 key :-");
                Console.ForegroundColor = ConsoleColor.Blue;
                Console.WriteLine(" To see Solution For Converting From Decimal To Binary");
            }
            Console.ForegroundColor = ConsoleColor.White;
            Console.Write("Press Esc key :-");
            Console.ForegroundColor = ConsoleColor.DarkYellow;
            Console.WriteLine(" To Exit");
            while(true)
            {
                key = Console.ReadKey(true).KeyChar;
                if (key == '\x1b')
                    return;
                else if (status1 && key == '1')
                {
                    Console.Clear();
                    Console.Title = "Solution For Converting From Binary To Decimal";
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.Write("Binary Form = ");
                    Console.ForegroundColor = ConsoleColor.White;
                    Console.WriteLine(number);
                    Console.ForegroundColor = ConsoleColor.Yellow;
                    Console.WriteLine("\nDecimal Conversion:\nSolution:-\n");
                    Console.ForegroundColor = ConsoleColor.Green;
                    for (int tm = 0; tm < num.decdata.Count - 1; tm++)
                        Console.WriteLine(num.decdata[tm]);
                    Console.ForegroundColor = ConsoleColor.Cyan;
                    Console.Write("\nConverted Decimal Form = ");
                    Console.ForegroundColor = ConsoleColor.White;
                    Console.WriteLine(num.conveted_decimal_number + '\n');
                    status1 = false;
                    goto K2;
                }
                else if (status2 && key == '2')
                {
                    Console.Clear();
                    Console.Title = "Solution For Converting From Decimal To Binary";
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.Write("Decimal Form = ");
                    Console.ForegroundColor = ConsoleColor.White;
                    Console.WriteLine(number);
                    Console.ForegroundColor = ConsoleColor.Yellow;
                    Console.WriteLine("\nBinary Conversion:\nSolution:-\n");
                    Console.ForegroundColor = ConsoleColor.Green;
                    for (int tm = 0; tm < num.bindata.Count - 1; tm++)
                        Console.WriteLine(num.bindata[tm]);
                    Console.ForegroundColor = ConsoleColor.Cyan;
                    Console.Write("\nConverted Binary Form = ");
                    Console.ForegroundColor = ConsoleColor.White;
                    Console.WriteLine(num.converted_binary_number + '\n');
                    status2 = false;
                    goto K1;
                }
            }
        }
    }
}