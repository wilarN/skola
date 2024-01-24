using System;

namespace Selektioner
{
    class Discount
    {
        static void Main(string[] args)
        {
            Console.Write("How old are you?: ");
            int age = Convert.ToInt32(Console.ReadLine());
            // in %
            /*
             [0] --> Student
             [1] --> Senior
             [2] --> Youth
             */
            float[] discounts = { 0.2f, 0.15f, 0.1f };

            float total_discount = 0.0f;

            if (age <= 18)
            {
                Console.Write("Student? ´yes/no´");
                bool student;

                if (Console.ReadLine().ToLower() == "yes")
                    student = true;
                else
                    student = false;
                // Kid
                if (!student)   {
                    // No student but youth
                    Console.WriteLine("No student discount, but you get youth discount...");
                    total_discount = discounts[2];
                }
                else
                {
                    // Student
                    Console.WriteLine("Student discount");
                    total_discount = discounts[0];

                }
            }
            else if (age >= 65) { 
                // Senior
                Console.WriteLine("Senior discount");
                total_discount = discounts[1];
            }
            else {
                // Full price
                Console.WriteLine("No discount");
                total_discount = 0.0f;
            }
            Console.WriteLine("Your discount is: " + total_discount * 100 + "%");
            Console.ReadKey();

        }
    }
}
