using System;

namespace ConsoleApp1
{
    class Program
    {
        static void cycle(int count, int[] myArray)
        {
            foreach (int num in myArray)
            {
                Console.WriteLine(num);
                if (count != -1)
                {
                    count += num;
                }
            }
        }

        static void Main(string[] args)
        {
            int[] myArray = { 21, 2, 41, 9, 11 };
            int count = 0;

            cycle(count, myArray);

            Console.WriteLine("Total Sum: " + count);
            for (int i = 0; i < myArray.Length; i++)
            {
                myArray[i] = myArray[i] * 2;
            }

            cycle(-1, myArray);

            Console.ReadKey();
            
        }
    }
}
