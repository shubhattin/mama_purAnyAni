using System;
using System.Numerics;
using System.Collections.Generic;
using System.Text;
using System.Linq;

namespace db_data
{
    public class data
    {
        private readonly BigInteger num;
        public List<string> bindata = new List<string>();
        public List<string> decdata = new List<string>();
        public  data(BigInteger num)
        {
            this.num = BigInteger.Abs(num);
        }
        public static string input()
        {
            string mn = "0123456789";
            StringBuilder main = new StringBuilder();
            char a = '\0';            
            while(a != '\r')
            {
                if(main.Length == 0)
                    while (true)
                    {
                        a = Console.ReadKey(true).KeyChar;
                        if (mn.Contains(a))
                        {
                            Console.Write(a);
                            main.Append(a);
                            break;
                        }
                        else
                        {
                            Console.SetCursorPosition(Console.CursorLeft - 1, Console.CursorTop);
                            Console.Write(' ');
                        }
                    }
                a = Console.ReadKey(true).KeyChar;
                if (main.Length == 0 && a == '\x08')
                {
                    Console.SetCursorPosition(Console.CursorLeft - 1, Console.CursorTop);
                    Console.Write(' ');
                }
                else if (a == '\x08')
                {
                    if (Console.CursorLeft == 0)
                        continue;
                    Console.SetCursorPosition(Console.CursorLeft - 1, Console.CursorTop);
                    Console.Write(' ');
                    Console.SetCursorPosition(Console.CursorLeft - 1, Console.CursorTop);
                    main.Length--;
                }
                else if (mn.Contains(a))
                {
                    Console.Write(a);
                    main.Append(a);
                }                         
            }
            return main.ToString();
        }
        public static void entr(string prnt="")
        {
            char tmp = '\0';
            Console.ForegroundColor = ConsoleColor.White;
            Console.WriteLine(prnt == "" ? "Press Enter Key To Continue" : prnt);
            while(true)
            {
                tmp = Console.ReadKey(true).KeyChar;
                if (tmp == '\r')
                    return;
                tmp = '\0';
            }
        }
        private bool check(BigInteger a)
        {
            foreach (char j in a.ToString())
                if ("23456789".Contains(j)) // verifying non binary numbers
                    return true;
            return false;
        }
        private string binset
        {
            set
            {
                bindata.Add(value);
            }
        }
        private string decset
        {
            set
            {
                decdata.Add(value);
            }
        }        
        private void binr()
        {
            int n = 0;
            StringBuilder m = new StringBuilder();
            BigInteger  d = num, c;
            Console.ForegroundColor = ConsoleColor.Green;
            if (d == 0)
            {
                binset = " 2 | 0 - 0";
                binset = "0";
                return;
            }
            while (d != 0)
            {
                c =d % 2;
                binset = string.Format("{0} | {1} - {2}", d != 1 ? "2" : " ", d, c);
                d = (d - c) / 2;
                n++;
                m.Append(c);
            }
            binset = new string(m.ToString().Reverse().ToArray());
        }
        public string converted_binary_number
        {
            get
            {
                if (bindata.Count == 0)
                    binr();
                return bindata[bindata.Count - 1];
            }           
        }
        private void decm()
        {                  
            if (check(num))
            {
                decset = "The Number Entered by You Can Not Be Converted To a Decimal Number";
                return;
            }
            BigInteger c = 0, d = 0;
            string m = num.ToString();
            int b = m.Length;
            Console.ForegroundColor = ConsoleColor.Green;
            for (int n = 0; n < b; n++)
            {
                c = (m[n] - 48) * BigInteger.Pow(2, b - n - 1);
                d += c;
                decset = string.Format("{0}*2^{1} = {2}", m[n], b - n - 1, c);
            }
            decset = d.ToString();
        }
        public string conveted_decimal_number
        {
            get
            {
                if (decdata.Count == 0)
                    decm();
                return decdata[decdata.Count - 1];
            }            
        }
    }
}